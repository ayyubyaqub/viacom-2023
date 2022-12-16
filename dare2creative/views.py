# from django.shortcuts import render
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import redirect, render

from dare2creative.models import Category, D2C_Page, Sub_Category, Super_Category
# Create your views here.

def index(request):
    # blogs = Blog.objects.all().order_by('-pub_date')
    # blog_page = Blog_Page.objects.all().first()
    # shorts = Shorts.objects.all().order_by('-pub_date')
    d2c_page = D2C_Page.objects.all().first()
    super_categories = Super_Category.objects.all()
    # print(d2c_page.d2c_posters_set.all())
    params = {
        'd2c_page' : d2c_page,
        'meta_title': d2c_page.meta_title,
        'meta_description': d2c_page.meta_description,
        'meta_keywords': d2c_page.meta_keywords,
        "super_categories" : super_categories
    }
    return render(request , 'd2c/d2c-HomePage.html' , params)

def category_view(request , category_slug):
    # print("Hello word")
    # return HttpResponse("Hello world" + category_slug)
    sub_categories = Sub_Category.objects.filter(category__slug = category_slug)
    if sub_categories:
        recents = Sub_Category.objects.filter(isFeautered = True)
        category = Category.objects.filter(slug = category_slug ).first()
        params = {
            "slug" : category_slug,
            "category_title" : category.text,
            "sub_categories" : sub_categories,
            "recents" : recents,
            'meta_title': category.meta_title,
            'meta_description': category.meta_description,
            'meta_keywords': category.meta_keywords,
        }
        return render(request , 'd2c/category.html' , params)
    else:
        return redirect("/d2c")




def event_view(request , category_slug , event_slug):
    event = Sub_Category.objects.filter(slug = event_slug).first()
    if event :

        params = {
            "event" : event,
            "category_slug" : category_slug,
            "event_slug" : event_slug,
            'meta_title': event.meta_title,
            'meta_description': event.meta_description,
            'meta_keywords': event.meta_keywords,
        }
        return render(request , 'd2c/event.html' , params)
    else:
        return redirect("/d2c")
    # return HttpResponse( "Hello " + event_slug  + "  world" + category_slug)

# def Subscribe(request ):
    
#     blog = Blog.objects.filter(slug=blog_slug).first()
#     if blog: 
#         params = {
#             'blog' : blog
#         }
#         return render(request , 'blogs/blog.html' , params)
#     else:
#         return redirect('/blogs')