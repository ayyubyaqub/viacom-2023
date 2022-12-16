from django.db import models
from django.template.defaultfilters import slugify
from djrichtextfield.models import RichTextField



class Story_page(models.Model):
    heading = models.CharField(max_length=200)
    paragraph = RichTextField()
    meta_keywords = models.TextField(default="")
    meta_description = models.TextField(default="")
    meta_title = models.TextField(default="")

class Story(models.Model):
    image = models.ImageField(upload_to='story' , null=True , blank=True)
    slug = models.SlugField(editable=False)
    company_name = models.CharField(max_length=200)
    card_description = models.TextField()
    problem = models.TextField()
    solution = models.TextField()
    result = models.TextField()
    meta_keywords = models.TextField(default="")
    meta_description = models.TextField(default="")
    meta_title = models.TextField(default="")
    video_link = models.URLField(default="#")

    # yt_link = models.URLField(default="https://www.youtube.com/embed/zlEb-Y9OOpQ")

    # podcast = models.
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.company_name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.company_name

