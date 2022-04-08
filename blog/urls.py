from django.urls import path
from . import views     # 상대 경로 사용 권장

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('category/<str:slug>/', views.show_category_posts),
    path('tag/<str:slug>/', views.tag_page)
    # path('', views.index),
    # path('<int:pk>/', views.single_post_page),  # blog/1
]
