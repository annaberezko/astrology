from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Service, Reviews, Articles, Pages
from .forms import ReviewsForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView


class ReviewView(CreateView):
    form_class = ReviewsForm
    model = Reviews
    # fields = '__all__'
    template_name = 'astro_app/reviews.html'
    success_url = '../done/'
    extra_context = {'reviews': Reviews.objects.all().order_by('-id')}

class DoneView(ListView):
    template_name = "astro_app/done.html"
    model = Reviews
    context_object_name = 'reviews'

    def get_queryset(self):
        context = super().get_queryset()
        filter_qs = context.order_by('-id')
        return filter_qs

# class FeedBackUpdateView(UpdateView):
#     model = Reviews
#     form_class = ReviewsForm
#     template_name = 'astro_app/reviews.html'
#     success_url = '../done/'
#     extra_context = {'reviews': Reviews.objects.all()}

class HomeView(ListView):
    template_name = 'astro_app/home.html'
    model = Service
    context_object_name = 'service'

class FAQView(TemplateView):
    template_name = 'astro_app/faq.html'

    def get_context_data(self, **kwargs):
        context = super(FAQView, self).get_context_data(**kwargs)
        context["info"] = Pages.objects.get(id=4)
        return context

class AboutView(TemplateView):
    template_name = 'astro_app/about.html'

    # extra_context = {'info': Pages.objects.get(id=2)}
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context["info"] = Pages.objects.get(id=2)
        return context

class ServisesView(ListView):
    template_name = "astro_app/services.html"
    model = Service
    context_object_name = 'service'

class ArticlesView(ListView):
    template_name = "astro_app/articles.html"
    model = Articles
    context_object_name = 'articles'

    # def get_context_data(self, **kwargs):
    #     context = super(ArticlesView, self).get_context_data(**kwargs)
    #     context["info"] = Articles.objects.get(id=2)
    #     return context

# def Articlestemp(request):
#     a = Articles.objects.all()
#     for item in a:
#         item.save()
#     return HttpResponse("efe")


class Article_View_info(DetailView):
    template_name = "astro_app/article_info.html"
    model = Articles
    context_object_name = 'article'
