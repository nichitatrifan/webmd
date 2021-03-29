from django.urls import path
from .import views

app_name = 'posts'
urlpatterns = [
    path('', views.posts_home, name='posts_home'),
    path('create', views.create_post, name='create_post'),
    path('<int:pk>',views.PostDetailView.as_view(), name='post_details'),
    path('<int:pk>/update',views.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete',views.PostDeleteView.as_view(), name='post_delete')
]