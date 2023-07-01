from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from website import forms
from website.models import Category, FlashNews, Slider, WebsiteSetting, Article, Video, LatestVideo, SportLight, \
    Comment, AboutUs


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
            'article': article,
            'menus': Category.objects.filter(is_menu=True, is_active=True),
            'flash_news': FlashNews.objects.last()
        }
        return render(request, 'article-details.html', context=context)



class SportLightNewsDetailView(View):

    def get(self, request, sportLightNews_id):
        sportLightNews = SportLight.objects.get(id=sportLightNews_id)
        context = {
            'sportLightNews': sportLightNews,
            'menus': Category.objects.filter(is_menu=True, is_active=True),
            'flash_news': FlashNews.objects.last()
        }
        return render(request, 'sport-light-news-details.html', context=context)

class SportLightMiddleNewsDetailView(View):
    def get(self, request, middleNews_id):
        middleNews = SportLight.objects.get(id=middleNews_id)
        context = {
            'middleNews': middleNews,
            'menus': Category.objects.filter(is_menu=True, is_active=True),
            'flash_news': FlashNews.objects.last()
        }
        return render(request, 'sport-light-middle-news-details.html', context=context)

class CelebrityNewsView(View):
    def get(self, request, cn_id):
        cn = SportLight.objects.get(id=cn_id)
        context = {
            'cn': cn,
            'menus': Category.objects.filter(is_menu=True, is_active=True),
            'flash_news': FlashNews.objects.last()
        }
        return render(request, 'celebrity-news-details.html', context=context)

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            password = form.data['password']
            user = form.save()
            user.set_password(password)
            user.save()
            messages.success(request, 'Registration successfully done')
            return redirect('/auth/login/')

        else:
            messages.error(request, 'Invalid data')

        context = {form: 'form'}
        return render(request, 'register.html', context=context)

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.data['username']
            password = form.data['password']
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    login(request, user)
                    messages.success(request, 'Logged in successfully')
                    return redirect('/')
                messages.error(request, 'Password did not match')
            except ObjectDoesNotExist:
                messages.error(request, 'User not found')
        else:
            messages.error(request, 'Invalid data')
        context = {'form': form}
        return render(request, 'login.html', context=context)
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/auth/login/')
class CommentView(View):
    def post(self, request, article_id):
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.data['comment']
            Comment.objects.create(
                user=self.request.user,
                article_id=article_id,
                comment=comment
            ).save()
        else:
            messages.error(request, 'Invalid data')

        return redirect(f"/article/detail/{article_id}")

class ContactUsView(TemplateView):
    template_name = 'contactus.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menus'] = Category.objects.filter(is_menu=True, is_active=True)
        context['flash_news'] = FlashNews.objects.last()
        return context

class ContactView(View):
    def post(self, request):
        form = forms.ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'You data has been successfully.')
        else:
            messages.error(request,'Invalid! Please try again.')
        return redirect('/contact/')
class AboutUsView(TemplateView):
    template_name = 'aboutus.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menus'] = Category.objects.filter(is_menu=True, is_active=True)
        context['flash_news'] = FlashNews.objects.last()
        context['aboutus'] = AboutUs.objects.last()
        return context

def business(request):
    context = {
        'menus': Category.objects.filter(is_menu=True, is_active=True),
        'flash_news': FlashNews.objects.last()
    }
    return render(request, 'business.html', context)
def magazine(request):
    context = {
        'menus': Category.objects.filter(is_menu=True, is_active=True),
        'flash_news': FlashNews.objects.last()
    }
    return render(request, 'magazine.html', context)
def politics(request):
    context = {
        'menus': Category.objects.filter(is_menu=True, is_active=True),
        'flash_news': FlashNews.objects.last()
    }
    return render(request, 'politics.html', context)
def sports(request):
    context = {
        'menus': Category.objects.filter(is_menu=True, is_active=True),
        'flash_news': FlashNews.objects.last()
    }
    return render(request, 'sports.html', context)