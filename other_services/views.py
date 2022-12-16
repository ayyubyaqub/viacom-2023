from django.shortcuts import render

from other_services.models import other_services, other_services_page

# Create your views here.
def index(request):
    links = other_services.objects.order_by("serial_number").all()
    page = other_services_page.objects.all().first()
    params = {
        'meta_title': page.meta_title,
        'meta_description': page.meta_description,
        'meta_keywords': page.meta_keywords,
        "links" : links,
        "page" : page
    }
    return render(request, 'other_services/other_services_homePage.html', params)


def others(request , others_slug):
    link = other_services.objects.filter(slug = others_slug).first()
    params = {
        'meta_title': link.meta_title,
        'meta_description': link.meta_description,
        'meta_keywords': link.meta_keywords,
        "other" : link,
    }
    return render(request, 'other_services/others.html', params)

