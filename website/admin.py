from django.contrib import admin

from website.models import Category, FlashNews, Slider, WebsiteSetting, Article, Teg, Video, LatestVideo, SportLight, \
    Comment, Contact, AboutUs

# Register your models here.
admin.site.register(Category)
admin.site.register(AboutUs)
admin.site.register(FlashNews)
admin.site.register(Slider)
admin.site.register(WebsiteSetting)
admin.site.register(Article)
admin.site.register(Teg)
admin.site.register(Video)
admin.site.register(LatestVideo)
admin.site.register(SportLight)
admin.site.register(Comment)
admin.site.register(Contact)
