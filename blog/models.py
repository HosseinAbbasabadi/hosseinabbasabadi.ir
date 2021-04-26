from django.db import models
from django.db.models.fields import CharField, DateField, SlugField, TextField
from django.db.models.fields.files import FileField


class Article(models.Model):
    title = CharField(verbose_name='عنوان', max_length=255)
    short_description = CharField(verbose_name='توضیحات کوتاه', max_length=300)
    description = TextField(verbose_name='متن')
    image = CharField(verbose_name='عکس', max_length=500)
    video = CharField(verbose_name='فیلم', max_length=500)
    keywords = CharField(verbose_name='کلمات کلیدی', max_length=100)
    meta_description = CharField(verbose_name='توضیحات متا', max_length=200)
    slug = SlugField(verbose_name='اسلاگ', max_length=300, allow_unicode=True)
    creation_date = DateField(verbose_name='تاریخ ایجاد')
