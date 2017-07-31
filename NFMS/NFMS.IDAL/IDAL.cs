//输出的文件为.cs

using NFMS.Model;

namespace NFMS.IDAL
{
   #region IactioninfoDAL   
	//actioninfo数据访问层
	/// <summary>
    /// 定义actioninfo实现类的接口
    /// 注意：
    /// 1 接口必须是是公开的，因为需要由实现类去继承（实现）
    /// 2 接口中的方法不需要添加访问修饰符（public），且没有方法体，只有方法签名
    /// </summary>
	public interface IactioninfoDAL:IBaseDAL<actioninfo>
    {
    }
	#endregion

	
}

