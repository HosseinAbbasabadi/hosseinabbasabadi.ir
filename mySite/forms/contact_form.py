from django import forms
from django.forms.fields import CharField, EmailField
from django.forms.widgets import EmailInput, NumberInput, TextInput, Textarea


class ContactForm(forms.Form):
    fullname = CharField(min_length=2, max_length=50, label='ایمیل', widget=TextInput(
        attrs={
            'class': 'form-control', 'placeholder': 'نام و نام خانوادگی'
        }))
    email = EmailField(min_length=10, max_length=50, label='ایمیل', widget=EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'ایمیل'
    }))
    mobile = CharField(min_length=11, max_length=11, widget=NumberInput(attrs={
        'class': 'form-control', 'placeholder': 'موبایل'
    }))
    message = CharField(min_length=10, max_length=1000, label='پیام خود را وارد نمایید', widget=Textarea(attrs={
                        'class': 'form-control', 'placeholder': 'پیام خود را وارد نمایید', 'rows': 5}))
