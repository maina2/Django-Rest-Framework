from . import views
from django.urls import path

urlpatterns = [
    path("homepage/",views.homepage, name="posts"),
    path("list/",views.all_posts,name="posts"),
    path("post/<int:post_id>",views.post_detail,name="post")
]
