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

    def __init__(self):
        '''
        无参的构造函数用来生成guid
        '''
        self.guid=uuid.uuid1()
        self.targetfile=self.targetfile()

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
    def targetfile(self):
        '''
        获取生成的文件名称
        每实例化一次本类，才生成一个guid作为targetfile的一个参考变量
        :return:
        '''
        self.targetfile="{}{}.gif".format("test",self.guid)
        return self.targetfile