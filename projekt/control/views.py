from django.shortcuts import render
from . import botcontrol as bc
#from .silniki.botcontrol import botstop, botforward, botreverse, botleft, botright
from django.views import View
# Create your views here.

class StopView(View):
    def get(self, request):
        bc.botstop()
        return render(request, 'controllinks.html')
    
class ForwardView(View):
    def get(self, request):
        bc.botforward(500)
        return render(request, 'controllinks.html')

class ReverseView(View):
    def get(self, request):
        bc.botreverse(1000)
        return render(request, 'controllinks.html')
    
class LeftView(View):
    def get(self, request):
        bc.botleft(1000)
        return render(request, 'controllinks.html')
    
class RightView(View):
    def get(self, request):
        bc.botright(500)
        return render(request, 'controllinks.html')
    