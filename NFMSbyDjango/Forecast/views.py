from django.shortcuts import render,HttpResponsePermanentRedirect
from Forecast import models
from Forecast import Forms
from Forecast import viewmodels
# import pynq
from Forecast import viewmodels
import json
import pickle
from django.conf import settings
from django.http import JsonResponse
import os
from Forecast import utils
from NFMSbyDjango import settings
from django.http import HttpResponse
from django.core import serializers
import time
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.csrf import csrf_protect
# Create your views here.

download_url=settings.FTP_URL
target_dir=settings.TARGET_DIR

def createuser(request):
    user=User.objects.create_user('test','123@126.com','123')
    pass


def selectMapping(request):
    #注意render也是需要返回的
    # 不能直接携程render(xxx)
    return render(request,"Forecast/Index.html",{})
    # return "selectMapping"

def routeMapping():
    return "routeMapping"

def test(request):
    # 1 获取请求中的用户名及密码
    # 对于传统的?方式提交的参数直接通过request.GET.get('key')的方式获取
    name = request.GET.get('name', None)
    pwd = request.GET.get('pwd', None)
    list_nodes=getActionsList(name, pwd)

    return render(request, 'Forecast/Test.html', {'list_actions': list_nodes})

def initModelData(request):
    obj= models.UserInfo(Name="ceshi",Pwd="123")
    obj.save()
    print("写入成功")
    return render(request, 'Forecast/Test.html', {})


def request2obj(request):
    '''
    将传入的request转换为Request_Data 对象
    :param request:request
    :return:Request_Data对象
    '''
    # 若使用POST的方式就不能通过request.form.get的方式获取数据
    obj_json = json.loads(request.body.decode("utf-8"))
    obj_rectangleMeasure = obj_json.get("rectangleMeasureViewModel", None)
    obj_elemenetViewModel = obj_json.get("elemenetViewModel", None)
    obj_baseInfoViewModel = obj_json.get("baseInfoViewModel", None)
    # 下面使用GET的方式
    '''
    是dict
    '''
    # 注意dict_json是QueryDict对象
    # dict_json=request.GET
    # # [print(key) for key,value in dict_json]
    # [print(value) for key, value in dict_json]
    # q = QueryDict('a=1&a=2&a=3')
    # obj_rectangleMeasure = dict_json["rectangleMeasureViewModel"]
    # obj_elemenetViewModel = dict_json["elemenetViewModel", None]
    # obj_baseInfoViewModel = dict_json["baseInfoViewModel", None]
    request_date = obj_baseInfoViewModel.get('targetdate', None)
    '''
    使用numpy创建二维数组
    对有前台传过来的四个值进行排序
    '''
    import numpy as np
    # 创建一个都是0的2*2数组
    latlon_arr=np.zeros((2,2))
    # latlon_arr=[]
    latlon_arr[0,0]=obj_rectangleMeasure.get('startlng', None)
    latlon_arr[0,1]=obj_rectangleMeasure.get('finishlng', None)
    latlon_arr[1,0]=obj_rectangleMeasure.get('startlat', None)
    latlon_arr[1,1]=obj_rectangleMeasure.get('finishlat', None)
    latlon_arr.astype(np.float64)
    latlon_arr[0].sort()
    latlon_arr[1].sort()
    print(latlon_arr)
    # print(latlon_arr)
    # latlon_arr.sort()
    # request_lon_start = obj_rectangleMeasure.get('startlng', None)
    # request_lon_finish = obj_rectangleMeasure.get('finishlng', None)
    # request_lat_start = obj_rectangleMeasure.get('startlat', None)
    # request_lat_finish = obj_rectangleMeasure.get('finishlat', None)
    # 对二维数组进行排序
    lon_start = latlon_arr[0,0]
    lon_finish = latlon_arr[0,1]
    lat_start = latlon_arr[1,0]
    lat_finish = latlon_arr[1,1]
    request_element = obj_elemenetViewModel.get('element', None)
    request_level = obj_elemenetViewModel.get('level', None)

    request_interval = obj_elemenetViewModel.get('interval', None)

    obj = viewmodels.Request_Data_Latlng(request_date, lon_start, lon_finish, lat_start, lat_finish,request_element, request_level, request_interval)
    return obj;

