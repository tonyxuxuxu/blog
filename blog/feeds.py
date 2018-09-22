from django.contrib.syndication.views import Feed
from .models import Post


class AllPostsRssFeed(Feed):
    title = 'Django personal blog'
    link = '/'
    description = 'Django blog'

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[{}] {}'.format(item.category, item.title)

    def item_description(self, item):
        return item.body