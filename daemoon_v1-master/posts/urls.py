from django.urls import path, re_path
from . import views


app_name = 'posts'
urlpatterns = [
    path('',views.posts_home,name='posts_home'),
    #path('<int:entry_id>/',views.post_detail,name="post_detail"),
    path('new/',views.posts_new,name="posts_new"),
    path('postslist/<str:category>',views.posts_list,name="posts_list"),
    #path('create/',views.post_create,name="post_create"),
    #path('like/', views.post_like, name='post_like'),
]