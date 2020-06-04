from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
# New
from django_currentuser.db.models import CurrentUserField
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)


class Post(models.Model):
  # author = models.ForeignKey(User, on_delete=models.CASCADE, editable=True, default=1)
  created_by = CurrentUserField(editable=False)
  title = models.CharField(max_length=100)
  content = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)
  post_slug = models.SlugField(blank=True, null=True, editable=False)
  image = models.ImageField( upload_to='post/')
  active = models.BooleanField(default=False)


  def save(self, *args, **kwargs):
     self.post_slug = slugify(self.title)
     super(Post, self).save(*args, **kwargs) # Call the real save() method


  def __str__(self):
    return self.title
