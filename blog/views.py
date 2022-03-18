from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    # db post 가져오기
    posts = Post.objects.all().order_by('-pk')
    return render(
        request,
        'blog/index.html',
        {
            'posts': posts
        }
    )

# (실행 경로)blog dir => templates dir => blog dir => index.html (django convention)
# dictionary key 값 - html 파일의 변수 연동