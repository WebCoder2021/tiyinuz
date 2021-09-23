from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class NewsType(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class New(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=500, blank=True)
    content = models.TextField(blank=True)
    img = models.ImageField(upload_to='image/')
    publeshed = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    news_type = models.ForeignKey(NewsType, on_delete=models.CASCADE)
    views = models.SmallIntegerField(default=0)
    is_view = models.BooleanField(default=True)

    def __str__(self):
        return self.title



