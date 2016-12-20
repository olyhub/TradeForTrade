from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from trade.models import Contact
import datetime

# Create your views here.
def say_hello(request):
    name = "Bootcamper"
    html = "<html><bodey><h1>Hello %s!</h1></body></html>" % name
    return HttpResponse(html)

def get_now(request):
    now = datetime.datetime.now()
    return render(request, "trades/base.html", {"current_date": now})

def inheritance_test(request):
    return render(request, "trades/home.html",
                  {"a_variable": "i've been rendered in the child template",
                   "another_variable": "me too!"})

def get_contacts(request):
    return render(request, "trades/home.html",
                  {'contact_list': Contact.objects.all()})