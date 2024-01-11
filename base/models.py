from django.db import models
import uuid

# Create your models here.
    
class Service(models.Model):
    Title = models.CharField(max_length=200, null=True, blank=True) 
    service_image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.Title
    

class Employee(models.Model):
    service = models.ForeignKey(Service, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, null=True, blank=True)
    skill = models.CharField(max_length=200, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True)
    social_facebook = models.CharField(max_length=200, null=True, blank=True)
    social_linked_in = models.CharField(max_length=200, null=True, blank=True)
    social_twitter = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.name
    
class Price(models.Model):
    price_service_owner = models.ForeignKey(Service, blank=True, null=True, on_delete=models.SET_NULL)
    price_service = models.CharField(max_length=200, null=True, blank=True)
    price = models.IntegerField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.price_service
    
class why_us(models.Model):
    img1 = models.ImageField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    sub_title = models.TextField(null=True, blank=True)
    brief = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return "Why Us"
    
class About(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    text1 = models.CharField(max_length=200, null=True, blank=True)
    text2 = models.CharField(max_length=200, null=True, blank=True)
    text3 = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return "About"
    
    
    
    
    
    