def produceImg(request):

    error=None
    myresponse=viewmodels.Response_Result(99,"未处理")
    # obj_json= json.loads(request.POST)
    recv_str=""
    if request.method=='POST':
        # 获取到前台传过来的数据
        request_latlng= request2obj(request)
        '''
        2 根据obj去执行指定的shell脚本，并输入指定的参数；
        生成jpg图片
        '''
        # cmd=request_latlng.cmdbyStr
        cmd_obj=request_latlng.cmd_obj

        client=utils.ParamikoClient(download_url,"lingtj","lingtj123")
        # client.exec_cmd("cd zyf/test/")
        # 此处暂时有问题
        # 具体原因待查
        # client.exec_cmd(cmd)
        # 使用invoke_shell的方式
        recv_result= client.exec_shell(cmd_obj.toCmdbyStr())

        # 暂时不用以下方式
        # linux_main = utils.Linux("128.5.6.21","lingtj","lingtj123")
        # linux_main.connect()
        # linux_main.send("cd zyf/test/")
        # linux_main.send(cmd)
        '''
        3 执行完命令后通过ftp的方式从指定地址下载指定文件
        3.1 获取下载文件的路径
        3.2 获取下载文件的名称
        3.3 判断指定路径下是否存在指定文件
        3.4 满足条件则将该文件下载到本地的
        3.5 按照指定规则分类存储
        '''
        # 不能使用ftp的方式下载需要改为sftp的方式下载
        # ftp_client=utils.FtpClient(download_url,"lingtj","lingtj123")
        # ftp_client.download("zyf/test/",cmd_obj.targetfile,target_dir)
        # 使用sftp的方式下载
        sftpclient=utils.SFtpClient(download_url,"lingtj","lingtj123")
        recv_obj= sftpclient.sftp_download(target_dir,"zyf/test/",cmd_obj.targetfile)
        recv_dict=recv_obj.__dict__
        # 若返回的是错误代码则不替换其中的message——即不将图片路径赋给recv
        if recv_obj.code!=-1:
            # 'D:\\测试\\testcc19d5d2-b4ac-11e7-8f45-34f39a9570ee.gif'
            # 将字典中的message字段中的\\替换为/
            # recv_dict['message']=recv_dict['message'].replace("\\",'/')
            recv_dict['message'] = "../static/img/download/%s" % cmd_obj.targetfile
        recv_str=json.dumps(recv_dict,ensure_ascii=False)
        print(recv_str)
        # utils.FtpClient.download(download_url,target_dir,)
    # return HttpResponse(jstr, content_type="application/json")
    return HttpResponse(recv_str, content_type="application/json")
    # return recv_str

# @csrf_protect
def log_in(request):
    '''
    等待补充的登录操作
    :param request:
    :return:
    '''
    # 获取登录时的时间
    currenttime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

    if request.method=='POST' or request.method=="GET":
        username = request.GET.get('username')
        pwd = request.GET.get('pwd')
        remember = request.GET.get('remeberme')
        # username=request.POST.get('username')
        # pwd=request.POST.get('pwd')
        # remember=request.POST.get('remeberme')
        user=authenticate(username=username,password=pwd)
        if user is not None:
            login(request,user)
            request.session.set_expiry(60*60)

            return None


    pass

def logout(request):
    '''
    等待补充的注销操作
    :param request:
    :return:
    '''
    pass


