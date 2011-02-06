from django.contrib.syndication.feeds import Feed
from magicblog.blog.models import Post

class BlogLatestEntries(Feed):
    title = "stay hungry, stay foolish"
    link = "/"
    description = "The latest stuff in the blog."
    
    def items(self):
        return Post.objects.all()[:10]
