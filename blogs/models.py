from django.db import models
from django.template.defaultfilters import slugify
from django.utils.timezone import now
from djrichtextfield.models import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='blogs' , null=True , blank=True)
    slug = models.SlugField(editable=False)
    article = RichTextField(null=True , blank=True)
    podcast = models.TextField( null=True , blank=True)
    meta_keywords = models.TextField(default="")
    meta_description = models.TextField(default="")
    meta_title = models.TextField(default="")
    pub_date = models.DateField(default=now )
    title_youtube1 = models.CharField(max_length=50, null=True, blank=True)
    brief_youtube1 = models.CharField(max_length=100, null=True, blank=True)
    image_youtube1 = models.ImageField(upload_to="othersvideoimage", null=True, blank=True)
    video_link_youtube1 = models.CharField(max_length=100,null=True,blank=True)
    
    # podcast = models.
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
class Blog_Page(models.Model):
    top_heading = models.CharField(max_length=200 , default="")
    paragraph = models.TextField(default="")
    blog_heading = models.CharField(max_length=200)
    others_heading = models.CharField(max_length=200)
    shorts_heading = models.CharField(max_length=200)
    content = RichTextField(null=True  , blank = True)
    meta_keywords = models.TextField(default="")
    meta_description = models.TextField(default="")
    meta_title = models.TextField(default="")

class Newsletter_Subscription(models.Model):
    email = models.EmailField( max_length=200 , unique=True)
    def __str__(self):
        return self.email