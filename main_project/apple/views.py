from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import buildingAdd
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def home(request):
    return render(request, "apple/index.html")

def building_form(request):
    if request.method == "POST":
        frm = buildingAdd(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect("/apple/")
    else:
        frm = buildingAdd()
    return render(request, "apple/building.html", {"form": frm})

# Login
def login_form(request):
    if request.method == 'POST':
        frm = AuthenticationForm(request=request, data = request.POST)

        if frm.is_valid():
            usern = frm.cleaned_data['username']
            userp = frm.cleaned_data['password']

            user = authenticate(
                request,
                username=usern,
                password=userp
            )
            if user is not None:
                login(request, user)
                return redirect('success')
            
    else:
        frm = AuthenticationForm()

    return render(request, "apple/login.html", {"form": frm})

# successfully login
def login_success(request):
    return render(request, "apple/success.html")

# logout
def logout_form(request):
    logout(request)
    return redirect("/apple/login/")
