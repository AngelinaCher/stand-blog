from django import template
from blog.models import Post

register = template.Library()


# Получение постов популярных постов
@register.inclusion_tag('blog/popular_posts_tpl.html')
def get_popular_post(count=3):
    posts = Post.objects.order_by('-views')[:count]
    return {'posts': posts}
