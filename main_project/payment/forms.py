from django import forms
from django.core import validators

class RecentProduct(forms.Form):
    mobile = forms.CharField(max_length=50)
    laptop = forms.CharField()
    email = forms.EmailField(initial='example@gmail.com',validators=[validators.MaxLengthValidator(30)])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Re Password'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    check_box = forms.BooleanField(required=False)
    file = forms.FileField(required=False)
    ram = forms.IntegerField(min_value=2, max_value=64)
    youtube_channel = forms.BooleanField(required=False)


    def clean_password(self):
        password_validations = self.cleaned_data['password']
        if len(password_validations)<4:
            raise forms.ValidationError("Enter your correct pasword")
        return password_validations

    def clean_laptop(self):
        laptop = self.cleaned_data['laptop']
        if len(laptop)>10:
            raise forms.ValidationError("Enter your correct forms")
        return laptop 
    
    def clean(self):
        cleaned_data= super().clean()
        password_match = self.cleaned_data.get('password')
        re_password_match = self.cleaned_data.get('re_password')
        if password_match != re_password_match:
            raise forms.ValidationError("password dosen't match")
        