from django import http
from django.db import models
from django.shortcuts import render
from django.contrib import messages
from .forms.contact_form import ContactForm
from .models import Contact
from .services import ContactService


def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            result = ContactService.create(form)
            if result > 0:
                messages.success(
                    request, 'پیام شما با موفقیت ارسال شد و پس از بررسی با شما تماس گرفته خواهد شد. متشکرم')
                return http.HttpResponseRedirect('contact')
            else:
                messages.error(
                    request, 'مشکلی رخ داده است، لطفا مجدد تلاش کنید')
                return render(request, 'contact.html', {'form': form})
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})
