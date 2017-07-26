using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(NFMS.Startup))]
namespace NFMS
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
