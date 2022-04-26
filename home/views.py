from datetime import datetime
import imp
from django.shortcuts import render
from django.http  import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home/home.html' , {'today':datetime.today()})