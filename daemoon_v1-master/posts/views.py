from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator
from .forms import PostForm
from .models import Post,Category
import datetime
try:
    from django.utils import simplejson as json
except ImportError:
    import json
# Create your views here.

def index(request):
    return render(request,'index.html')

def posts_home(request):
    category_list = list(Category.objects.all())
    category_name = [x.name for x in category_list]
    return render(request,"posts_categories.html",{'categories':category_name})

def posts_list(request,category):
    posts = Post.objects.filter(slug=category)
    return render(request,'posts_list.html',{'posts':posts})

def posts_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/posts/')
    else:
        form = PostForm()
    return render(request,'posts_new.html',{'form':form})

def show_category(request,hierarchy= None):
    category_slug = hierarchy.split('/')
    category_queryset = list(Category.objects.all())
    all_slugs = [ x.slug for x in category_queryset ]
    parent = None
    for slug in category_slug:
        if slug in all_slugs:
            parent = get_object_or_404(Category,slug=slug,parent=parent)
        else:
            instance = get_object_or_404(Post, slug=slug)
            breadcrumbs_link = instance.get_cat_list()
            category_name = [' '.join(i.split('/')[-1].split('-')) for i in breadcrumbs_link]
            breadcrumbs = zip(breadcrumbs_link, category_name)
            return render(request, "posts_detail.html", {'instance':instance,'breadcrumbs':breadcrumbs})

    return render(request,"posts_categories.html",{'post_set':parent.post_set.all(),'sub_categories':parent.children.all()})