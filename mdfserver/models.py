from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=8000) #Use the WYSIWYG editor in this field.
    def __unicode__(self):
        return self.title

class Subpage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=8000) #Use the WYSIWYG editor in this field.
    pages = models.ForeignKey(Page)
    def __unicode__(self):
        return self.title