# coding: utf-8

import paramiko
import re
from time import sleep
import ftplib
from ftplib import FTP
import sys
import os
from NFMSbyDjango import settings

class ParamikoClient(object):
    def __init__(self ,ip, username, password,port=22, timeout=30):
        self.ip = ip
        self.username = username
        self.password = password
        self.port=port
        self.timeout = timeout

        self.client = None

        # 链接失败的重试次数
        self.try_times = 3

    def __connect(self):
        '''
        通过Paramiko进行连接
        :return:
        '''
        while True:
            # 连接过程中可能会抛出异常，比如网络不通、链接超时
            try:
                self.client = paramiko.SSHClient()
                self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.client.connect(self.ip, self.port, self.username, self.password)
                # 如果没有抛出异常说明连接成功，直接返回
                print(u'连接%s成功' % self.ip)
                return
            # 这里不对可能的异常如socket.error, socket.timeout细化，直接一网打尽
            except Exception as e:
                if self.try_times != 0:
                    print(e)
                    print(u'连接%s失败，进行重试' % self.ip)
                    self.try_times -= 1
                else:
                    print(u'重试3次失败，结束程序')
                    return

    def __close(self):
        '''
        关闭Paramiko创建的连接
        :return:
        '''
        if self.client is not None:
            self.client.close()
            self.client=None

    def exec_cmd(self, cmd):
        '''
        执行命令
        :param cmd:
        :return:
        '''
        if self.client is None:
            self.__connect()
        stdin, stdout, stderr = self.client.exec_command(cmd)
        print(stdout.readlines())
        self.__close()



# 定义一个类，表示一台远端linux主机
class Linux(object):
    '''
    通过IP, 用户名，密码，超时时间初始化一个远程Linux主机
    '''
    def __init__(self, ip, username, password,port=22, timeout=30):
        self.ip = ip
        self.username = username
        self.password = password
        self.port=port
        self.timeout = timeout
        # transport和chanel
        self.t = ''
        self.chan = ''
        # 链接失败的重试次数
        self.try_times = 3


    # 调用该方法连接远程主机
    def connect(self):
        while True:
            # 连接过程中可能会抛出异常，比如网络不通、链接超时
            try:
                self.t = paramiko.Transport(sock=(self.ip, 22))
                self.t.connect(username=self.username, password=self.password)
                self.chan = self.t.open_session()
                self.chan.settimeout(self.timeout)
                self.chan.get_pty()
                self.chan.invoke_shell()
                # 如果没有抛出异常说明连接成功，直接返回
                print(u'连接%s成功' % self.ip)
                # 接收到的网络数据解码为str
                print(self.chan.recv(65535).decode('utf-8'))
                return
            # 这里不对可能的异常如socket.error, socket.timeout细化，直接一网打尽
            except Exception as e:
                if self.try_times != 0:
                    print(e)
                    print(u'连接%s失败，进行重试' %self.ip)
                    self.try_times -= 1
                else:
                    print(u'重试3次失败，结束程序')
                    exit(1)

    # 断开连接
    def close(self):
        self.chan.close()
        self.t.close()

    def exec_cmd(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect("128.5.6.21", 22, "lingtj", "lingtj123")
        # client.connect('ssh.example.com')
        stdin, stdout, stderr = client.exec_command('ls -l')
        print(stdout.readlines())
        client.close()

    # 发送要执行的命令
    def send(self, cmd):
        cmd += '\r'
        # 通过命令执行提示符来判断命令是否执行完成
        p = re.compile(r':~ #')

        result = ''
        # 发送要执行的命令
        self.chan.send(cmd)
        # 回显很长的命令可能执行较久，通过循环分批次取回回显
        while True:
            sleep(0.5)
            ret = self.chan.recv(65535)
            if len(ret)==0:
                print("结束")
                break
            ret = ret.decode('utf-8')
            result += ret
            if p.search(ret):
                print(result)
                return result

class DirFileHelper:
    def checkTargetFileOrCreate(self,targetpath,filename):
        '''
        判断指定路径下是否存在指定文件
        :param targetpath:指定路径
        :param filename:目标文件
        :return:
        '''
        # 判断指定路径下是否已经存在指定文件
        fullname = os.path.join(targetpath, filename)
        if os.path.isfile(fullname):
            return "ok"
        else:
            # 不保存在指定文件则创建
            # 先判断指定路径是否存在
            if os.path.exists(targetpath):
                pass
            else:
                # 不存在则创建
                os.makedirs(targetpath)
                # pass
             # 存在目录则创建文件
            try:
                os.mknod(fullname)
                return fullname
            except Exception as e:
                print(e)
                return None


class FtpClient:
    def __init__(self,host,username,pwd,port=21):
        '''
        构造函数 需要url，name，pwd，以及端口

        :param host:
        :param username:
        :param pwd:
        :param port:
        '''
        self.host=host
        self.username=username
        self.pwd=pwd
        self.port=port
        self.url="%s:%s"%(self.host,self.port)

    def __ftpconnect(self):
        ftp=FTP()
        welcome= ftp.connect(self.host,self.port)
        resp=ftp.login(self.username,self.pwd)
        return ftp

    def __testcontect(self):
        '''
        测试是否已连接
        :return:
        '''
        pass

    def download(self,targetpath,filename):
        '''
        公开的下载方法
        :param targetpath:
        :param filename:
        :return:
        '''
        # ftp连接
        ftp=self.__ftpconnect()
        # 下载
        fullname= self.__downloadfile(ftp,self.url,targetpath,filename)
        return fullname

    def __downloadfile(self,ftp,url,targetpath,filename):
        '''
        从指定url下载名为filename的文件下载到本地targetpath路径下
        :param ftp:ftp实例对象
        :param url:ftp下载地址
        :param targetpath:本地路径
        :param filename:下载文件名
        :return:将本地存储的文件全路径返回
        '''
        bufsize=1024
        # 以二进制的方式打开并可写
        dirHelper= DirFileHelper()
        result=dirHelper.checkTargetFileOrCreate(targetpath,filename)
        if result is not None:
            try:
                fileInfo=open(result,'wb')
                ftp.retrbinary('RETR %S'%url,fileInfo.write,bufsize)
                fileInfo.close()
                ftp.quit()
                return result
            #ftp的错误在ftplib中，ftplib.FTP中没有错误
            except ftplib.error_perm:
                print("error:ftp error user:%s,pwd:%s"%(self.username,self.pwd))
                ftp.quit()
                return

class ParamikoConn(object):
    def __init__(self,host,port,user,pwd):
        self.host=host
        self.port=port
        self.user=user
        self.pwd=pwd
        self.ssh=None

    def ssh_connect(self):
        try:
            self.ssh=paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(self.host,self.port,self.user,self.pwd)
        except Exception as e:
            print('ssh %s%s:%s'%(self.host,self.user,e))
            exit()

    def ssh_exec_cmd(self,cmd):
        stdin, stdout, stderr =self.ssh.exec_command(cmd)

        err_list=stderr.readlines()
        if len(err_list)>0:
            print('error:%s'%err_list[0])
            exit()
        else:
            print(stdout.read().decode())

    def ssh_close(self):
        self.ssh.close()

