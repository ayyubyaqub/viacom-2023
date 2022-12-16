from django.urls import  path
from .views import index , category_view , event_view


app_name='dare2creative'

urlpatterns = [
    path('', index, name="d2c"),
    path('<slug:category_slug>', category_view, name="category"),
    path('<slug:category_slug>/<slug:event_slug>', event_view, name="events"),
    # path('subscribe/',Subscribe , name="subscribe"),
  
] 