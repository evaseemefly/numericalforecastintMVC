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
            var action_list = actionBLL.GetListBy(a => (a.isShow == true) && (a.DelFlag == false)).ToList();

            List<ViewModel.Bootstrap_TreeNode> list_treenode = new List<ViewModel.Bootstrap_TreeNode>();
            TreeInfo(list_treenode);
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

        private void TreeInfo(List<ViewModel.Bootstrap_TreeNode> list_tree)
        {
            list_tree[0].id = 0;
            list_tree[0].text = "trreeee";
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