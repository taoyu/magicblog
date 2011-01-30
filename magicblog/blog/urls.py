from django.conf.urls.defaults import *
from django.views.generic import list_detail, date_based
from magicblog.blog.models import Post
from magicblog.blog.views import *

urlpatterns = patterns('',
    url(r'^post/(?P<slug>[a-z-]+)/$', blog_generic_view, 
        {'redirect_to': list_detail.object_detail, 'slug_field': 'slug'}, name="single_post"),
    url(r'^$', blog_generic_view, 
        {'redirect_to': list_detail.object_list}, name="blog_home"),
    url(r'^archive/(?P<month>[a-z]+)/(?P<year>\d{4})/$', blog_generic_view,
        {'redirect_to': date_based.archive_month, 'date_field': 'pub_date', 'template_name': 'blog/post_list.html',}
            , name="blog_posts_by_month"),
    url(r'^category/(\d+)/$', blog_posts_by_category, name="blog_posts_by_category"),
    url(r'^tag/(\d+)/$', blog_posts_by_tag, name="blog_posts_by_tag"),
)
