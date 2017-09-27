from Forecast import viewmodels

# 创建一个菜单项的类
class NavbarMenu:
    '''
    屏幕左侧的手风琴导航栏
    '''
    def __init__(self,actions):
        self.actions=actions
        self.list_treeNode=None

    def getHomeTreeNode(self,actions, pid):
        '''
        根据传入的权限列表转换为tree结构的
        :param actions:传入的权限集合
        :param pid:开始遍历的父节点id
        :return:返回viewmodels.Bootstrap_TreeNode集合
        '''
        # list_actions=[]
        list_treeNodes = []
        for a in actions:
            # 若当前权限的父级id为传入的pid时
            if a.ParentID == pid:
                node = viewmodels.Bootstrap_TreeNode(a.AID, a.Name, a.Url, a.IconCls);
                list_treeNodes.append(node)
            self.__addTreeNodes(a, list_treeNodes)
        self.list_treeNode=list_treeNodes
        return list_treeNodes

    def __addTreeNodes(self,action, list_tree):
        '''
         迭代添加子节点
        :param action:一个权限对象
        :param list_tree:tree集合
        :return:
        '''
        node = viewmodels.Bootstrap_TreeNode(action.AID, action.Name, action.Url, action.IconCls)
        for item in list_tree:
            if item.id == action.ParentID:
                item.children.append(node)
            else:
                self.__addTreeNodes(action, item.children)