from django.shortcuts import render
from . import botcontrol as bc
#from .silniki.botcontrol import botstop, botforward, botreverse, botleft, botright
from django.views import View
from control.forms import LoginForm
from django.urls import reverse
from django.http import HttpResponse,  HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


class StopView(View):
    
    def get(self, request):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect('login')
        bc.botstop()
        return render(request, 'controllinks.html')


class ForwardView(View):
    
    def get(self, request):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect('login')
        bc.botforward(500)
        return render(request, 'controllinks.html')


class ReverseView(View):
    
    def get(self, request):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect('login')
        bc.botreverse(1000)
        return render(request, 'controllinks.html')


class LeftView(View):
    
    def get(self, request):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect('login')
        bc.botleft(1000)
        return render(request, 'controllinks.html')


class RightView(View):
   
    def get(self, request):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect('login')
        bc.botright(500)
        return render(request, 'controllinks.html')


class LoginView(View):
    def get(self, request):
        form=LoginForm()
        return render(request, "login.html", {"form":form})
    def post(self, request):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user= authenticate(username=username,password=password )
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("stop")
            else:
                return HttpResponse("nie udalo sie")
            
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponse("wylogowano")