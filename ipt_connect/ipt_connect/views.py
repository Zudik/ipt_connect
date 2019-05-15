from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):

    text = """<h1>IPT Connect</h1>

              <a href="http://connect.iptnet.info/IPTdev">Results of IPT dev</a>"""
    return HttpResponse(text)

def custom_404(request):
    return render_to_response('404.html', RequestContext(request))

def custom_500(request):
    return render_to_response('500.html', RequestContext(request))