import xml.etree.ElementTree as ET


from django.template.defaultfilters import slugify

import os


root = ET.parse(os.path.join(os.path.abspath(os.path.dirname(__file__)),'blog/wordpress.xml')).getroot().find('channel')

for item in root.findall('item'):
	print item.findtext('title')
	print item.findtext('{http://wordpress.org/export/1.0/}post_id')
	print item.findtext('{http://purl.org/rss/1.0/modules/content/}encoded')
	print item.findtext('{http://wordpress.org/export/1.0/excerpt/}encoded')
	print item.findtext('{http://wordpress.org/export/1.0/}post_date')

        categories = item.findall("category")
        for c in categories:
#		cat = Category.objects.get(name=c.text)
#		post.categories.add(cat)
		if c.attrib.has_key('nicename'):
			nicename = c.attrib['nicename']
			cat_type = c.attrib['domain']
			if cat_type == 'tag':
				print 'tag:'+c.text
			else:
				print 'category:'+c.text
	print '\n\n\n'
