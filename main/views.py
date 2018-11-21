from django.shortcuts import render


# Create your views here.

def login(request):
    return render(request,"login_form.html")


def logout(request):
    pass


def index(request):
    pass
