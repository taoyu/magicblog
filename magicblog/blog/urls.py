from django.conf.urls.defaults import *
from django.views.generic import list_detail, date_based
from magicblog.blog.models import Post
from magicblog.blog.views import *

from magicblog.blog.feeds import BlogLatestEntries

from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap


feeds = {
    'latest' : BlogLatestEntries
}

info_dict = {
    'queryset': Post.objects.all(),
    'date_field' : 'pub_date',
}

sitemaps = {
    'flatpages' : FlatPageSitemap,
    'blog' : GenericSitemap(info_dict, priority=0.6, changefreq = "monthly"),
}


urlpatterns = patterns('',
    url(r'^post/(?P<slug>[a-z-]+)/$', blog_generic_view, 
        {'redirect_to': list_detail.object_detail, 'slug_field': 'slug', 'paginate': False,}, name="single_post"),
    url(r'^$', blog_generic_view, 
        {'redirect_to': list_detail.object_list}, name="blog_home"),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{1,2})/$', blog_generic_view,
        {'redirect_to': date_based.archive_month, 'month_format': '%m', 'date_field': 'pub_date', 'template_name': 'blog/post_list.html', 'paginate': False,}
            , name="blog_posts_by_month"),
    url(r'^category/(\d+)/$', blog_posts_by_category, name="blog_posts_by_category"),
    url(r'^tag/(\d+)/$', blog_posts_by_tag, name="blog_posts_by_tag"),

    url(r'^search/$', blog_post_search, name="blog_post_search"),

    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),

    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps' : sitemaps}),
)
