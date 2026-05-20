from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

def about(request):
    return render(request, "orange/index.html", {'about': 'About for Banana'}) 

def about_me(request):
    name = 'Sabbir Khan'
    district = 'Gopalganj'
    company = 'Wyze Tech Ltd'
    position = 'Officer'
    data_con = {'nm': name, 'vill': 'Bhulbaria','dis': district, 'com': company, 'pos': position,}
    return render(request, "orange/about_me.html", {'data': data_con})