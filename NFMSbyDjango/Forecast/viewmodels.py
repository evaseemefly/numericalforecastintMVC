
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
    def __init__(self, id,text,url,iconClass,children):
        self.id=id
        self.text=text
        self.url=url
        self.iconClass=iconClass
        self.childer=[]
        #return super().__init__(**kwargs)