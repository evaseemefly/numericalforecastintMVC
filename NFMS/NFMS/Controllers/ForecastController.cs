using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace NFMS.Controllers
{
    public class ForecastController : Controller
    {
        // GET: Forecast
        public ActionResult Index()
        {
            return View();
        }

        public ActionResult SelectMapping()
        {
            return View();
        }

        public ViewResult jsdkfjksdfj()
        {
            return View("SelectMapping");
        }

        public ViewResult RouteMapping()
        {
            return View();
        }
    }
}