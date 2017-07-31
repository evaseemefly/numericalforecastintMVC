//输出的文件为.cs

using NFMS.Model;

namespace NFMS.IDAL
{
  	
	 public partial  interface IDBSession
    {
	  
	  #region IactioninfoDAL
      IDAL.IactioninfoDAL actioninfoDAL { get; set; }
	  #endregion

	  }




}

