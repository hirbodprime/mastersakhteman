from django import forms
from django.contrib.auth.models import User

class ContactUsForm(forms.Form):
    name = forms.CharField( max_length=100, required=True,label="نام شما (الزامی)",widget=forms.TextInput(attrs={"placeholder":"نام" }))
    productName = forms.CharField( max_length=100, required=False,label="نام محصول مورد نظر",widget=forms.TextInput(attrs={"placeholder":"جکوزی مدل x-1" }))

    email = forms.EmailField(required=True,label="ایمیل شما (الزامی)",widget=forms.EmailInput(attrs={"placeholder":"your_email@gmail.com*"}))

    title = forms.CharField(max_length=300,required=True,label="موضوع",widget=forms.TextInput(attrs={"placeholder":"موضوع"}))

    phone = forms.CharField(max_length=20,required=True,label="تلفن همراه",widget=forms.TextInput(attrs={"placeholder":"09121111111"}))

    content = forms.CharField(max_length=1000,required=False,label="توضیحات",widget=forms.Textarea(attrs={"placeholder":"توضیحات", "class":"form-control2"}))
     
    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")

        return email

