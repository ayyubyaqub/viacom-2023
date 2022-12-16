from django.urls import  path
from .views import index


app_name='vi_network'

urlpatterns = [
    path('', index, name="vi_network"),
] 