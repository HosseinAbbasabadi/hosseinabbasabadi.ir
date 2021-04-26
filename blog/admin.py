from blog.models import Article
from django.contrib import admin

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    exclude = ('creation_date',)
    list_display = ('title', 'short_description')
    search_fields = ['title']


admin.site.register(Article, ArticleAdmin)
