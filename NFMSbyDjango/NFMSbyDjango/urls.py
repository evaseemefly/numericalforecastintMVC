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
# from ForecastTest import views

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
     url(r'^Forecast/Test*',views.test),
     url(r'Forecast/init',views.initModelData),
     #url(r'Forecast/actions?(?P<uid>\d+)&(?P<pwd>\s+)',views.getActions)
     url(r'Forecast/actions*',views.getActions),
    url(r'Forecast/produceImg*',views.produceImg),
]
