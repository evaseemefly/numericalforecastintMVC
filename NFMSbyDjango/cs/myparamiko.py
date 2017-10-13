# from Forecast import utils
#
# if __name__=="__main__":
#     # linux_main = utils.Linux("128.5.6.21", "lingtj", "lingtj123")
#     # linux_main.connect()
#     # linux_main.send("cd zyf/test/")
#     client= utils.ParamikoClient("128.5.6.21", "lingtj", "lingtj123")
#     client.exec_cmd("cd zyf/test/")

import paramiko

# 建立一个ssh client对象
ssh = paramiko.SSHClient()
# 允许
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("128.5.6.21",22,"lingtj","lingtj123")
# stdin, stdout, stderr = ssh.exec_command('ls -l')
stdin, stdout, stderr =ssh.exec_command("ls")
# stdin, stdout, stderr = ssh.exec_command("cd zyf/test/")
print(stdout.readlines())
# stdin, stdout, stderr = ssh.exec_command('./sfc.sh 2013040100 6 14.69 30.52 115.91 128.57 mttestresult.gif')

# stdin, stdout, stderr = ssh.exec_command('./sfc.sh 2013040100 2 23.40 35.53 23.40  125.49 test17101104.gif')
# print(stdout.readlines())

