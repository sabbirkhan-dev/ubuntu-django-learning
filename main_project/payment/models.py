from django.db import models

# Create your models here.

class Payment(models.Model):
    name = models.CharField(max_length=50)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name 
    

class Laptop(models.Model):
    mobile = models.CharField(max_length=50)
    laptop = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=100)
    text = models.TextField()
    check_box = models.BooleanField(default=False)
    file = models.FileField(upload_to='files/', blank=True, null=True)
    ram = models.IntegerField()
    youtube_channel = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.laptop