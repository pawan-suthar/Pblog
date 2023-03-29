from django.shortcuts import HttpResponse, render
from requests import request

from.models import *
# Create your views here.

def home(request):
    # load data from database
    posts = Post.objects.all().order_by('-post_id') #get only 10 posts
    
    categorys = Category.objects.all() #get all category from DB
    data={
        'posts':posts,
        'categorys':categorys
    }
    return render(request, "home.html", data)

def post(request,url):
    post = Post.objects.get(url=url) # read more me post ka full url 
    category = Category.objects.all() #get all category from DB
    return render(request,'posts.html',{'post':post,'category':category}) #jis post prr read more click kiya uska data bhej do

def category(request,url):
    cat = Category.objects.get(url=url)
    pos = Post.objects.filter(cat=cat)
    return render(request, 'category.html',{'pos':pos,'cat':cat})


