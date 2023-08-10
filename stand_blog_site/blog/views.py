from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.core.mail import send_mail, BadHeaderError
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.db.models import F

from .models import Post, Category, Tag, Contact
from .forms import ContactForm


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Stand Blog '
        return context


class News(ListView):
    model = Post
    template_name = 'blog/news.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости'
        return context


class PostByCategory(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'categories'
    paginate_by = 6
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class PostByTag(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Записи по тегу: {Tag.objects.get(slug=self.kwargs['slug'])}"
        return context


class GetPost(DetailView):
    model = Post
    template_name = 'blog/single_post.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class Search(ListView):
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context


class ContactCreate(SuccessMessageMixin, CreateView):
    template_name = 'blog/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')
    extra_context = {'title': 'Контакты'}

    def form_valid(self, form):
        subject = form.cleaned_data.get('subject')
        sender = 'AngelinaVeza@yandex.ru'
        message = form.cleaned_data.get('message')
        recipients = [form.cleaned_data.get('email')]
        name = form.cleaned_data.get('name')
        if form.is_valid():
            try:
                response_letter = f'{name}, большое спасибо за обратную связь. Мы учтём ваши пожелания!'
                send_mail(subject=subject, message=response_letter, from_email=sender, recipient_list=recipients)
                contact = Contact(
                    name=form.cleaned_data['name'],
                    email=form.cleaned_data['email'],
                    subject=form.cleaned_data['subject'],
                    message=form.cleaned_data['message']
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found')
        return super().form_valid(form)

