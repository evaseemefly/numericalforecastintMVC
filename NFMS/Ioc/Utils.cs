using Microsoft.Practices.Unity;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;

namespace Ioc
{
    public class Utils
    {
        public static IEnumerable<ParameterOverride> GetParameterOverrides(object overridedArguments)
        {
            //创建unity需要的参数集合
            List<ParameterOverride> overrides = new List<ParameterOverride>();

            //获取参数的类型
            Type argumentsType = overridedArguments.GetType();
            //获取公共成员及实例成员
            argumentsType.GetProperties(BindingFlags.Public | BindingFlags.Instance)
                .ToList()
                .ForEach(property =>
                {
                    //获取指定属性的值
                    var propertyValue = property.GetValue(overridedArguments, null);
                    //获取成员的名称
                    var propertyName = property.Name;
                    //将每一个属性的名称及对应的值加入到ParameterOverride中
                    overrides.Add(new ParameterOverride(propertyName, propertyValue));
                });

            return overrides;
        }
    }
}
