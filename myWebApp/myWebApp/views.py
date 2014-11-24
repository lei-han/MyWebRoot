from django.http.request import HttpRequest
from django.http.response import HttpResponse, Http404
from datetime import datetime, timedelta
from django.shortcuts import render_to_response

def hello(httpRequest):
    return HttpResponse("Hello..")

def now(httpRequest):
    now = datetime.now()
    html = "Now is %s" %now
    return HttpResponse(html)

def futureHours(httpRequest,hour):
    try:
        hour = int(hour)
    except ValueError:
        raise Http404()
    future = datetime.now()+timedelta(hours=hour)
    html = "%s hours later is %s." %(hour,future)
    return HttpResponse(html)

def showName(httpRequest,name):
    try:
        name = str(name)
    except ValueError:
        raise Http404()
    #return render_to_response('template1.tpl.html',locals())
    return render_to_response('test/template1.tpl.html',{'name':'abc'})

def showRequest(httpRequest):
    return render_to_response('template2.html',{'items':httpRequest.META.items()})



