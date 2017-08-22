using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using NFMS.IBLL;
using NFMS.BLL;

namespace NFMS.Controllers
{
    public class HomeController : Controller
    {
        IactioninfoBLL actionBLL = new actioninfoBLL();

        public ActionResult Index()
        {
            var action_list = actionBLL.GetListBy(a => (a.isShow == true) && (a.DelFlag == false)).OrderBy(a=> a.ParentID).ToList();

            List<ViewModel.Bootstrap_TreeNode> list_treenode = new List<ViewModel.Bootstrap_TreeNode>();
            getHomeTreeNode(action_list, list_treenode, 0);
           
            //进行treeNode转换
            /*
             * 1 创建一个XXXXfunc
             * private void XXX(List<actionInfo> list,out List<ViewModel.Bootstrap_TreeNode> list_treenode,int pid)
             * 迭代方法
             * 实现效果：
             *          给一个顶级父节点（pid=0）
             *          反复迭代，最终返回list_treenode集合，所有对应的父 节点中的子节点放在children这个(List<ViewModel.Bootstrap_TreeNode>）
             * 
             */
            //return View(action_list);
            //最终返回的
            return View(list_treenode);
            //return View();
        }

        /// <summary>
        /// 添加顶级节点，若不是顶级节点，调用迭代函数添加子节点
        /// </summary>
        /// <param name="list_action"></param>
        /// <param name="list_tree"></param>
        /// <param name="pid"></param>
        private void getHomeTreeNode(List<NFMS.Model.actioninfo> list_action, List<ViewModel.Bootstrap_TreeNode> list_tree, int pid)
        {
            foreach(NFMS.Model.actioninfo item in list_action)
            {
                ViewModel.Bootstrap_TreeNode node = new ViewModel.Bootstrap_TreeNode(item.ID, item.ActionInfoName);
                if (item.ParentID == pid)
                {
                    list_tree.Add(node);
                }
                else
                {
                    addTreeNodes(item, list_tree);
                }
            }
        }

        /// <summary>
        /// 迭代添加子节点
        /// </summary>
        /// <param name="action"></param>
        /// <param name="list_tree"></param>
        private void addTreeNodes(NFMS.Model.actioninfo action, List<ViewModel.Bootstrap_TreeNode> list_tree)
        {
            ViewModel.Bootstrap_TreeNode node = new ViewModel.Bootstrap_TreeNode(action.ID, action.ActionInfoName);

            foreach (ViewModel.Bootstrap_TreeNode item in list_tree)
            {
                if (action.ParentID == item.id)
                {
                    item.children.Add(node);
                }
                else
                {
                    addTreeNodes(action, item.children);
                }
            }
        }

        public ActionResult About()
        {
            ViewBag.Message = "Your application description page.";

            return View();
        }

        public ActionResult Contact()
        {
            ViewBag.Message = "Your contact page.";

            return View();
        }
    }
}