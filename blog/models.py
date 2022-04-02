import os.path

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)  # NULL 허용
    attached_file = models.FileField(upload_to='blog/files/%Y/%m/%d', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):    # 인터페이스
        return f'/blog/{self.pk}/'

    # full name 을 base name 으로 변환
    def get_file_name(self):
        return os.path.basename(self.attached_file.name)
