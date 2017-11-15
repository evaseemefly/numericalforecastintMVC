from django.conf.urls import url,include
from Forecast import views
# urlpatterns = [
#    url(r'^')
#
# ]
from django.conf.urls import include, url

# urlpatterns = patterns('',
#                        url(r'^$', views.show, name='index'),
#                        url(r'^static/(?P<path>.*)', 'django.views.static.serve',
#                            {'document_root': '/home/anna/Documents/django_py/showImg/static'}),
#                        )

urlpatterns = [
    # url(r'^download/(?P<path>.*)', 'django.views.static.serve', {'document_root':'/download'}),
    url(r'Test*',views.test),
    url(r'init',views.initModelData),
    #url(r'Forecast/actions?(?P<uid>\d+)&(?P<pwd>\s+)',views.getActions)
    url(r'actions*', views.getActionsList),
    url(r'searchInit',views.searchInit),
    url(r'searchHistory',views.searchHistory),
    url(r'produceImg*',views.produceImg),
    # url(r'Forecast/getDropDownList*',views.getDropDownList)
    url(r'getDropDown*',views.getDropDown),
    url(r'create_user',views.create_user),
    url(r'guest_login',views.guest_login),

]