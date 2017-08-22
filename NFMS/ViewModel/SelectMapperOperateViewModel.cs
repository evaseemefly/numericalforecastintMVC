using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NFMS.ViewModel
{
    public class SelectMapperOperateViewModel
    {
        /// <summary>
        /// 时效
        /// </summary>
        public int  timelimit{get;set;}

        public DateTime Date { get; set; }

        /// <summary>
        /// 要素
        /// </summary>
        public string element { get; set; }

        /// <summary>
        /// 等级
        /// </summary>
        public int level { get; set; }

        public float lon_start { get; set; }

        public float lon_finish { get; set; }

        public float lat_start { get; set; }

        public float lat_finish { get; set; }

        public int area { get; set; }
    }
}
