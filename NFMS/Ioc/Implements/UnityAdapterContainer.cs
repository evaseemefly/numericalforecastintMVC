using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Practices.Unity;

namespace Ioc.Implements
{
    internal sealed class UnityAdapterContainer : UnityContainer, IContainer
    {
        /// <summary>
        /// 判断类型是否被注册到Ioc容器
        /// </summary>
        /// <param name="type"></param>
        /// <returns></returns>
        public bool IsRegistered(Type type)
        {
            return UnityContainerExtensions.IsRegistered(this, type);
        }

        public void RegisterType(Type from, Type to)
        {
            UnityContainerExtensions.RegisterType(this, from, to);
        }

        public TService Resolve<TService>()
        {
            return UnityContainerExtensions.Resolve<TService>(this);
        }

        public object Resolve(Type type)
        {
            return UnityContainerExtensions.Resolve(this, type);
        }

        public TService Resolve<TService>(object overridedArguments)
        {
            var overrides = Utils.GetParameterOverrides(overridedArguments);
            return UnityContainerExtensions.Resolve<TService>(this, overrides.ToArray());
        }

        public object Resovle(Type type, object overridedArguments)
        {
            var overrides = Utils.GetParameterOverrides(overridedArguments);

            return UnityContainerExtensions.Resolve(this, type, overrides.ToArray());
        }
    }
}
