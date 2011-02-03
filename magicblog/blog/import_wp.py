from magicblog.blog.models import *

from django.shortcuts import redirect

from django.contrib.comments import *

import os
import xml.etree.ElementTree as ET

from datetime import datetime

def parse_date(date_str):
	try:
		date = datetime.strptime(date_str ,"%Y-%m-%d %H:%M:%S")
	except:
		try:
			date = datetime.strptime(date_str ,"%a, %d %b %Y %H:%M:%S")
		except:
			date = datetime.now()
	return date

def import_wp(request):
	wpns = "{http://wordpress.org/export/1.0/}"
	contentns = "{http://purl.org/rss/1.0/modules/content/}"
	excerptns = "{http://wordpress.org/export/1.0/excerpt/}"

	root = ET.parse(os.path.join(os.path.abspath(os.path.dirname(__file__)),'wordpress.xml')).getroot().find('channel')

	for item in root.findall(wpns+'category'):
		category = Category()
		category.name = item.findtext(wpns+'cat_name')
		category.save()

	for item in root.findall(wpns+'tag'):
		tag = Tag()
		tag.name = item.findtext(wpns+'tag_name')
		tag.save()


	for item in root.findall('item'):
		post = Post()
		post.author_id = 1
		post.title = item.findtext('title')
		post.slug = item.findtext(wpns+'post_id')
		post.body = item.findtext(contentns+'encoded')
		post.excerpt = item.findtext(excerptns+'encoded')
		post.published = True

		date = item.findtext(wpns+'post_date')
		
		post.pub_date = parse_date(date)

		post.up_date = post.pub_date

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

		comments = item.findall(wpns+'comment')
		for c in comments:
			comment = Comment()
			comment.content_object = post

			comment.site_id = 1
			
			comment.user_name = c.findtext(wpns+'comment_author')
			comment.user_email = c.findtext(wpns+'comment_author_email')
			comment.user_url = c.findtext(wpns+'comment_author_url')

			date = c.findtext(wpns+'comment_date')
			comment.submit_date = parse_date(date)

			comment.comment = c.findtext(wpns+'comment_content')
			comment.is_public = True
			
			comment.save()
	return redirect('/')
