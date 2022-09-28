from django.contrib import admin
from django.urls import path
from post.views import *

urlpatterns = [
    path("<int:pk>/", PostView.as_view(), name="post-detail"),
    path("", PostListView.as_view(), name="post-list"),
]