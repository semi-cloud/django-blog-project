from django.contrib import admin
from .models import Post, Category, Tag

admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    #기본 값 설정
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    #기본 값 설정
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Tag, TagAdmin)
