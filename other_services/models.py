from email.policy import default
from django.db import models
from django.template.defaultfilters import slugify
from djrichtextfield.models import RichTextField

# Create your models here.
class other_services(models.Model):
    # url = models.URLField(max_length=250)
    serial_number = models.IntegerField(default=0)
    title = models.CharField(max_length=300)
    secondary_title = models.CharField(max_length=200 , default="" , null=True , blank=True )
    outer_image= models.ImageField(upload_to="others")
    inner_image = models.ImageField(upload_to="others/inner_images" , default="" , blank=True  , null =True)
    block_heading = models.CharField(max_length=200 , blank=True , null=True)
    video= models.FileField(upload_to="others/videos" , null=True , blank = True)
    short_description = models.TextField(default="")
    description = RichTextField()
    link = models.URLField(blank=True , null=True)
    slug = models.SlugField(editable=True)
    yt_heading=models.CharField(max_length=100, null=True, blank=True)
    title_youtube1 = models.CharField(max_length=50, null=True, blank=True)
    brief_youtube1 = models.CharField(max_length=100, null=True, blank=True)
    image_youtube1 = models.ImageField(
        upload_to="othersvideoimage", null=True, blank=True)
    video_link_youtube1 = models.CharField(max_length=100,null=True,blank=True)
    title_youtube2 = models.CharField(max_length=50, null=True, blank=True)
    brief_youtube2 = models.CharField(max_length=100, null=True, blank=True)
    image_youtube2 = models.ImageField(
        upload_to="othersvideoimage", null=True, blank=True)
    video_link_youtube2 = models.CharField(max_length=100,null=True,blank=True)
    title_youtube3 = models.CharField(max_length=50, null=True, blank=True)
    brief_youtube3 = models.CharField(max_length=100, null=True, blank=True)
    image_youtube3 = models.ImageField(
        upload_to="othersvideoimage", null=True, blank=True)
    video_link_youtube3 = models.CharField(max_length=100,null=True,blank=True)
    meta_keywords = models.TextField(default="")
    meta_description = models.TextField(default="")
    meta_title = models.TextField(default="")
    sub_image_1=models.ImageField(upload_to="others/sub_images" , blank=True , null=True )
    sub_image_2=models.ImageField(upload_to="others/sub_images" , blank=True , null=True )
    sub_image_3=models.ImageField(upload_to="others/sub_images" , blank=True , null=True )
    sub_image_4=models.ImageField(upload_to="others/sub_images" , blank=True , null=True )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self) :
        return self.title
class other_services_blocks(models.Model):
    other_service = models.ForeignKey( other_services , on_delete=models.CASCADE)
    heading = models.CharField(max_length=200)
    paragraph = models.TextField()


class other_services_page(models.Model):
    heading = models.CharField(max_length=250)
    meta_keywords = models.TextField(default="")
    meta_description = models.TextField(default="")
    meta_title = models.TextField(default="")