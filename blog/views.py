from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post
# Create your views here.
# (실행 경로)blog dir => templates dir => blog dir => post_list.html (django convention)
# dictionary key 값 - html 파일의 변수 연동

# def index(request):
#     # db post 가져오기
#     posts = Post.objects.all().order_by('-pk')
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts': posts
#         }
#     )
#
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(
#         request,
#         'blog/post_detail.html',
#         {
#             'post': post
#         }
#     )

class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post

