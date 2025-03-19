from django.db import models

class Partner(models.Model):
    image = models.ImageField(upload_to="")
    url = models.CharField(max_length=255, blank=True)
    order = models.IntegerField(default=1)

class Company(models.Model):  
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="")
    image = models.ImageField(upload_to="")
    short_description = models.CharField(max_length=255)

class CompanyAchievements(models.Model):
    year = models.IntegerField(default=1)    
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to="")
    company = models.ForeignKey(
        Company, related_name="company_achievements", on_delete=models.CASCADE
    )

class Region(models.Model):  
    name = models.CharField(max_length=255)    
    number = models.IntegerField(default=1)
    company = models.ForeignKey(
        Company, related_name="company_region", on_delete=models.CASCADE
    )

class Achievements(models.Model): 
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="")
    description = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="")
    order = models.IntegerField(default=1)

class Gallery(models.Model): 
    title = models.CharField(max_length=255)
    url = models.ImageField(upload_to="")
    order = models.IntegerField(default=1)
