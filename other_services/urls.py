from django.urls import  path
from .views import index , others


app_name='other_services'

urlpatterns = [
    path('', index, name="other_services_home_page"),
    path('<slug:others_slug>', others, name="others"),
] 