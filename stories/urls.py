from django.urls import  path
from stories.views import story_view,index


app_name='stories'

urlpatterns = [
    path('', index, name="stories"),
    path('<slug:story_slug>', story_view, name="story_detail"),
    # path('subscribe/',Subscribe , name="subscribe"),
  
] 