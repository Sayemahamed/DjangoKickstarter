from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from allauth.account.views import LoginView
print( LoginView)


# Create your views here.
def index(request) -> HttpResponse:
    return render(request=request, template_name="index.html")


@login_required
def profile(request) -> HttpResponse:
    return render(request=request, template_name="account/profile.html")
