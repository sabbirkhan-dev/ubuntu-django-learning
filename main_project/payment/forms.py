from django import forms

class RecentProduct(forms.Form):
    Mobile = forms.CharField(max_length=50)
    Laptop = forms.CharField(max_length=50)
    Email = forms.EmailField(max_length=30, initial='example@gmail.com')
    Password = forms.CharField(widget=forms.PasswordInput)
    Text = forms.CharField(widget=forms.Textarea)
    Check_Box = forms.CharField(widget=forms.CheckboxInput)