from django.db import models
import uuid

# Create your models here.

class ActionInfo(models.Model):
    # 主键
    AID=models.AutoField(primary_key=True)
    ParentID=models.IntegerField(default=0)
    Name=models.CharField(max_length=64)
    DelFlag=models.BooleanField(default=True)
    ModifiedOnTime=models.DateField()
    Remark=models.CharField(max_length=256)
    Url=models.CharField(max_length=256)
    AreaName=models.CharField(max_length=64)
    ActionMethodName=models.CharField(max_length=64)
    ControllerName=models.CharField(max_length=64)
    JsFunctionName=models.CharField(max_length=32)
    Sort=models.SmallIntegerField(default=0)
    ActionTypeEnum=models.PositiveSmallIntegerField(default=0)
    IconWidth=models.PositiveSmallIntegerField(null=True)
    IconHeigh=models.PositiveSmallIntegerField(null=True)
    IconCls=models.CharField(max_length=64)
    IconClassName=models.CharField(max_length=64)
    isShow=models.BooleanField(default=True)
    MethodTypeEnum=models.PositiveSmallIntegerField(default=0)
    class Meta:
        db_table="actioninfo"

class DropDownInfo(models.Model):
    '''
    级联菜单表
    '''
    # 主键
    DId=models.AutoField(primary_key=True)
    # 下拉框text显示内容
    DText=models.CharField(max_length=64)
    # key
    Dkey=models.CharField(max_length=64)
    # 父级id
    PDId=models.IntegerField(default=0)
    # 标记暂时未想好用处
    Stamp=models.IntegerField(default=0)
    class Meta:
        db_table="dropdowninfo"

    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        d = {}
        for attr in fields:
            import datetime
            if isinstance(getattr(self, attr), datetime.datetime):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(getattr(self, attr), datetime.date):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d')
            else:
                d[attr] = getattr(self, attr)

        import json
        return json.dumps(d)

class TestInfo(models.Model):
    SubTime=models.DateTimeField(auto_now=True, blank=True)
    TestTime = models.DateTimeField(auto_now=True, blank=True)
    isDel=models.BooleanField(default=True)
    class Meta:
        db_table="testinfo"

class UserInfo(models.Model):
    UID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=64)
    Pwd=models.CharField(max_length=64)
    DelFlag=models.BooleanField(default=False)
    SubTime=models.DateTimeField(auto_now_add=True)
    ModifiedOnTime=models.DateTimeField(auto_now=True, blank=True)
    TestModifiedOnTime=models.DateTimeField(auto_now=True, blank=True)
    Remark=models.CharField(max_length=256)
    Sort=models.SmallIntegerField(default=0)
    class Meta:
        db_table="userinfo"

class R_UserInfo_Action(models.Model):
    RID=models.AutoField(primary_key=True)
    UserId=models.ForeignKey(UserInfo)
    # UserId=models.IntegerField
    ActionId=models.ForeignKey(ActionInfo)
    # ActionId=models.IntegerField
    isPass=models.BooleanField(default=False)
    class Meta:
        db_table="r_userinfo_action"

class R_DropDownInfo_ActionInfo(models.Model):
    DId=models.ForeignKey(DropDownInfo)
    AId=models.ForeignKey(ActionInfo)
    class Meta:
        db_table="r_drowdowninfo_action"

class CmdInfo:
    '''
    实现生成linux端存储的随机文件名的功能
    '''
    def __init__(self,sh,date,interval,lat_start,lat_finish,lon_start,lon_finish):
        '''

        :param sh:
        :param date:
        :param interval:
        :param lat_start:
        :param lat_finish:
        :param lon_start:
        :param lon_finish:
        '''
        # self.cmd_str=cmd
        self.guid = uuid.uuid1()
        self.targetfile = self.__targetfile_str
        self.sh_file=sh
        self.target_date=date
        self.interval=interval
        self.date = date
        self.lon_start = lon_start
        self.lon_finish = lon_finish
        self.lat_start = lat_start
        self.lat_finish = lat_finish
        # self.latlng=latlng
        # self.targetfile=file
        # self.guid=guid
    # __slots__ = ('cmd_str','sh_file','target_date','interval','latlng','targetfile','guid')

    # def __init__(self):
    #     '''
    #     无参的构造函数用来生成guid
    #     '''
    #     self.guid=uuid.uuid1()
    #     self.targetfile=self.targetfile()

    def toCmdbyStr(self):
        '''
        生成cmd字符串
        :return:
        '''
        str_cmd = "./zyf/test/sfc.sh %s %s %s %s %s %s %s" % (
            self.date, self.interval, self.lat_start, self.lat_finish, self.lon_start, self.lon_finish,
            self.targetfile
        )
        return str_cmd
        # pass

    @property
    def __targetfile_str(self):
        '''
        获取生成的文件名称
        每实例化一次本类，才生成一个guid作为targetfile的一个参考变量
        :return:
        '''
        self.targetfile="{}{}.gif".format("test",self.guid)
        return self.targetfile

class BaseResultInfo:
    '''
    基础的返回信息父类
    '''
    def __init__(self,code=None,result=None,message=None):
        self.code=code
        self.result=result
        self.message=message

class RecvResultInfo(BaseResultInfo):
    '''

    '''
    def __init__(self,code=None,result=None,message=None):
        # self.code=code
        # self.result=result
        # self.message=message
        super().__init__(code,result,message)

class ReturnResultInfo(BaseResultInfo):
    '''
    由后台返回给前台显示的信息类（多了一个title属性）
    '''
    def __init__(self,code=None,result=None,message=None,title=None):
        # super(ReturnResultInfo, self).__init__()
        # super(ReturnResultInfo, self).__init__()
        super().__init__(code,result,message)
        self.title=title

class Permission(models.Model):
    name=models.CharField("权限名称",max_length=64)
    url=models.CharField("URL名称",max_length=255)
    chioces = ((1, 'GET'), (2, 'POST'))
    per_method = models.SmallIntegerField('请求方法', choices=chioces, default=1)
    argument_list = models.CharField('参数列表', max_length=255, help_text='多个参数之间用英文半角逗号隔开', blank=True, null=True)
    describe = models.CharField('描述', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "permission"
        verbose_name = '权限表'
        verbose_name_plural = verbose_name
        # 权限信息，这里定义的权限的名字，后面是描述信息，描述信息是在django admin中显示权限用的
        permissions = (
            ('views_action_list', '查看权限信息表'),
            ('views_action_info', '查看权限详细信息'),
        )