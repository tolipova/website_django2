from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category
    
class MainSilder(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_info/')
    date = models.DateTimeField(auto_now=False)
    title = models.CharField(max_length=255)
    info = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class StartSlider(models.Model):
    image = models.ImageField(upload_to='user_info/')
    info = models.CharField(max_length=255)

class Posts(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now=False)
    image = models.ImageField(upload_to='user_info/')
    info = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Featured(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='user_info/')
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now=False)
    info = models.TextField()

    def __str__(self):
        return self.name
    
class Main_Popular(models.Model):
    image = models.ImageField(upload_to='user_info/')
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=False)
    little_info = models.CharField(max_length=255)
    big_info = models.TextField()

    def __str__(self):
        return self.title
class Popular(models.Model):
    image = models.ImageField(upload_to='user_info/')    
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    info = models.CharField(max_length=255)

class Main_Latest(models.Model):
    image = models.ImageField(upload_to='user_info/')
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=False)
    little_info = models.CharField(max_length=255)
    big_info = models.TextField()

        
class Latest(models.Model):
    image = models.ImageField(upload_to='user_info/')    
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    info = models.CharField(max_length=255)

class Follow(models.Model):
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    you_tube = models.CharField(max_length=255)
    vimeo = models.CharField(max_length=255)

class NewsLetter(models.Model):
    info = models.TextField()
    button = models.CharField(max_length=255)
    small_info = models.CharField(max_length=255)

class Addstart(models.Model):
    image = models.ImageField(upload_to='user_info/') 

class Tranding(models.Model):
    image = models.ImageField(upload_to='user_info/')
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=False)   
    info = models.CharField(max_length=255)