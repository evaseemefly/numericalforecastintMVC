from django.shortcuts import render,HttpResponsePermanentRedirect

# Create your views here.

def selectMapping(request):
    #注意render也是需要返回的
    # 不能直接携程render(xxx)
    return render(request,"Forecast/Index.html",{})
    # return "selectMapping"

def routeMapping():
    return "routeMapping"

def test(request):
    return render(request,'Forecast/Test.html',{})