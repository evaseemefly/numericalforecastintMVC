# coding: utf-8

import paramiko
import re
from time import sleep
from ftplib import FTP

# 定义一个类，表示一台远端linux主机
class Linux(object):
    # 通过IP, 用户名，密码，超时时间初始化一个远程Linux主机
    def __init__(self, ip, username, password, timeout=30):
        self.ip = ip
        self.username = username
        self.password = password
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
            except Exception:
                if self.try_times != 0:
                    print(u'连接%s失败，进行重试' %self.ip)
                    self.try_times -= 1
                else:
                    print(u'重试3次失败，结束程序')
                    exit(1)

    # 断开连接
    def close(self):
        self.chan.close()
        self.t.close()

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
            ret = ret.decode('utf-8')
            result += ret
            if p.search(ret):
                print(result)
                return result

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

    def ftpconnect(self):
        ftp=FTP()
        ftp.connect(self.host,self.port)
        ftp.login(self.username,self.pwd)
        return ftp

    def downloadfile(self,ftp,url,targetpath):
        bufsize=1024
        # 以二进制的方式打开并可写
        fp=open(targetpath,'wb')


        ftp.retrbinary()