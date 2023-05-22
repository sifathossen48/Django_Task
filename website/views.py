from django.shortcuts import render
from django.views.generic import TemplateView

from website.models import Category, FlashNews, Slider, Website_Setting


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menus'] = Category.objects.filter(is_menu=True, is_active=True)
        context['flash_news'] = FlashNews.objects.last()
        context['sliders'] = Slider.objects.last()
        context['websettings'] = Website_Setting.objects.last()

        return context



