"""
URL configuration for social_media_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from feed.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserCreateView.as_view()),
    path('login/', LoginView.as_view()),
    path('postcreate/', PostCreateView.as_view()),
    path('post/', PostListView.as_view()),
    path('post/<int:pk>/', PostDetailView.as_view()),
    path('comment/<int:pk>/', CommentCreateView.as_view()),
    path('listcomment/<int:pk>/', CommentListView.as_view()),
    path('like/<int:pk>/', LikeCreateView.as_view()),
    path('unlike/<int:pk>/', UnlikeView.as_view()),
    path('follow/', FollowCreateView.as_view()),
    path('listfollow/', FollowListView.as_view()),
    path('unfollow/<int:pk>/', UnfollowView.as_view()),
    path('followers/', FollowersListView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('myposts/', UserPostListView.as_view()),
    ]
