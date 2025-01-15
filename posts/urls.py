from . import views
from django.urls import path

urlpatterns = [
    path("homepage/",views.homepage, name="posts"),
    path("list/",views.all_posts,name="posts"),
    path("post/<int:post_id>",views.post_detail,name="post"),
    path("update/<int:post_id>",views.updatePost,name="postUpdate"),
    path("delete/<int:post_id>",views.DeletePost,name="delete"),
    path("postsList/",views.PostListCreateView.as_view(),name="viewPostList"),
    path("updateView/<int:post_id>",views.UpdateView.as_view(),name="updateview"),
    path("mixinsall/<int:pk>",views.PostUpdateDeleteMixins.as_view())
]
