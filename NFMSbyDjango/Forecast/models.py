from django.db import models

# Create your models here.

class ActionInfo(models.Model):
    # 主键
    AID=models.AutoField(primary_key=True)
    ParentID=models.IntegerField
    Name=models.CharField(max_length=64)
    DelFlag=models.BooleanField(default=True)
    ModifiedOnTime=models.DateField
    Remark=models.CharField(max_length=256)
    Url=models.CharField(max_length=256)
    AreaName=models.CharField(max_length=64)
    ActionMethodName=models.CharField(max_length=64)
    ControllerName=models.CharField(max_length=64)
    JsFunctionName=models.CharField(max_length=32)
    Sort=models.SmallIntegerField
    ActionTypeEnum=models.PositiveSmallIntegerField
    IconWidth=models.PositiveSmallIntegerField
    IconHeigh=models.PositiveSmallIntegerField
    IconCls=models.CharField(max_length=64)
    IconClassName=models.CharField(max_length=64)
    isShow=models.BooleanField(default=True)
    MethodTypeEnum=models.PositiveSmallIntegerField
    class Meta:
        db_table="actioninfo"

class UserInfo(models.Model):
    UID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=64)
    Pwd=models.CharField(max_length=64)
    DelFlag=models.BooleanField(default=False)
    SubTime=models.DateField
    ModifiedOnTime=models.DateField
    Remark=models.CharField(max_length=256)
    Sort=models.SmallIntegerField
    class Meta:
        db_table="userinfo"
