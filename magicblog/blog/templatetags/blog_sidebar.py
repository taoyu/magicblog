from django import template
register = template.Library()

from magicblog.blog.models import *

@register.inclusion_tag('blog/categories.html')
def blog_categories():
    return {
            'categories': Category.objects.all(),
    }
    
@register.inclusion_tag('blog/archive.html')
def blog_archive():
    return {
            'archives': Post.objects.dates('pub_date', 'month', order='DESC'),
    }

@register.inclusion_tag('blog/tags.html')
def blog_tags():
    return {
            'tags': Tag.objects.all(),
    }

