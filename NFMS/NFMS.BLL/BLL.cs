//输出的文件为.cs

using NFMS.IBLL;
using NFMS.Model;

namespace NFMS.BLL
{
	   #region	actioninfoBLL
    public partial class actioninfoBLL : BaseBLL<actioninfo>, IactioninfoBLL
    {	

		/// <summary>
        /// 为当前的DAL对象赋值，赋值为actioninfoDAL
        /// </summary>
        public override void SetCurrentDAL()
        {
            base.CurrentDAL = base.CurrentDBSession.actioninfoDAL;
        }
    }
	#endregion
	}