def getDropDown(request):
    #获取aid
    aid=request.GET.get('aid')
    dict_list=getDropDownDict(aid)

    '''
            序列化：
            使用两种方式序列化
            1、json.dumps
            只能传入字典类型的参数
            2、serializers.serialize
            需要指定序列化的类型（xml，json）
            serializers支持的类型有：QuerySet以及list
            以及序列化的对象
            3、还可以看一下第三方的django-simple-serializer
            '''
    # from django.utils import simplejson
    # json_data=JsonResponse(dict_list,ensure_ascii=False)
    # json_data=serializers.serialize("json", dict_list, ensure_ascii=False)
    json_data=json.dumps(dict_list, ensure_ascii=False)
    # 注意此处若是直接返回json_data是会报错的
    return HttpResponse(json_data)
    # return JsonResponse
    # dict_dropdowninfo=list_dropdowninfo.__dict__
    # json.dumps(list_dropdowninfo, ensure_ascii=False)
    # list_dropdowninfo.__dict__
    # return render(request, 'Forecast/Test.html', {'list_actions': list_nodes})

def getDropDownDict(aid):
    '''
    根据传入的action id获取该action对应的dropdownInfo字典
    list_element,list_level,list_interval
    :param aid:action id
    :return:dict
    '''
    #根据action id 获取该action对应的dropdowninfo集合
    # aid=request.GET.get('aid')
    dropdown_dict={}
    if aid is not None:
        #找到指定id的action
        actions=models.ActionInfo.objects.filter(AID=aid)
        #找到actions对应的dropdowninfo集合
        action_temp=actions.first()
        # 判断集合是否长度>0
        # 遍历list
        # list_element=list_dropdown.
        list_dropdowninfo=[]
        dict_list={}
        [list_dropdowninfo.append(x.DId) for x in action_temp.r_dropdowninfo_actioninfo_set.all()]
        select_list=lambda index:[x for x in list_dropdowninfo if x.Stamp==index]
        list_element=select_list(0)
        # dropdown_dict["list_element"]=list_element
        '''
        如果使用utf-8或者其他的非ascii编码数据，然后用json序列器
        需要传一个ensure_ascii参数进去，否则输出的编码将会不正常
        '''
        dropdown_dict["list_element"] = serializers.serialize("json", list_element,ensure_ascii=False)
        list_level=select_list(1)
        # dropdown_dict["list_level"]=list_level
        dropdown_dict["list_level"] = serializers.serialize("json", list_level,ensure_ascii=False)
        list_interval=select_list(2)
        # dropdown_dict["list_interval"]=list_interval
        dropdown_dict["list_interval"] = serializers.serialize("json", list_interval,ensure_ascii=False)

        # 此处是测试list 类型的序列化——可行
        # data = serializers.serialize("json", list_element)
        # print(data)
        # # 此处时测试queryset 类型的序列化——可行
        # data1 = serializers.serialize("json", actions)
        # print(data1)
        # dict_list={'list_element':serializers.serialize("json",list_element),'list_interval':serializers.serialize("json",list_interval),'list_level':serializers.serialize("json",list_level)}
        # dict_list["list_element"] = serializers.serialize("json", list_element)
        # dict_list["list_interval"] = serializers.serialize("json", list_interval)
        # dict_list["list_level"] = serializers.serialize("json", list_level)
        # 注意使用pickle.dumps这种方式进行序列化序列化后的结果是二进制数据
        # ss= pickle.dumps(dict_list)
        # 此种方式序列化后，前台是否可以解析（待测试）
        # result_data = json.dumps(dict_list)

    return dropdown_dict

def getActionsList(name, pwd):
    '''
    根据用户名及密码获取该用户所拥有的菜单集合
    :param name:用户名
    :param pwd:密码
    :return:
    '''
    # 2 根据用户名及密码查询是否存在指定用户，密码是否正确
    # obj_user= models.UserInfo.objects.get(Name=name)
    users = models.UserInfo.objects.filter(Name=name)
    if users.count() == 1:
        obj_user = users.first()
        if obj_user and pwd:
            if obj_user.Pwd == pwd:
                # 2.1 密码用户名均正确
                # 根据该用户查询其拥有的权限
                # 注意此处的r是个 <QuerySet[]>
                r = obj_user.r_userinfo_action_set.all()

                # 查找该用户拥有的全部权限
                # actions= From(r).Where()
                # actions=pynq.From(r.ActionId).Where("isPass==0").select_many()
                list_actions = [x.ActionId for x in r]
                # 对actions进行排序
                # actions_sorted=sorted(actions,key=lambd a:a.Sort)
                # new_actions=list(set(actions))
                # new_actions.sort(key=actions.Url)
                # func=lambda x,y:x if y.Url==x.Url
                for a in list_actions:
                    #
                    print(a.Name)

                navbarmenu = Forms.NavbarMenu(list_actions)
                list_nodes = navbarmenu.getHomeTreeNode(list_actions, 0)
    return  list_nodes

