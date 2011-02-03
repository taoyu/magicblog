from django.contrib import admin
from magicblog.blog.models import *

class PostAdmin(admin.ModelAdmin):
	filter_horizontal = ("categories", "tags", )
	list_display = ("title", "published", "pub_date", "id")
	date_hierarchy = 'pub_date'
	prepopulated_fields = {"slug" : ("title",)}
	
	def save_model(self, request, obj, form, change):
		if not change:
			obj.author=request.user
		obj.save()

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
