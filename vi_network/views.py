from django.shortcuts import render

from vi_network.models import Vi_Network, Vi_Network_Page

def index(request):
    vi_network = Vi_Network.objects.order_by("serial_number").all()
    page = Vi_Network_Page.objects.first()
    params = {
        "vi_network" : vi_network,
        "page" : page,
        'meta_title': page.meta_title,
        'meta_description': page.meta_description,
        'meta_keywords': page.meta_keywords,

    }
    return render(request , "vi_network/index.html" , params)

# Create your views here.
