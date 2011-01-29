from django.conf.urls.defaults import *
from django.views.generic import list_detail, date_based
from magicblog.blog.models import Post
from magicblog.blog.views import *

urlpatterns = patterns('',
    url(r'^post/(?P<slug>[a-z-]+)/$', blog_generic_view, 
        {'redirect_to': list_detail.object_detail, 'slug_field': 'slug'}, name="single_post"),
    url(r'^$', blog_generic_view, 
        {'redirect_to': list_detail.object_list}, name="blog_home"),
)
