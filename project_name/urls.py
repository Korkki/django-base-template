from __future__ import unicode_literals
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap
}

urlpatterns = patterns('',
   url(r'^admin/', include(admin.site.urls)),
   url(r'^robots\.txt', TemplateView.as_view(template_name='robots.txt')),
   url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
   url(r'$', TemplateView.as_view(template_name='index.html'), name='index'),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns += patterns('', url(r'^__debug__/', include(debug_toolbar.urls)))
    urlpatterns += patterns('', url(r'^silk/', include('silk.urls', namespace='silk')))
