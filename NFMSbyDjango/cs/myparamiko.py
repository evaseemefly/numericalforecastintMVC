# from Forecast import utils
import os
from time import sleep
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# E:\01开发\numericalforecastintMVC\NFMSbyDjango
BASE_TEMPLATE_DIRS = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# from Forecast import utils

#
# if __name__=="__main__":
#     # linux_main = utils.Linux("128.5.6.21", "lingtj", "lingtj123")
#     # linux_main.connect()
#     # linux_main.send("cd zyf/test/")
#     client= utils.ParamikoClient("128.5.6.21", "lingtj", "lingtj123")
#     client.exec_cmd("cd zyf/test/")

import paramiko as pa

# （一）基于用户名和密码的sshclient的方式登录
# 建立一个ssh client对象
client = pa.SSHClient()
# 允许
parameter1 = 1000
client.set_missing_host_key_policy(pa.AutoAddPolicy())
# ssh.connect("128.5.6.21",22,"lingtj","lingtj123",timeout=20)
client.connect("128.5.6.21",22,"lingtj","lingtj123")
stdin,stdout,stderr= client.exec_command("ls")
print
channel=pa.client.invoke_shell()
print ("Logged in into Site server")
channel.send("cd parent_folder/Sub_folder/script_folder; ./script1.sh %s" % parameter1)
print ("Script executed perfectly")
client.close()

# stdin, stdout, stderr = ssh.exec_command('ls -l')
stdin, stdout, stderr =ssh.exec_command("ls")
# stdin, stdout, stderr = ssh.exec_command("cd zyf/test/")
print(stdout.readlines())
'''
    可以使用如下的方式
    ./zyf/test/sfc.sh 2013040100 6 14.69 30.52 115.91 128.57 mttestresult.gif
    访问指定目录下的 shell脚本
'''
#
stdin, stdout, stderr = ssh.exec_command('./zyf/test/sfc.sh 2013040100 6 14.69 30.52 115.91 128.57 test17101301.gif')
print(stdout.readlines())
stdin, stdout, stderr = ssh.exec_command('./sfc.sh 2013040100 2 23.40 35.53 23.40  125.49 test17101104.gif')
print(stdout.readlines())

# （二）基于用户名和密码的transport方式登录
# 实例化一个transport对象
# trans = paramiko.Transport(("128.5.6.21",22))
# # 建立连接
# t=trans.connect(username='lingtj', password='lingtj123')
# chan=t.open_session()
# chan.settimeout(20)
# chan.get_pty()
# chan.invoke_shell()
# print("连接成功")
# print(chan.recv(65535).decode('utf-8'))
# result = ''
# # 发送要执行的命令
# result=chan.send('ls')
# ret = chan.recv(65535)
# ret = ret.decode('utf-8')
# print(ret)

# 将sshclient的对象的transport指定为以上的trans
# ssh = paramiko.SSHClient()
# ssh._transport = trans
# # 执行命令，和传统方法一样
# # stdin, stdout, stderr = ssh.exec_command('df -hl')
# ssh.exec_command('cd zyf/test')
# stdin, stdout, stderr = ssh.exec_command('ls')
# print(stdout.read().decode())
# # stdin, stdout, stderr = ssh.exec_command('./sfc.sh 2013040100 6 14.69 30.52 115.91 128.57 test17101301.gif')
# stdin, stdout, stderr = ssh.exec_command('./zyf/test/sfc.sh 2013040100 6 14.69 30.52 115.91 128.57 test17101603.gif',timeout=20)
# # sleep(3)
# print(stdout.read().decode())
# stdin, stdout, stderr = ssh.exec_command('ls')
# print(stdout.read().decode())

# （三）将paramiko封装至一个类中
# ssh=utils.ParamikoConn("128.5.6.21",22,"lingtj", "lingtj123")
# ssh.ssh_connect()
# '''
#     此处有问题，执行完之后还是在根目录下？？
# '''
# ssh.ssh_exec_cmd('cd zyf/test')
# ssh.ssh_exec_cmd('ls')
# ssh.ssh_exec_cmd('./zyf/test/sfc.sh 2013040100 6 14.69 30.52 115.91 128.57 test17101301.gif')
# ssh.ssh_exec_cmd('ls')
# ssh.ssh_close()

# （四）
# client = paramiko.SSHClient()
# # 不添加此句会出现：Server  not found in known_hosts的错误
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(hostname="128.5.6.21",username="lingtj", password="lingtj123")
# stdin, stdout, stderr =client.exec_command("ls")
# print(stdout.read().decode())
# # Obtain session
# # session = client.get_transport().open_session()
# # Forward local agent
# # Commands executed after this point will see the forwarded agent on
# # the remote end.
# # 取不到值
# '''
# TypeError: 'NoneType' object is not iterable
# '''
# stdin, stdout, stderr=client.exec_command('./zyf/test/sfc.sh 2013040100 6 14.69 30.52 115.91 128.57 test17101301.gif')
# err_list = stderr.readlines()
# if len(err_list) > 0:
#     print('error:%s' % err_list[0])
#     exit()
# else:
#     print(stdout.read().decode())
# print("结束")

# 关闭连接
# trans.close()

# （五）
# parameter1 = 1000
# pa.client.connect('128.5.6.21', username='user', password='pass')
# # client.connect('128.5.6.21', username='user', password='pass')
# channel = pa.client.invoke_shell()
# print ("Logged in into Site server")
# channel.send("ls" % parameter1)
# print(stdout.readlines())
# print ("Script executed perfectly")
# client.close()