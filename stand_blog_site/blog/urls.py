from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', TemplateView.as_view(template_name="blog/about.html"), name='about'),
    path('category/<str:slug>/', views.PostByCategory.as_view(), name='category'),
    path('tag/<str:slug>/', views.PostByTag.as_view(), name='tag'),
    path('post/<str:slug>/', views.GetPost.as_view(), name='post'),
    path('search/', views.Search.as_view(), name='search'),
]
