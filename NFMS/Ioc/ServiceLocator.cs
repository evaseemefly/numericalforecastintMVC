using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Practices.Unity;
using Microsoft.Practices.Unity.Configuration;
using System.Configuration;


namespace Ioc
{
    /// <summary>
    /// 服务定位器
    /// 通过服务定位器实现根据传入的Type
    /// 通过Untity映射为指定类型的操作
    /// </summary>
    public class ServiceLocator : IContainer
    {
        private readonly IContainer container;

        private static readonly ServiceLocator instance = new ServiceLocator();

        /// <summary>
        /// 私有的构造函数
        /// </summary>
        private ServiceLocator()
        {
            Action<IUnityContainer> unityAction = container =>
            {
                //1 获取配置文件中的unity段
                UnityConfigurationSection section = (UnityConfigurationSection)ConfigurationManager.GetSection("unity");

                if (section == null)
                {
                    throw new ArgumentException("请配置unity节点");
                }

                if(section != null)
                {
                    section.Configure(container);
                }

               

            };

            container = new Implements.UnityAdapterContainer();
            unityAction((IUnityContainer)container);
        }

        public bool IsRegistered(Type type)
        {
            throw new NotImplementedException();
        }

        public void RegisterType(Type from, Type to)
        {
            throw new NotImplementedException();
        }

        public TService Resolve<TService>()
        {
            throw new NotImplementedException();
        }

        public object Resolve(Type type)
        {
            throw new NotImplementedException();
        }

        public TService Resolve<TService>(object overridedArguments)
        {
            throw new NotImplementedException();
        }

        public object Resovle(Type type, object overridedArguments)
        {
            throw new NotImplementedException();
        }
    }
}
