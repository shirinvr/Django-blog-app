from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
  path('', views.posts, name='posts'),
  path('get/', views.get_posts, name='get_posts'),
  path('post/', views.write_post, name='write_post'),
  path('<int:post_id>/', views.post, name='post'),
  path('<int:post_id>/get/', views.get_post_by_id, name='get_post_by_id'),
  path('<int:post_id>/comment/', views.write_comment, name='write_comment'),
]