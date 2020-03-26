# Create your models here.
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import auth
from ckeditor_uploader.fields import RichTextUploadingField


class TimeStampedModel(models.Model):
    """Base Model"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children',on_delete=models.PROTECT)

    class Meta:
        unique_together = ('slug', 'parent',)    #enforcing that there can not be two
        verbose_name_plural = "categories"       #categories under a parent with same 
                                                 #slug 

    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.name]                  # post.  use __unicode__ in place of
                                                 # __str__ if you are using python 2
        k = self.parent                          

        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])

class Post(TimeStampedModel):
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name='post',
        verbose_name='글쓴이',
        )
    body = RichTextUploadingField()
    slug = models.SlugField(unique=True)
    category = models.ForeignKey('Category', null=True, blank=True,on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_cat_list(self):           #for now ignore this instance method,
        k = self.category
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent

        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]