from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField

# Create your models here.


# catagory 
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    url = models.CharField(max_length=100)
    img = models.ImageField(upload_to='catagoryimg')
    date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    #to show images of category in admin
    def image_show(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px; border-radius:50%" />.'.format(self.img))


#  posts
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = HTMLField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE) # post konse catagory me jayegi or jab catagory delete ho to post v delete ho jaye
    img = models.ImageField(upload_to='postimg')

    def __str__(self):
        return self.title