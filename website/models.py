from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    is_menu = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    html_file = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class FlashNews(models.Model):
    title = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Slider (models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='slider/')
    news_type = models.CharField(max_length=100)
    news_desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class WebsiteSetting(models.Model):
    site_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo/')
    facebook = models.CharField(max_length=100)
    youtube = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)

    def __str__(self):
        return self.site_name

class Teg(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='articles/')
    timestamp = models.DateTimeField(auto_now=True)
    desc = models.TextField()
    author_image = models.ImageField(upload_to='articles/')
    author_name = models.CharField(max_length=100)
    tegs = models.ManyToManyField(Teg)
    is_draft = models.BooleanField(default=True)


    @property
    def get_short_desc(self):
        return self.desc[:100]

    def get_related_posts(self):
        return Article.objects.filter(tegs__in=self.tegs.all())[:2]

    def get_comment(self):
        return self.comment_set.all()

    def __str__(self):
        return self.title

class Video(models.Model):
    video_type = models.CharField(max_length=60)
    video_url = models.CharField(max_length=100)
    video_thumb = models.ImageField(upload_to='thumbnails/',null=True,blank=True)

    def __str__(self):
        return self.video_type

class LatestVideo(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='latestvideo/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class SportLight(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='sportlights/')
    author_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)
    description = models.TextField()
    tegs = models.ManyToManyField(Teg)
    is_actives = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_display = models.BooleanField(default=False)
    is_celebrity_news = models.BooleanField(default=False)

    @property
    def get_short_desc(self):
        return self.description[:100]
    def get_short_desc2(self):
        return self.description[:60]
    def get_short_desc3(self):
        return self.description[:20]
    def get_short_title(self):
        return self.title[:25]
    def get_short_title2(self):
        return self.title[:15]
    def get_sportlight_related_posts(self):
        return SportLight.objects.filter(is_active=True, tegs__in=self.tegs.all())[:2]
    def get_middleNews_related_posts(self):
        return SportLight.objects.filter(is_display=True, tegs__in=self.tegs.all())[:2]
    def get_celebrityNews_related_posts(self):
        return SportLight.objects.filter(is_celebrity_news=True, tegs__in=self.tegs.all())[:2]
    def __str__(self):
        return self.title
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username}:{self.id}"

class Contact(models.Model):
    message = models.TextField(blank=True,null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)

    def __str__(self):
        return self.name
class AboutUs(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(null=True, blank=True)
    desc2 = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.name