from django.db import models
from django.utils import timezone


class Contact(models.Model):

    fullname = models.CharField(max_length=50, verbose_name='نام کامل')
    email = models.EmailField(max_length=50, verbose_name='ایمیل')
    mobile = models.CharField(max_length=11, verbose_name='موبایل')
    message = models.TextField(verbose_name='پیام')
    creationDate = models.DateField(
        default=timezone.now, verbose_name='تاریخ ارسال')

    def __str__(self) -> str:
        return self.fullname
