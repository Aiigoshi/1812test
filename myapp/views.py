from django.shortcuts import render, redirect
from myapp.models import MyLessons, MyTable
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse


def main(request):
    b = User.objects.all()
    a = MyLessons.objects.all()
    return render(request, "index.html", {"test": a})


def auth(request):
    if request.method == "POST":
        data = request.POST
        user = authenticate(username=data["user"], password=data["password"])

        if user == None:
            request.session["userid"] = True
            return HttpResponse("Не авторизован")
        else:
            request.session["userid"] = True
            return HttpResponse(f"Авторизован {request.session['userid']}")
            # return redirect('адрес страницы') переход на др страницу
    else:
        return render(request, "auth.html")


def regi(request):
    if request.method == "POST":
        data = request.POST
        new = User.objects.create_user(username=data["user"], password=data["password"])
        new.save()
        #user = authenticate(username=data["user"], password=data["password"])
        return render(request, "index.html")
    else:
        return render(request, "reg.html")

# Create your views here.
