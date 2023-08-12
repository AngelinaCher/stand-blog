from django import template
from blog.models import Category

register = template.Library()


# Получение постов по категории
@register.inclusion_tag('blog/categories_tpl.html')
def get_categories():
    categories = Category.objects.all()
    return {"categories": categories}
