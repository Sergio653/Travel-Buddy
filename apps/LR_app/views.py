from django.shortcuts import render, HttpResponse,redirect
from .models import *
from apps.exam2.models import *
import bcrypt
from django.contrib import messages
from django.contrib.messages import get_messages

def index(request):
    return render(request,"LR_app/index.html")


def create(request):
    password=''
    Nuser = {
        'name' : request.POST["name"],
        'username' : request.POST["username"],
        'pw' : request.POST["pw"],
        'pwc' : request.POST["pw_confirmed"],
    }
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        password = bcrypt.hashpw(Nuser['pw'].encode(), bcrypt.gensalt())
        user = User.objects.create(name=Nuser['name'],username=Nuser['username'],pw_h=password.decode())
        request.session['username']=user.username
    return redirect('/travels')

def login(request):
    user = {
        "username" : request.POST['username'],
        "pw" : request.POST['pw']
    }
    try:
        user_account = User.objects.get(username=user['username'])
        print(user_account.pw_h)
        if bcrypt.checkpw(request.POST['pw'].encode(), user_account.pw_h.encode()):
            request.session['username'] = user['username']
            return redirect('/travels')
        else:
            messages.add_message(request,messages.ERROR,"Invalid Email/password")
            return redirect("/")
    except:
        messages.add_message(request,messages.ERROR,"Invalid Email/password")
        return redirect("/")
def logout(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect("/")