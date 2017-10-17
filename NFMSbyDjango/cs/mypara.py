# coding:utf-8
import time
import paramiko
import re


def exec_shell(command):
    '''
        command：传入的要执行的shell命令
    '''
    # f = StringIO.StringIO()
    '''
    由于执行完命令之后会以[lingtj@tlogin ~]$ 结尾
    eg：
    (0)	====20130401  08
warning:smth9: No missing values are being set.
Default missing values will be used.
Be careful of results.

warning:gsnScalarContour is not a valid resource in wbar_contour at this time

warning:gsnScalarContour is not a valid resource in wbar_contour at this time

warning:gsnScalarContour is not a valid resource in wbar_contour at this time

(0)	---------- 006 Hours ------------
warning:NumVectors is not a valid resource in wbar_vector at this time

rasttopnm: writing PPM file
pamtogif: computing colormap...
pamtogif: 3 colors fou
nd
+ '[' -n test17101703.gif ']'
+ mv wbar.gif test17101703.gif
[lingtj@tlogin ~]$ 
************************************************
若执行完命令总是以[lingtj@tlogin ~]$结束
    
    需要对[lingtj@tlogin ~]$进行匹配
    [除“\n”之外的任何单个字符出现一次或多次 @ 多个任意字符 空格 多个任意字符]$
    '''
    header_match = '(\[.+?@.+?\s.+?\]\$)'
    channel.send(command + '\n')
    while True:
        # 将返回的receive data进行接收（二进制）——>转换为utf-8格式
        out = channel.recv(1024).decode('utf-8')
        print(out)
        # f.write(out)
        # 匹配投
        result_match = re.findall(header_match, out)
        '''
        .strip()移除字符串头尾指定的字符（默认为空格）。
        .endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。可选参数"start"与"end"为检索字符串的开始与结束位置。
        '''
        # 有匹配结果并且该匹配结果出现在最后
        # 再跳出循环
        if result_match and out.strip().endswith(result_match[-1]):
            break
    # return


def check_ip(content):
    '''
        从content中取出所有符合xx.120.xx.xx格式的ip地址（xx代表任意多数字）并返回
    '''
    ips = re.findall('\d+\.120\.\d+\.\d+', content)
    return ips


if __name__ == '__main__':
    '''
        host：对应要连接的服务器ip
        port：对应连接服务器的端口
        username：对应访问服务器的用户名
    '''
    host = '128.5.6.21'
    port = 22
    username = "lingtj"
    password = "lingtj123"
    '''
        key_file为secureCRT对应的OpenSSH格式的私钥文件
        可以在secureCRT的'Tools->Convert Private Key to OpenSSH Format...'选择相应的私钥文件转化为OpenSSH格式
        例如：在Windows下保存到'E:\keys\'路径下，保存文件名为'id_rsa'
    '''
    # key_file = 'E:\\keys\\id_rsa'
    # key = paramiko.RSAKey.from_private_key_file(key_file)
    # 不使用之前的调用paramiko.SSHClient的方式，之前使用的exex_command只能执行基本操作语法，无法远程执行shell脚本
    
    # 
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port, username, password)
    # 使用invoke_shell的方法
    # 返回的是一个channel
    channel = client.invoke_shell()
    '''
        下面对应在secureCRT上执行命令的过程
    '''
    exec_shell(
        './zyf/test/sfc.sh 2013040100 6 14.69 30.52 115.91 128.57 test17101703.gif')

    # exec_shell('cd /home/project/api.winyyg.com')
    # out = exec_shell('ls')
    # ips = check_ip(out.getvalue())
    # exec_shell('cat '+ips[0]+'/log/duobao.log')
