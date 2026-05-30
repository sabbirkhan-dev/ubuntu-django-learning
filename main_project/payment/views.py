from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Payment, Laptop
from .forms import RecentProduct

# ---- Payment Views ----

def buy(request):
    payment_method = 'Bkash'
    Discount = '70%'
    payment_details = {'pm': payment_method, 'dis': Discount}
    return render(request, "payment/buy.html", {'name': 'Bkash', 'pd': payment_details})

def bk(request):
    return render(request, "payment/bk.html", {'name': 'Bkash', 'nm': 'Sabbir Khan'})

def ng(request):
    names = {'friends': ['sabbir', 'tuhin', 'golam rabbi', 'rayhan', 'shapin', 'sujan']}
    return render(request, 'payment/ng.html', names)

def payment_method(request):
    pay_m = Payment.objects.all()
    return render(request, 'payment/payment.html', {'pay': pay_m})

def sand(request):
    return render(request, 'payment/submit.html')


# ---- Product Form View ----

def recent_product(request):
    if request.method == 'POST':
        # request.FILES oboshioi thakbe file upload er jonno
        frm = RecentProduct(request.POST, request.FILES)
        
        if frm.is_valid():
            # Database-e data save hocche
            Laptop.objects.create(
                mobile=frm.cleaned_data['mobile'],
                laptop=frm.cleaned_data['laptop'],
                email=frm.cleaned_data['email'],
                password=frm.cleaned_data['password'],
                text=frm.cleaned_data['text'],
                check_box=frm.cleaned_data['check_box'],
                file=frm.cleaned_data['file'],
                ram=frm.cleaned_data['ram'],
                youtube_channel=frm.cleaned_data['youtube_channel']
            )
            return HttpResponseRedirect('/pdc/successfully')
        else:
            # Jodi validation fail hoy, terminal-e error dekhাবে
            print("Form Validation Errors:", frm.errors)

    else:
        # GET request ba prothombar load hobar somoy
        frm = RecentProduct(auto_id=True, label_suffix=' - ')
        # Field order choto hater namer sathe match kora holo
        frm.order_fields(field_order=['email', 'laptop', 'mobile'])

    # Validation fail hole error shoho form ferot jabe ekhane
    return render(request, 'payment/recent_product.html', {'form': frm})