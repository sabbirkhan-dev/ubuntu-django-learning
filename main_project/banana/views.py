from django.shortcuts import render

from datetime import datetime

# Create your views here.
# from django.http import HttpResponse

def contract(request):
    return render(request, "banana/index.html", {'name': 'Sabbir Khan'})

def time(request):
    d = datetime.now()
    return render(request, "banana/date_time.html", {'dt': d})