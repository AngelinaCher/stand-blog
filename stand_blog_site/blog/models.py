from django.db import models
from django.urls import reverse


class Category(models.Model):
    """
    Модель категории
    """
    title = models.CharField(max_length=300, verbose_name='Категория')
    slug = models.SlugField(max_length=300, verbose_name='URL', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname='category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tag(models.Model):
    """
    Модель тега
    """
    title = models.CharField(max_length=70, verbose_name='Тег')
    slug = models.SlugField(max_length=70, verbose_name='URL', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname='tag', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']


class Post(models.Model):
    """
    Модель поста
    """
    title = models.CharField(max_length=70, verbose_name='Заголовок')
    slug = models.SlugField(max_length=70, verbose_name='URL', unique=True)
    author = models.CharField(max_length=120, verbose_name='Автор')
    content = models.TextField(verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото')
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 related_name='posts', verbose_name='Категория')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name='Теги')

    def get_absolute_url(self):
        return reverse(viewname='post', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']


class Contact(models.Model):
    """
     Модель обратной связи
    """
    name = models.CharField(max_length=200, verbose_name='Пользователь')
    email = models.EmailField(max_length=200, verbose_name='Email')
    subject = models.CharField(max_length=100, verbose_name='Тема письма')
    message = models.TextField(max_length=1000, verbose_name='Сообщение')

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    def __str__(self):
        return self.email
