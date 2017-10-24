from django.shortcuts import render,HttpResponsePermanentRedirect
from Forecast import models
from Forecast import Forms
from Forecast import viewmodels
# import pynq
from Forecast import viewmodels
import json
from Forecast import utils
from NFMSbyDjango import settings
from django.http import HttpResponse

# Create your views here.

download_url=settings.FTP_URL
target_dir=settings.TARGET_DIR

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
    list_nodes=getActions(name,pwd)

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
    request_lon_start = obj_rectangleMeasure.get('startlng', None)
    request_lon_finish = obj_rectangleMeasure.get('finishlng', None)
    request_lat_start = obj_rectangleMeasure.get('startlat', None)
    request_lat_finish = obj_rectangleMeasure.get('finishlat', None)
    request_element = obj_elemenetViewModel.get('element', None)
    request_level = obj_elemenetViewModel.get('level', None)

    request_interval = obj_elemenetViewModel.get('interval', None)

    # request_date = request.form.get('date', None)
    # request_lon_start = request.form.get('lon_start', None)
    # request_lon_finish = request.form.get('lon_finish', None)
    # request_lat_start = request.form.get('lat_start', None)
    # request_lat_finish = request.form.get('lat_finish', None)
    # request_element = request.form.get('element', None)
    # request_level = request.form.get('level', None)
    # request_interval = request.form.get('interval', None)
    obj = viewmodels.Request_Data_Latlng(request_date, request_lon_start, request_lon_finish, request_lat_start, request_lat_finish,request_element, request_level, request_interval)
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

def login(request):
    '''
    等待补充的登录操作
    :param request:
    :return:
    '''
    pass

def logout(request):
    '''
    等待补充的注销操作
    :param request:
    :return:
    '''
    pass

def getActions(name,pwd):
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
