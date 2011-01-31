from django.conf.urls.defaults import *
from magicblog.views import *

from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^magicblog/', include('magicblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    (r'^comments/', include('django.contrib.comments.urls')),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.STATIC_PATH}),



    (r'^', include("magicblog.blog.urls")),
)
