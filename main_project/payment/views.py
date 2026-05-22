from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

def buy(request):
    payment_method = 'Bkash'
    Discount = '70%'
    payment_details = {'pm': payment_method, 'dis': Discount}
    return render(request, "payment/buy.html", {'name':'Bkash', 'pd' : payment_details})

def bk(request):
    return render(request, "payment/bk.html", {'name':'Bkash', 'nm': 'Sabbir Khan'})


def ng(request):
    names ={'friends': ['sabbir', 'tuhin', 'golam rabbi', 'rayhan', 'shapin', 'sujan']}
    return render(request, 'payment/ng.html', names)

from .models import Payment

def payment_method(request):
    pay_m = Payment.objects.all()
    return render(request, 'payment/payment.html', {'pay': pay_m})


# form link start here
from .forms import RecentProduct
def recent_product(request):
    frm = RecentProduct(auto_id=True, label_suffix=' - ')
    frm.order_fields(field_order=['Email', 'Laptop','Mobile'])

    return render(request, 'payment/recent_product.html', {'form': frm})