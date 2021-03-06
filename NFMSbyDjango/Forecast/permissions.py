from django.shortcuts import render
from Forecast import models
from django.db.models import Q
from django.core.urlresolvers import resolve   #此方法可以将url地址转换成url的name

from django.contrib.auth.models import User,Group,Permission

def perm_check(request, *args, **kwargs):
    # 1 获取请求类型以及url
    # 使用resolve无法获取到'/Forecast/guest_login',暂时注释掉，不使用这种方式
    # url_obj = resolve(request.path)
    # 对'/Forecast/guest_login'根据/进行切分
    pathes=request.path.split('/')
    # url_name = request.path
    # 获取pathes的最后一个值
    # url_name对应的就是auth_permission中的codename
    url_name=pathes[-1]
    #url_name = url_obj.url_name
    dict_method={
        'GET':1,
        'POST':2
    }
    perm_name = url_name
    # 2 根据url与post或get请求查找permission对象找到唯一的权限
    #权限必须和urlname配合使得
    if url_name:
        #获取请求方法，和请求参数
        url_method, url_args = request.method, request.GET
        url_args_list = []
        #将各个参数的值用逗号隔开组成字符串，因为数据库中是这样存的
        for i in url_args:
            url_args_list.append(str(url_args[i]))
        url_args_list = ','.join(url_args_list)
        # 不使用以下方式
        #操作数据库
        #get_perm = models.Permission.objects.filter(Q(url=url_name) and Q(per_method=dict_method[url_method]) and Q(argument_list=url_args_list))
        # get_perm = models.Permission.objects.filter(url=url_name,per_method=dict_method[url_method])
        # if get_perm.count()>0:
        #     for i in get_perm:
        #         perm_name = i.name
        #         perm_str =perm_name
        #         # perm_str = 'Forecast.%s' % perm_name
        #         id_user=request.user.id
        #         is_permission=User.objects.get(id=id_user).has_perm(perm_str)
        #         # 注意此处存在问题，由于在后台为user重新分配了群组，群组重新分配了permission，所以在request中的user中的该群组及group中并未有该权限（我的猜测）
        #         if request.user.has_perm(perm_str):
        #             print('====》权限已匹配')
        #             return True
        #     else:
        #         print('---->权限没有匹配')
        #         return False
        # else:
        #     return False

        # 直接判断当前登录用户是否拥有访问此页面的权限
        # 注意若用户未登录，此处的id为none，需要加入判断
        id_user = request.user.id
        if id_user is None:
            return False
        # 注意此处若未拥有该权限会抛出异常
        # perm_str =perm_name
        # get_perm = models.Permission.objects.filter(
        #     Q(url=url_name) and Q(per_method=dict_method[url_method]) and Q(argument_list=url_args_list))
        # 2.1 查询
        # 使用Q对象的方式查询，对于多参数较为遍历，不使用拼接参数的方式
        # 注意不要使用and和or关键字，不知为何and和or实际效果是反的，使用&和|实现或与操作
        permission_temp = models.Permission.objects.filter(
             Q(url=url_name) & Q(per_method=dict_method[url_method])).first()
        if permission_temp is None:
            return False
        # 3 根据permission对象中的url判断当前用户是否拥有该请求
        perm_str = 'Forecast.%s' % permission_temp.url
        # 在创建auth_permission表中的数据时，会为codename自动添加app的名字
        is_permission= User.objects.get(id=id_user).has_perm(perm_str)
        if is_permission:
            print("用户%s拥有：%s权限" % (id_user, url_name))
            return True
        else:
            print("用户%s未有：%s权限" % (id_user, url_name))
            return False
    return False

def check_permission(fun):    #定义一个装饰器，在views中应用
    def wapper(request, *args, **kwargs):
        if perm_check(request, *args, **kwargs):  #调用上面的权限验证方法
            return fun(request, *args, **kwargs)
        return render(request, '403.html', locals())
    return wapper