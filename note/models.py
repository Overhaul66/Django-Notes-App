from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Note(models.Model):
  title = models.CharField(max_length=255)
  content = models.TextField()
  tags = models.ManyToManyField('Tag')
  slug = models.SlugField(null=False)
  date_created = models.DateTimeField(auto_now=True)
  
  def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super().save(*args, **kwargs)
    
  def get_absolute_url(self):
    return reverse('note', kwargs={
      'slug':self.slug,
      'pk':self.pk
    } )
  
  def __str__(self):
    return self.title
  
class Tag(models.Model):
  tag_name = models.CharField(max_length=100, unique=True)
  slug = models.SlugField(null=False)
  
  def save(self, *args, **kwargs):
    self.slug = slugify(self.tag_name)
    super().save(*args, **kwargs)
  
  def __str__(self):
    return self.tag_name
  