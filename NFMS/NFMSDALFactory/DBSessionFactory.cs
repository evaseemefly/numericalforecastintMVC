﻿using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Runtime.Remoting.Messaging;
using System.Text;
using System.Threading.Tasks;

namespace NFMS.DALFactory
{
    public class DBSessionFactory
    {
        /// <summary>
        /// 创建线程内唯一的DBSession
        /// </summary>
        /// <returns></returns>
        public static IDAL.IDBSession CreateDbSession()
        {
            //1 获取当前线程中的EF上下文对象
            IDAL.IDBSession DbSession = CallContext.GetData(typeof(DBSessionFactory).Name) as IDAL.IDBSession;

            //判断当前线程中 是否包含EF上下文对象，若不存在则创建
            if (DbSession == null)
            {
                DbSession = new DBSession();

                CallContext.SetData(typeof(DBSessionFactory).Name, DbSession);

            }

            return DbSession;
        }
    }
}
