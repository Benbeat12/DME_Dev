from django.urls import path
from .views import (
    BlogListView,
    BlogCreateView,
    BlogDetailView,
    BlogUpdateView,
    BlogDeleteView,
    PostListView)

urlpatterns = [
    # home blog view -- public blog view
    path("",BlogListView.as_view(),name="blog"),
    #personal user view
    path("post/list/",PostListView.as_view(), name="post_list"),
    path("post/new/",BlogCreateView.as_view(),name='post_new'),
    path("post/<int:pk>/",BlogDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/update/",BlogUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/",BlogDeleteView.as_view(), name="post_delete"),
]
