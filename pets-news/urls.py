from django.conf.urls import patterns, include, url
from apps.pets.views import NewsDetail
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'apps.pets.views.home', name='home'),
    url(r'^about$', 'apps.pets.views.about', name='about'),
    url(r'^pet/(?P<pet_id>\d+)/$', 'apps.pets.views.pet_detail', name='pet_detail'),
    url(r'^news/(?P<pk>\d+)/$', NewsDetail.as_view(), name='news_detail'),

    url(r'^admin/', include(admin.site.urls)),
)
