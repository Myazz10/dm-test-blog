from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField  # pip install django-ckeditor


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('blog-home')

    def __str__(self):
        return f'{self.name.title()}'

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Post(models.Model):
    title = models.CharField(max_length=100)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    title_tag = models.CharField(max_length=100, default="Moi's Blog!")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='categories')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(blank=True, null=True)
    snippet = models.CharField(max_length=255)
    # content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    # After the user adds a post this method will redirect them to the post details page.
    def get_absolute_url(self):
        # return reverse('blog-home')  # --> This will return the user to the home page.
        return reverse('post-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.title.title()} | {self.author.username.title()}'


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField()
    date_made = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.post.id)])

    def __str__(self):
        return f'{self.post.title} - {self.name}'
