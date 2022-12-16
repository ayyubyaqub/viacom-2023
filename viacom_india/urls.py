from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from viacom_india.sitemaps import Static_Sitemap, Categories_Sitemap, Sub_Categories_Sitemap, Super_Categories_Sitemap

sitemaps = {
    'super_categories': Super_Categories_Sitemap(),
    'categories': Categories_Sitemap(),
    'sub_categories': Sub_Categories_Sitemap(),
    'static': Static_Sitemap()
}

urlpatterns = [
    path('admin/clearcache/', include('clearcache.urls')),
    path('admin/', admin.site.urls),
    path('blogs/',include('blogs.urls')),
    path('success-stories/',include('stories.urls')),
    path('d2c/',include('dare2creative.urls')),
    path('api/',include('api.urls')),
    path('vi-network/',include('vi_network.urls')),
    path('other-services/',include('other_services.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('',include('home.urls')),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path(
        'sitemap.xml',
        TemplateView.as_view(template_name="sitemap.xml", content_type="text/plain"),
    ),
    # url(r'^sitemap\.xml$', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
