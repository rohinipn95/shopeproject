from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
# Create your views here.
def demo(request):
  obj=Place.objects.all()
  return render(request,"index1.html",{'result':obj})
"""def addition(request):
  n1=int(request.GET['num1'])
  n2=int(request.GET['num2'])
  s=n1+n2
  return render(request,"about.html",{'res':s})"""