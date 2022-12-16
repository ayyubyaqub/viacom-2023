# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
# Create your views here.
from .models import Blog, Blog_Page,Newsletter_Subscription
from home.models import Shorts

def index(request):
    blogs = Blog.objects.all().order_by('-pub_date')
    blog_page = Blog_Page.objects.all().first()
    shorts = Shorts.objects.all().order_by('-pub_date')
    params = {
        # 'first_blog' : blogs[0:1][0],
        'blogs' : blogs,
        'shorts': shorts[:10],
        'blog_page' : blog_page,
        'meta_title': blog_page.meta_title,
        'meta_description': blog_page.meta_description,
        'meta_keywords': blog_page.meta_keywords,
    }
    print(blogs[0:1][0])
    return render(request , 'blogs/blogHomepage.html' , params)

def blog_view(request , blog_slug):
    if request.method == 'POST':
        email = request.POST.get("email")
        Newsletter_Subscription.objects.create(email=email)
    blog = Blog.objects.filter(slug=blog_slug).first()
    
    if blog: 
        params = {
            'blog' : blog,
            'meta_title': blog.meta_title,
            'meta_description': blog.meta_description,
            'meta_keywords': blog.meta_keywords,
        }
        return render(request , 'blogs/blog.html' , params)
    else:
        return redirect('/blogs')

        
# def Subscribe(request ):
    
#     blog = Blog.objects.filter(slug=blog_slug).first()
#     if blog: 
#         params = {
#             'blog' : blog
#         }
#         return render(request , 'blogs/blog.html' , params)
#     else:
#         return redirect('/blogs')