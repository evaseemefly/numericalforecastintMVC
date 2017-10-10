
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
    def tocmd(self):
        '''
        根据请求数据生成shell要执行的cmd命令行
        :return:
        '''
        str_cmd = "sfc.sh %s %s %s %s %s %s %s" % (
        self.date, self.interval, self.lat_start,self.lat_finish, self.lon_start, self.lon_finish,"mttestresult.gif"
        )

        # str_cmd="./sfc.sh %s %s %s %s %s"%(self.date,self.lat_start,self.lat_finish,self.lon_start,self.lon_finish,self.element,self.level,self.interval)
        return  str_cmd
    def getFileName(self):
        name=""


if __name__=='__main__':
    app.run(debug=True)