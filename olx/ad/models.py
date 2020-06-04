from django.db import models
from django.contrib.auth.models import User


class Ad(models.Model):
  code = models.CharField(max_length=12, blank=True, null=True)
  owner = models.ForeignKey(User, related_name='ad_owner', on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now=True)
  update_at = models.DateTimeField(auto_now_add=True)
  image = models.ImageField(upload_to='ad/')
  content = models.TextField(max_length=1000)
  price = models.IntegerField(default=0)
  category = models.ForeignKey('Category', limit_choices_to = {'main_category': True},related_name='add_category', on_delete=models.CASCADE) ## reltion -> main

  def save(self, *args, **kwargs):
     self.code = f'##{str(self.owner.id).ljust(10, "0")}'
     super().save(*args, **kwargs)

  def __str__(self):
    return self.name


class AdImages(models.Model):
  ad = models.ForeignKey(Ad, related_name='ad_images', on_delete=models.CASCADE)
  images = models.ImageField(upload_to='ad_images/')




class Category(models.Model):
  name = models.CharField(max_length=50)
  main_category = models.ForeignKey('self', limit_choices_to = {'main_category': None}, related_name='maincategory', on_delete=models.CASCADE, blank=True, null=True) ## reltion -> sub category
  def __str__(self):
    return self.name
