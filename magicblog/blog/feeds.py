from django.contrib.syndication.feeds import Feed
from magicblog.blog.models import Post

class BlogLatestEntries(Feed):
    title = "The super Blog"
    link = "/"
    description = "The latest stuff in the blog."
    
    def items(self):
        return Post.objects.all()[:10]
