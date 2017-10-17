import getpass,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# E:\01开发\numericalforecastintMVC\NFMSbyDjango
BASE_TEMPLATE_DIRS = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
import pexpect


def ssh_command (user, host, password, command):
    """
    This runs a command on the remote host. This could also be done with the
    pxssh class, but this demonstrates what that class does at a simpler level.
    This returns a pexpect.spawn object. This handles the case when you try to
    connect to a new host and ssh asks you if you want to accept the public key
    fingerprint and continue connecting.
    """
    ssh_newkey = 'Are you sure you want to continue connecting'
    # 为 ssh 命令生成一个 spawn 类的子程序对象.
    # <class 'tuple'>: ("module 'pexpect' has no attribute 'spawn'",)
    pexpect.run('ls -la')
    child = pexpect.spawn('ssh -l %s %s %s'%(user, host, command))
    i = child.expect([pexpect.TIMEOUT, ssh_newkey, 'password: '])
    # 如果登录超时，打印出错信息，并退出.
    if i == 0: # Timeout
        print('ERROR!')
        print('SSH could not login. Here is what SSH said:')
        print(child.before, child.after)
        return None
    # 如果 ssh 没有 public key，接受它.
    if i == 1: # SSH does not have the public key. Just accept it.
        child.sendline ('yes')
        child.expect ('password: ')
        i = child.expect([pexpect.TIMEOUT, 'password: '])
        if i == 0: # Timeout

        # print('ERROR!')
            print('SSH could not login. Here is what SSH said:')
            print(child.before, child.after)
            return None
    # 输入密码.
    child.sendline(password)
    return child

def main ():
    # 获得用户指定 ssh 主机域名.
    host = "128.5.6.21"
    # 获得用户指定 ssh 主机用户名.
    user = "lingtj"
    # 获得用户指定 ssh 主机密码.
    password = "lingtj123"
    # 获得用户指定 ssh 主机上即将运行的命令.
    command = "ls"
    child = ssh_command (user, host, password, command)
    # 匹配 pexpect.EOF
    child.expect(pexpect.EOF)
    # 输出命令结果.
    print(child.before)

if __name__ == '__main__':
    try:

        main()
    except Exception as e:
        print(str(e))
        # traceback.print_exc()
        os._exit(1)