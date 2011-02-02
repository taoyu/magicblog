from django.shortcuts import render_to_response, get_object_or_404, redirect
from magicblog.blog.models import *
from django.views.generic import list_detail

import os
import xml.etree.ElementTree as ET

from datetime import datetime

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
        queryset = category.post_set.all()
    )

def blog_posts_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, pk = tag_id)
    return blog_generic_view(
        request,
        list_detail.object_list,
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

def test(request):
	root = ET.parse(os.path.join(os.path.abspath(os.path.dirname(__file__)),'wordpress.xml')).getroot().find('channel')

	for item in root.findall('{http://wordpress.org/export/1.0/}category'):
		category = Category()
		category.name = item.findtext('{http://wordpress.org/export/1.0/}cat_name')
		category.save()

	for item in root.findall('{http://wordpress.org/export/1.0/}tag'):
		tag = Tag()
		tag.name = item.findtext('{http://wordpress.org/export/1.0/}tag_name')
		tag.save()


	for item in root.findall('item'):
		post = Post()
		post.author_id = 1
		post.title = item.findtext('title')
		post.slug = item.findtext('{http://wordpress.org/export/1.0/}post_id')
		post.body = item.findtext('{http://purl.org/rss/1.0/modules/content/}encoded')
		post.excerpt = item.findtext('{http://wordpress.org/export/1.0/excerpt/}encoded')
		post.published = True

		date = item.findtext('{http://wordpress.org/export/1.0/}post_date')
		
		try:
			pub_date = datetime.strptime(date ,"%Y-%m-%d %H:%M:%S")
		except:
			try:
				pub_date = datetime.strptime(date ,"%a, %d %b %Y %H:%M:%S")
			except:
				pub_date = datetime.now()

		up_date = pub_date

		post.save()

		categories = item.findall("category")
		for c in categories:
			if c.attrib.has_key('nicename'):
				nicename = c.attrib['nicename']
				cat_type = c.attrib['domain']
				if cat_type == 'tag':
					tag = Tag.objects.get(name=c.text)
					if tag:
						post.tags.add(tag)
				else:
					cat = Category.objects.get(name=c.text)
					if cat:
						post.categories.add(cat)

		post.save()

	return redirect('/')
