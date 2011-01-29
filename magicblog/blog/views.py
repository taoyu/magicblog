from django.shortcuts import render_to_response, get_object_or_404
from magicblog.blog.models import *
from django.views.generic import list_detail

def blog_generic_view(request, redirect_to, **view_args):
    view_args['queryset'] = view_args.get('queryset', Post.objects.all())
    view_args['template_object_name'] = 'post'
    
    
    return redirect_to(request, **view_args)
