from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('article/detail/<int:article_id>', views.ArticleDetailView.as_view(), name='article-details'),
    path('sportLightNews/detail/<int:sportLightNews_id>', views.SportLightNewsDetailView.as_view(),
         name='sport-light-news-details'),
    path('sportLightMiddleNews/detail/<int:middleNews_id>', views.SportLightMiddleNewsDetailView.as_view(),
         name='sport-light-middle-news-details'),
    path('celebrityNews/detail/<int:cn_id>', views.CelebrityNewsView.as_view(), name='celebrity-news-details'),
    path('article/comment/<int:article_id>', views.CommentView.as_view(), name='article-comment'),
    path('contact/', views.ContactUsView.as_view(), name='contact-us'),
    path("contact", views.ContactView.as_view(), name='contact'),
    path('business/', views.business, name='business'),
    path('magazine/', views.magazine, name='magazine'),
    path('politics/', views.politics, name='politics'),
    path('sports/', views.sports, name='sports'),
    path('about-us/', views.AboutUsView.as_view(), name='about-us')
]