# def getActions(request):
#     '''
#     根据用户名及pwd获取该用户的所拥有的权限
#     '''
#
#     # 2 根据用户名及密码查询是否存在指定用户，密码是否正确
#     # obj_user= models.UserInfo.objects.get(Name=name)
#     users= models.UserInfo.objects.filter(Name=name)
#     if users.count()==1:
#         obj_user=users.first()
#         if obj_user and pwd:
#             if obj_user.Pwd==pwd:
#                 # 2.1 密码用户名均正确
#                 # 根据该用户查询其拥有的权限
#                 # 注意此处的r是个 <QuerySet[]>
#                 r= obj_user.r_userinfo_action_set.all()
#                 # 查找该用户拥有的全部权限
#                 # actions= From(r).Where()
#                 # actions=pynq.From(r.ActionId).Where("isPass==0").select_many()
#                 list_actions=[x.ActionId for x in r]
#                 # 对actions进行排序
#                 #actions_sorted=sorted(actions,key=lambd a:a.Sort)
#                 #new_actions=list(set(actions))
#                 #new_actions.sort(key=actions.Url)
#                 #func=lambda x,y:x if y.Url==x.Url
#                 for a in list_actions:
#                     #
#                     print(a.Name)
#                 navbarmenu=Forms.NavbarMenu(list_actions)
#                 list_node= navbarmenu.getHomeTreeNode(list_actions,0)
#                 # list_node= getHomeTreeNode(list_actions,0)
#
#                 # print("指定用户存在")
#     return render(request, 'Forecast/Test.html', {'list_actions':list_node})

def searchInit(request):
    #初始化显示全球里面的所有内容
    data_dict,files = iterator_dir(os.path.join(settings.BASE_DIR, 'static\images\pic\Global'))
    return render(request, 'Forecast/SerachHistory.html', {'data_dict': data_dict,'image_url':data_dict[files[0]]})

# 遍历文件夹下所有文件
def iterator_dir(dirpath):
    leng = len(settings.BASE_DIR)
    dict = {} #{filename:filepath}
    files=[] #[filename]
    for dirpath, dirnames, filenames in os.walk(dirpath, topdown=True):
        root = dirpath[leng:]
        for filename in filenames:
            filepath = os.path.join(root, filename)
            dict[filename] = filepath
            files.append(filename)
    return dict,files

# @csrf.exempt
# <a href="#" class="list-group-item" data-imgurl="{{ value }}" onclick="changePic(this)">{{ key }}</a>
# request.POST[start_time]= 2017-09-01
# request.POST[end_time]=
# request.POST[area]= 西北太
# request.POST[category]= C1
# request.POST[factor]= F5
# request.POST[layer]= L7
# request.POST[moment]= M7
def searchHistory(request):
    # 暂时使用本地图片路径做测试
    root_path = os.path.join(settings.BASE_DIR, 'static\images\pic')
    html = ''
    if request.method == 'POST':
    #     print('request.POST=',request.POST)
    #     for i in request.POST:
    #        print("request.POST[%s]=" % i, request.POST[i])
        dir_path = os.path.join(root_path,
                                settings.AREA_DICT[request.POST['area']])
        data_dict, files = iterator_dir(dir_path)
        #判断查询是否有结果
        for filename,filepath in data_dict.items():
            line = "<a href='#' class='list-group-item' data-imgurl="+filepath+" onclick='changePic(this)'>"+filename+"</a>";
            html += line
        return_json={'image_url':data_dict[files[0]],'html':html}
    return JsonResponse(return_json)
