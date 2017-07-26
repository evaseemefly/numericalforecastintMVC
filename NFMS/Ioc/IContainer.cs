using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ioc
{

    /// <summary>
    /// 
    /// </summary>
    public interface IContainer
    {
        /// <summary>
        /// 反射成指定对象
        /// </summary>
        /// <typeparam name="TService"></typeparam>
        /// <returns></returns>
        TService Resolve<TService>();

        /// <summary>
        /// 将指定类型反射为ojbect
        /// </summary>
        /// <param name="type"></param>
        /// <returns></returns>
        object Resolve(Type type);

        /// <summary>
        /// 含参数的反射
        /// </summary>
        /// <typeparam name="TService"></typeparam>
        /// <param name="overridedArguments"></param>
        /// <returns></returns>
        TService Resolve<TService>(object overridedArguments);

        /// <summary>
        /// 含参数的反射
        /// </summary>
        /// <param name="type"></param>
        /// <param name="overridedArguments"></param>
        /// <returns></returns>
        object Resovle(Type type, object overridedArguments);

        /// <summary>
        /// 注册类型与具体实现的类型
        /// </summary>
        /// <param name="from"></param>
        /// <param name="to"></param>
        void RegisterType(Type from, Type to);

        /// <summary>
        /// 判断类型是否被注册到了Ioc容器
        /// </summary>
        /// <param name="type"></param>
        /// <returns></returns>
        bool IsRegistered(Type type);

    }
}
