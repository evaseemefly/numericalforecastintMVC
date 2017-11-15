"""NFMSbyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
# from NFMS import views
from Forecast import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import staticfiles# from ForecastTest import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^nfms/',views),
    # url(r'^Forecast',include("Forecast.urls"))
    # url(r'^Forecast',NFMSbyDjango.Forecast.views.selectMapping)
    # url(r'^Forecast/selectMapping',views.selectMapping),
    # url(r'^Forecast/Test',views.test),
    # url(r'Forecast/init',views.initModelData),
    # url(r'Forecast/actions*',views.getActions),
    # url(r'^Forecast/selectMapping',views.selectMapping),
    # 所有的Forecast开头的url的匹配规则统一放在Forecast中的urls.py中
    url(r'^Forecast/', include('Forecast.urls')),

    # url(r'login',views.log_in),
    # url(r'create_permission*',views.test_login),
    url(r'test*',views.test_login),
    url(r'create_group',views.create_group),
    url(r'create_permission',views.create_permission),
    url(r'guest_login*',views.guest_login),
    # url(r'test*',views.test_login1),
    # url(r'^Forecast/',include("Forecast.urls"))
    # url(r'^download/(?P<path>.*)', 'django.views.static.serve', {'document_root':'/download'}),
    # url(r'^download/(?P<path>.*)','django.views.static.serve', {'document_root':'/download'}),
]

#����ͼƬʱ��Ҫʹ�õ�
# urlpatterns += staticfiles_urlpatterns()
# print(urlpatterns)
