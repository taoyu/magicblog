from django.shortcuts import render_to_response, get_object_or_404
from magicblog.blog.models import *
from django.views.generic import list_detail

def blog_generic_view(request, redirect_to, **view_args):
    view_args['queryset'] = view_args.get('queryset', Post.objects.all())
    view_args['template_object_name'] = 'post'
    
    
    return redirect_to(request, **view_args)

def blog_posts_by_category(request, category_id):
    category = get_object_or_404(Category, pk = category_id)
    return blog_generic_view(
        request,
        list_detail.object_list,
        queryset = category.post_set.all()
    )

def blog_posts_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, pk = tag_id)
    return blog_generic_view(
        request,
        list_detail.object_list,
        queryset = tag.post_set.all()
    )
