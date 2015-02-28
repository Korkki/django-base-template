from __future__ import unicode_literals
from django.contrib import sitemaps
from django.core.urlresolvers import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1
    changefreq = 'weekly'

    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)
