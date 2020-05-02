from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView,MoviePostListView
from . import views

urlpatterns = [
    path('',PostListView.as_view(),name='home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
    path('user/<str:username>', UserPostListView.as_view(), name='user_posts'),
    path('movie/<str:movie>', MoviePostListView.as_view(),name='movie_posts'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
