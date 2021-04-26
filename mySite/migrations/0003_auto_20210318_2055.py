# Generated by Django 3.1.7 on 2021-03-18 17:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mySite', '0002_auto_20210316_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='creationDate',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='تاریخ ارسال'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='fullname',
            field=models.CharField(max_length=50, verbose_name='نام کامل'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(verbose_name='پیام'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mobile',
            field=models.CharField(max_length=11, verbose_name='موبایل'),
        ),
    ]