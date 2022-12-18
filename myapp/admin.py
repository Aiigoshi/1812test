from django.contrib import admin
from myapp.models import MyLessons


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'style', 'level', 'date')


admin.site.register(MyLessons, AuthorAdmin)
# Register your models here.
