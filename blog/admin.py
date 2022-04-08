from django.contrib import admin
from .models import Post, Category

admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    #기본 값 설정
    prepopulated_fields = {'slug': ('name',)}
# Register your models here.

admin.site.register(Category, CategoryAdmin)