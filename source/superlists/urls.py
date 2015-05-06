from django.conf.urls import patterns, include, url
from django.contrib import admin

from accounts import urls as account_urls

urlpatterns = patterns('',
    url(r'^$', 'lists.views.home_page', name='home'),
    url(r'^lists/', include('lists.urls')),
    url(r'^accounts/', include(account_urls)),
    # url(r'^admin/', include(admin.site.urls)),
)
