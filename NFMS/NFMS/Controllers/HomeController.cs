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
            actionBLL.GetListBy(a=>(a.isShow==true)&&(a.DelFlag==false))
            return View();
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