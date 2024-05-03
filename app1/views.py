from django.shortcuts import render
from django.views import View

# Create your views here.
from .models import Mode
class Link(View):
    def get(self,request):
        return render(request,'base.html',{'baza':Mode.objects.all()})