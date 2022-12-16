# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
# Create your views here.
from .models import Story,Story_page

def index(request):
    stories = Story.objects.all()
    story_page_detail = Story_page.objects.all().first()
    params = {
        'stories' : stories,
        "detail" : story_page_detail,
        'create_video_footer':False,
        'meta_title': story_page_detail.meta_title,
        'meta_description': story_page_detail.meta_description,
        'meta_keywords': story_page_detail.meta_keywords,
    }
    return render(request , 'stories/storyHomepage.html' , params)

def story_view(request , story_slug):
    print(request.path.split("/")[1])
    story = Story.objects.filter(slug=story_slug).first()
    if story: 
        params = {
            'story' : story,
            'create_video_footer':False,
            'meta_title': story.meta_title,
            'meta_description': story.meta_description,
            'meta_keywords': story.meta_keywords,

        }

        return render(request , 'stories/story.html' , params)
    else:
        return redirect('/stories')

        
