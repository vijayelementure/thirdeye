from django.shortcuts import render


def login(request):
    return render(request, "ourauthsys/login.html")


def reset(request):
    return render(request, "ourauthsys/reset.html")
