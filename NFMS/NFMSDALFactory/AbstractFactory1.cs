//输出的文件为.cs

using NFMS.Model;
using NFMS.IDAL;

namespace NFMS.DALFactory
{

    public partial class AbstractFactory
    {     
		 
		#region 创建actioninfo的实例
        /// <summary>
        /// 创建actioninfo的实例
        /// </summary>
        /// <returns></returns>
        public static IactioninfoDAL CreateactioninfoDAL()
        {
            //获取类的全名称：命名空间+类名
            string fullClassName = NameSpace + ".actioninfoDAL";
            return CreateInstance(fullClassName) as IactioninfoDAL;
        }
		#endregion
	    }
	
}

