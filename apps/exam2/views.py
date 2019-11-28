from django.shortcuts import render, HttpResponse,redirect
from .models import *
import bcrypt
from django.contrib import messages
from django.contrib.messages import get_messages

def index(request):
    username = request.session['username']
    user = User.objects.get(username=username)

    context = {
        "fn": user.name, 
        "travels":Travel.objects.filter(users_going=user),
        "other": Travel.objects.exclude(users_going=user),
    }
    return render (request,"exam2\index.html",context)

def show(request):
    return render (request,"exam2\show.html")

def dest(request,id):
    dest = Travel.objects.get(id=id)
    username = request.session['username']
    user = User.objects.get(username=username)

    context = {
        "fn": user.name,
        "sd" : dest.sDate,
        "ed" : dest.eDate,
        "dest" : dest.destinations,
        "dFn": dest.uploadeder.name,
        "plan":dest.plan,
        "travelers":dest.users_going.exclude(id=dest.uploadeder.id),
    }
    return render(request,"exam2\dest.html",context)

def create(request):
    username = request.session['username']
    user = User.objects.get(username=username)
    
    errors = Travel.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/travels/add")
    else:
        dest = request.POST['dest']
        desc = request.POST['desc']
        sd = request.POST['sd']
        ed = request.POST['ed']

        t = Travel.objects.create(destinations=dest,plan=desc,sDate=sd,eDate=ed,uploadeder=user)

        t.users_going.add(user)
        t.save()

        return redirect("/travels")
    
def join(request):
    username = request.session['username']
    user = User.objects.get(username=username)

    if request.method =="POST":
        t_id = request.POST['travel_id']
        t = Travel.objects.get(id=t_id)

        t.users_going.add(user)
        t.save()
        print(t.users_going.all().values())
        return redirect("/travels")