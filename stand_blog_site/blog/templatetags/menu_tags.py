from django import template
from blog.models import Tag

register = template.Library()


# Получение постов по тегам
@register.inclusion_tag('blog/tags_tpl.html')
def get_tags():
    tags = Tag.objects.all()
    return {"tags": tags}
