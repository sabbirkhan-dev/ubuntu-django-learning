from django.contrib import admin

# Register your models here.
from payment.models import Payment
from django.contrib import admin
from .models import Payment, Laptop


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):

    list_display = (
        'mobile',
        'laptop',
        'email',
        'password',
        'ram',
        'youtube_channel',
        'created_at',
    )


admin.site.register(Payment)