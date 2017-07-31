//输出的文件为.cs

using NFMS.IDAL;

namespace NFMS.DALFactory
{
public partial class DBSession
    {
	#region _actioninfoDAL 属性 
	private IDAL.IactioninfoDAL _actioninfoDAL;
	#endregion

	#region
        /// <summary>
        /// 获取actioninfoDAL的实例
        /// </summary>
        public IactioninfoDAL actioninfoDAL
        {
            get
            {
                if(_actioninfoDAL==null)
                {
                    _actioninfoDAL = AbstractFactory.CreateactioninfoDAL();
                }
                return _actioninfoDAL;
            }

            set
            {
                _actioninfoDAL = value;
            }
        }
	#endregion
	

		}
}

