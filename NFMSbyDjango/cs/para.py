# from Forecast import utils
import os
from time import sleep
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# E:\01开发\numericalforecastintMVC\NFMSbyDjango
BASE_TEMPLATE_DIRS = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
from Forecast import utils

#
# if __name__=="__main__":
#     # linux_main = utils.Linux("128.5.6.21", "lingtj", "lingtj123")
#     # linux_main.connect()
#     # linux_main.send("cd zyf/test/")
#     client= utils.ParamikoClient("128.5.6.21", "lingtj", "lingtj123")
#     client.exec_cmd("cd zyf/test/")

import paramiko