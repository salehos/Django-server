import reserve as reserve
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from main.models import Food


def login_(request):
    username, password = "", ""
    error = False
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                error = True
        error = True
    return render(request, "login_form.html", {
        "error": error
    })


def logout_(request):
    logout(request)
    return HttpResponseRedirect("/")


@login_required(login_url="/login")
def index(request):
    foods = Food.objects.all()
    return render(request, 'order.html', {
        "foods": foods
    })


@login_required(login_url="/login")
def reserve_food(request, food_type="lunch", food_id=None):
    try:
        food = Food.objects.get(id=food_id)
        reserve_obj = reserve()
        reserve_obj.food = food
        reserve_obj.user = request.user
        reserve_obj.reserve_date = request.datetime.now()
        reserve_obj.save()
    except Exception as exp:
        return HttpResponse("error")

# Emailesh : soleimany@outlook.com
