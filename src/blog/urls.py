from django.urls import include, path

from blog.views import all_blogs, create_blog

app_name = "blog"

urlpatterns = [
    path("create-blog/", create_blog, name="create_blog"),
    path("", all_blogs, name="all_blogs"),
]
