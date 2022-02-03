from django import http
from django.shortcuts import render
import random
from .forms import Urlform
from .models import Urlmodel
from django.http import HttpResponseRedirect
# Create your views here.

# db_items = URLModel.objects.filter(shortened_url=short)
db_all = Urlmodel.objects.all()

def generate_rand_str():
    n = 5
    random_s = ""
    s = '0'
    for i in range(n):
        k= random.randrange(0,3)
        if k==0:
            l = random.randrange(0,10)
            s = chr(ord('0')+l)
        elif k==1:
            l = random.randrange(0,26)
            s = chr(ord('a')+l)
        elif k==2:
            l = random.randrange(0,26)
            s = chr(ord('A')+l)
        random_s+=s
    return random_s

website_url = "http://127.0.0.1:8000/"

def home(request):
    form = Urlform()
    if request.method == 'POST':
        form = Urlform(request.POST)
        shortened_url = generate_rand_str()
        link = Urlmodel(original_url=form.data['form_url_field'],shortened_url=shortened_url)
        link.save()
        # print(generate_rand_str())
        # print(link.original_url)
        return render(request,"url_s/index.html",{
            "website_url" : website_url,
        "form":form,
        "shortened_url" : shortened_url,
    })    
    elif request.method == 'GET':
        return render(request,"url_s/index.html",{
        "form":form,
    })

def short(request,short):
    db_items = Urlmodel.objects.filter(shortened_url=short)
    return HttpResponseRedirect(db_items[0].original_url)