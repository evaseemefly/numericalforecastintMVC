import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# E:\01开发\numericalforecastintMVC\NFMSbyDjango
BASE_TEMPLATE_DIRS = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
from Forecast import models

class ViewModel_UserInfo:
    '''
        用户视图模型
    '''
    def __init__(self,name,pwd,delflag,sort,remark):
        '''

        :param name:
        :param pwd:
        :param delflag:
        :param sort:
        :param remark:
        '''
        self.name=name
        self.pwd=pwd
        self.delflag=delflag
        self.sort=sort
        self.remark=remark

class Bootstrap_TreeNode:
    '''
    BootStrap可用的树节点
    '''
    def __init__(self, id,text,url,iconClass):
        '''

        :param id:
        :param text:
        :param url:
        :param iconClass:
        :param children:
        '''
        self.id=id
        self.text=text
        self.url=url
        self.iconClass=iconClass
        self.children=[]
        #return super().__init__(**kwargs)

class Response_Result:
    '''
    返回的响应
    '''
    def __init__(self,code,data):
        '''

        :param code:响应代码
        :param data:响应内容
        '''
        self.resultCode=code
        self.resultData=data

class Request_Data_Latlng:
    '''
    前台发过来的请求数据
    '''
    def __init__(self,date,lon_start,lon_finish,lat_start,lat_finish,element,level,interval):
        '''

        :param date:
        :param lon_start:
        :param lon_finish:
        :param lat_start:
        :param lat_finish:
        :param element:
        :param level:
        :param interval:
        '''
        self.date=date
        self.lon_start=lon_start
        self.lon_finish=lon_finish
        self.lat_start=lat_start
        self.lat_finish=lat_finish
        self.element=element
        self.level=level
        self.interval=interval
        # 最终修改为此种方式——替代在toCmd方法中注释掉的部分
        '''
            调用models包中的cmdinfo
            （1）其中有生成的随机文件名的属性
            （2）生成cmd字符串的方法（或改为属性）
        '''
        # self.cmd_obj = models.CmdInfo("sfc.sh", self.date, self.interval, self.lat_start, self.lat_finish, self.lon_start,self.lon_finish)
        self.cmd_obj = models.CmdInfo("sfc.sh", self.date, self.interval, self.lat_start, self.lat_finish, self.lon_start, self.lon_finish)
        

    @property
    def cmdbyStr(self):
        '''
        （通过属性的方式）根据请求数据生成shell要执行的cmd命令行
        :return:要远程执行的shell的str命令行
        '''

        # 注释掉
        # cmd_obj=models.CmdInfo()

        # targetfilename="mttestresult.gif"
        # cmd_obj = models.CmdInfo("sfc.sh", self.date, self.interval)

        # str_cmd = "./zyf/test/sfc.sh %s %s %s %s %s %s %s" % (
        # self.date, self.interval, self.lat_start,self.lat_finish, self.lon_start, self.lon_finish,cmd_obj.targetfile
        # )


        # cmd_obj.cmd_str =str_cmd
        # cmd_obj.interval=self.interval
        # cmd_obj.sh_file=
        # str_cmd="./sfc.sh %s %s %s %s %s"%(self.date,self.lat_start,self.lat_finish,self.lon_start,self.lon_finish,self.element,self.level,self.interval)
        return self.cmd_obj.toCmdbyStr()

    @property
    def targetFilebyStr(self):
        '''
        （通过属性的方式）获取最终保存的文件的随机文件名称
        :return:生成的随机文件名str
        '''
        return self.cmd_obj.targetfile


if __name__=='__main__':
    app.run(debug=True)