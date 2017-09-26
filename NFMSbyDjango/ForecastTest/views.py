from django.shortcuts import render, HttpResponsePermanentRedirect
from ForecastTest import models
# import pynq
# from ForecastTest import viewmodels


# Create your views here.

def selectMapping(request):
    # 注意render也是需要返回的
    # 不能直接携程render(xxx)
    return render(request, "Forecast/Index.html", {})
    # return "selectMapping"


def routeMapping():
    return "routeMapping"


def test(request):
    return render(request, 'Forecast/Test.html', {})


def initModelData(request):
    obj = models.UserInfo(Name="ceshi", Pwd="123")
    obj.save()
    print("写入成功")
    return render(request, 'Forecast/Test.html', {})


def getActions(request, name, pwd):
    '''
    根据用户名及pwd获取该用户的所拥有的权限
    '''
    # 1 获取请求中的用户名及密码
    # name= request.GET.get('name',None)
    # pwd=request.GET.get('pwd',None)
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
                getHomeTreeNode(list_actions, 0)
                # print("指定用户存在")


def getHomeTreeNode(actions, pid):
    '''
    根据传入的权限列表转换为tree结构的
    '''
    list_actions = []
    list_treeNodes = []
    for a in actions:
        # 若当前权限的父级id为传入的pid时
        if a.ParentID == pid:
            list_actions.append(a)
        addTreeNodes(a, list_treeNodes)
    return list_treeNodes


def addTreeNodes(action, list_tree):
    '''
    迭代添加子节点
    '''
    node = viewmodels.Bootstrap_TreeNode()
    for item in list_tree:
        if item.id == action.ParentID:
            item.children.append(node)
        else:
            addTreeNodes(action, item.children)

