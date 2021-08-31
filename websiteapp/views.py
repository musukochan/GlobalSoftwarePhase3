from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _

def index(request):
    context = {}
    pagereq=str(request.path)
    return render(request,'index.html',context)


def text(request):
	context = {}
	pagereq=str(request.path)


def contact(request):
		context = {}
		pagereq=str(request.path)
		return render(request,'index.html',context)
        
def testlang(request):
        return HttpResponse(_('Welcome to language translation!'))