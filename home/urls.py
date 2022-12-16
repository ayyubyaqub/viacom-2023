from django.urls import path
from home import views

# app_name="home"
urlpatterns = [
    path('', views.index, name="homepage"),
    path('verify-hcaptcha-token', views.verifyHcaptchaToken, name="verifyHcaptchaToken"),
    path('create_video/',views.create_videos,name='create_video'),
    path('pricing/',views.pricing,name='pricing'),
    path('about-us/',views.about,name='about-us'),
    path('works/',views.works,name='works'),
    path('marketplace/',views.marketplace,name='marketplace'),
    path('contactus/',views.contactus,name='contactus'),
    path('contact-us/',views.contactus,name='contact-us'),
    path('all-industry/',views.industry,name='all-industry'),   
    path('categories/',views.categories,name='categories'),
    path('creators/',views.creator,name='creators'),  
    path('subscription/',views.subscription,name='subscription'),
    path('24x7/',views.two_four_seven,name='24x7'),
    path('career/',views.career_view,name='career'),
    path('media/',views.media_view,name='media'),
    path('shorts/',views.shorts_view,name='shorts'),
    path('shorts/page=<int:num>/',views.shorts_view,name='shorts'),
    path('marketing/',views.marketing_view,name='marketing'),
    path('video-marketing/',views.video_marketing_view,name='video-marketing'),
    path('experimental-marketing/',views.experimental_marketing_view,name='experimental-marketing'),
    path('academics/',views.academics_view,name='academics'),
    path('terms-and-conditions/',views.allTermsAndCondition,name='all-terms-and-condition'),
    path('terms-and-condition/<slug:slug>/',views.termsAndCondition,name='terms-and-condition'),
    path('<slug:slug>/',views.category,name='category'),   
] 
