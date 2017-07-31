using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NFMS.IDAL;
using System.Data.Entity;
using NFMS.DALMYSQL;

namespace NFMS.DALFactory
{
    public partial class DBSession : IDBSession
    {
        /// <summary>
        /// 获取当前线程中的EF上下文对象
        /// </summary>
        public DbContext Db
        {
            //通过属性的方式，使用单例模式取得EF上下文对象
            get { return DBSessionFactory.GetDBContext(); }
        }

        public bool SaveChanges()
        {
            try
            {
                int index = Db.SaveChanges();
                //6月12日修改
                /*
                由于在修改部门及修改群组时，
                若没有对之前的部门进行重新修改，而只对部门或群组中的一个进行修改
                保存时改变的Index会为0
                此处修改为若Index>=0都算修改成功
                （只要没有抛出异常）
                */
                return index >= 0;
            }
            //此处抛出异常使用DB.Save时的异常类
            //DbEntityValidationException
            catch (Exception dbEx)
            {

                return false;
            }
        }
    }
}
