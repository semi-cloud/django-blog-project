import os.path

from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)  # url에 들어갈 수 없는 문자들 지원

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'

    class Meta:   # override
        verbose_name_plural = 'Categories'


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_msg = models.TextField(blank=True)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)  # NULL 허용
    attached_file = models.FileField(upload_to='blog/files/%Y/%m/%d', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.title} : {self.author}'

    def get_absolute_url(self):    # 인터페이스
        return f'/blog/{self.pk}/'

    # full name 을 base name 으로 변환
    def get_file_name(self):
        return os.path.basename(self.attached_file.name)