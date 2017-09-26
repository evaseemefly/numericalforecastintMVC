from django.shortcuts import render,HttpResponsePermanentRedirect
from Forecast import models
# import pynq
from Forecast import viewmodels

# Create your views here.

def selectMapping(request):
    #注意render也是需要返回的
    # 不能直接携程render(xxx)
    return render(request,"Forecast/Index.html",{})
    # return "selectMapping"

def routeMapping():
    return "routeMapping"

def test(request):
    return render(request,'Forecast/Test.html',{})

def initModelData(request):
    obj= models.UserInfo(Name="ceshi",Pwd="123")
    obj.save()
    print("写入成功")
    return render(request, 'Forecast/Test.html', {})


# noinspection PyInterpreter
def getActions(request):
    # 1 获取请求中的用户名及密码
    name= request.GET.get('name',None)
    pwd=request.GET.get('pwd',None)
    # 2 根据用户名及密码查询是否存在指定用户，密码是否正确
    # obj_user= models.UserInfo.objects.get(Name=name)
    users= models.UserInfo.objects.filter(Name=name)
    # noinspection PyInterpreter
    if users.count()==1:
        obj_user=users.first()
        if obj_user and pwd:
            if obj_user.Pwd==pwd:
                # 2.1 密码用户名均正确
                # 根据该用户查询其拥有的权限
                # 注意此处的r是个 <QuerySet[]>
                r= obj_user.r_userinfo_action_set.all()
                # 查找该用户拥有的全部权限
                # actions= From(r).Where()
                # actions=pynq.From(r.ActionId).Where("isPass==0").select_many()
                actions=[x.ActionId for x in r]
                for a in actions:
                    print(a.Name)
                # print("指定用户存在")