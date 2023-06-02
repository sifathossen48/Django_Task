from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from website.models import Category, FlashNews, Slider, WebsiteSetting, Article, Video, LatestVideo, SportLight


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menus'] = Category.objects.filter(is_menu=True, is_active=True)
        context['flash_news'] = FlashNews.objects.last()
        context['sliders'] = Slider.objects.last()
        context['websettings'] = WebsiteSetting.objects.last()
        context['categorys'] = Category.objects.filter(is_menu=True)
        context['articles'] = Article.objects.filter(is_draft=False)
        context['videos'] = Video.objects.all()
        context['latestvideos'] = LatestVideo.objects.filter(is_active=True)
        context['sport_lights'] = SportLight.objects.filter(is_actives=True)
        context['sport_lights_center'] = SportLight.objects.filter(is_active=True)
        context['sport_lights_middle'] = SportLight.objects.filter(is_display=True)
        context['celebrity_news'] = SportLight.objects.filter(is_celebrity_news=True)
        return context



class ArticleDetailView(View):

    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        context = {
            'article': article
        }
        return render(request, 'article-details.html', context=context)


class SportLightNewsDetailView(View):

    def get(self, request, sportLightNews_id):
        sportLightNews = SportLight.objects.get(id=sportLightNews_id)
        context = {
            'sportLightNews': sportLightNews
        }
        return render(request, 'sport-light-news-details.html', context=context)

class SportLightMiddleNewsDetailView(View):
    def get(self, request, middleNews_id):
        middleNews = SportLight.objects.get(id=middleNews_id)
        context = {
            'middleNews': middleNews
        }
        return render(request, 'sport-light-middle-news-details.html', context=context)

class CelebrityNewsView(View):
    def get(self, request, cn_id):
        cn = SportLight.objects.get(id=cn_id)
        context = {
            'cn': cn
        }
        return render(request, 'celebrity-news-details.html', context=context)