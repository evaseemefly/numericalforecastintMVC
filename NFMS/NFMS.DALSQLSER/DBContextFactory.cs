using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Runtime.Remoting.Messaging;
using System.Text;
using System.Threading.Tasks;

namespace NFMS.DALMYSQL
{
    
        public class DBContextFactory
        {
            /// <summary>
            /// 创建线程中唯一的EF 上下文 对象
            /// </summary>
            /// <returns></returns>
            public static DbContext GetDBContext()
            {
                //1 获取当前线程中的EF上下文对象
                //注意：
                //.Name=DBContextFactory，即当前类的名字
                //根据名称读取线程槽中的对象            
                DbContext dbContext = CallContext.GetData(typeof(DBContextFactory).Name) as DbContext;

                //判断当前线程中 是否包含EF上下文对象，若不存在则创建
                if (dbContext == null)
                {
                    //2.1 将实体层的数据上下文对象赋给EF上下文对象
                    dbContext = new NFMS.Model.NFMSEntities();
                    //2.2 将已经获取到的EF上下文对象存储到当前线程槽中
                    CallContext.SetData(typeof(DBContextFactory).Name, dbContext);
                }
                //dbContext.Configuration.AutoDetectChangesEnabled = false;
                //3 返回数据上下文对象
                return dbContext;
            }
        }
    }

