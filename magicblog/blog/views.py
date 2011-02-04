from django.shortcuts import render_to_response, get_object_or_404, redirect
from magicblog.blog.models import *
from django.views.generic import list_detail



def blog_generic_view(request, redirect_to, paginate = True, **view_args):
    view_args['queryset'] = view_args.get('queryset', Post.objects.all())
    view_args['template_object_name'] = 'post'
   
    if paginate:
        view_args['paginate_by'] = 5
    
    return redirect_to(request, **view_args)

def blog_posts_by_category(request, category_id):
    category = get_object_or_404(Category, pk = category_id)
    return blog_generic_view(
        request,
        list_detail.object_list,
	paginate = False,
        queryset = category.post_set.all()
    )

def blog_posts_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, pk = tag_id)
    return blog_generic_view(
        request,
        list_detail.object_list,
	paginate = False,
        queryset = tag.post_set.all()
    )

def blog_post_search(request):
    if 's' in request.GET and request.GET['s']:
        s = request.GET['s']
        return blog_generic_view(
            request,
            list_detail.object_list,
	    queryset = Post.objects.search(s)
        )
    else:
        return render_to_response('blog/invalid_search.html')
