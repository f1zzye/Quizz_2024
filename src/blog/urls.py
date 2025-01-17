from django.urls import include, path

from blog.views import create_blog, all_blogs

app_name = 'blog'

urlpatterns = [
    path("create-blog/", create_blog, name="create_blog"),
    path("", all_blogs, name="all_blogs"),
]