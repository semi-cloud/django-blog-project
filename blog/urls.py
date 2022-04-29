from django.urls import path
from . import views     # 상대 경로 사용 권장

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('<int:pk>/new_comment/', views.new_comment),
    path('category/<str:slug>/', views.show_category_posts),
    path('tag/<str:slug>/', views.tag_page),
    path('create_post/', views.PostCreate.as_view()),
    path('update_post/<int:pk>', views.PostUpdate.as_view())
    # path('', views.index),
    # path('<int:pk>/', views.single_post_page),  # blog/1
]
