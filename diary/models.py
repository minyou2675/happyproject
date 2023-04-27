from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return f'{self.name}'
    
class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    
    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return f'/yuneediary/category/{self.name}'

class Post(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=10)
    createdat = models.DateField(auto_now=True)
    updateat = models.DateField(auto_now_add=True)
    content = models.TextField()
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    tag = models.ManyToManyField(Tag,blank=True)
    category = models.ForeignKey(Category,blank=True,null=True,on_delete=models.SET_NULL)

    
    def __str__(self):
        return f'[{self.pk}] [{self.title}]'

    def get_absolute_url(self):
        return f'/yuneediary/{self.pk}/'
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.content}'
    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'
    