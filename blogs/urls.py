from django.urls import  path
from blogs.views import blog_view, index


app_name='blogs'

urlpatterns = [
    path('', index, name="blogs"),
    path('<slug:blog_slug>', blog_view, name="blog_detail"),
    # path('subscribe/',Subscribe , name="subscribe"),
  
] 