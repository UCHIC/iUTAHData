from django.db import models
from tinymce import models as tinymce_models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    content = models.TextField(max_length=20000) #tinymce_models.HTMLField()#forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30})) #Use the WYSIWYG editor in this field.
    def __unicode__(self):
        return self.title

class Subpage(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    url_visible = models.BooleanField()
    content = models.TextField(max_length=20000)#tinymce_models.HTMLField() #forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30})) #Use the WYSIWYG editor in this field.
    pages = models.ForeignKey(Page)
    def __unicode__(self):
        return self.title