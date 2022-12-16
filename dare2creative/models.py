from django.db import models
from django.template.defaultfilters import slugify
from django.utils.timezone import now

class D2C_Page(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=500)
    meta_keywords = models.TextField(default="")
    meta_description = models.TextField(default="")
    meta_title = models.TextField(default="")

class D2C_Posters(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="d2c")
    url = models.URLField(default="#")
    d2c = models.ForeignKey(D2C_Page , on_delete= models.PROTECT)

class Super_Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default="" , blank=True , null =  True)
    
    def __str__(self):
        return self.title
    
class Category(models.Model):
    logo = models.ImageField(upload_to="d2c")
    text = models.CharField(max_length=200)
    super_category = models.ForeignKey(Super_Category , on_delete=models.PROTECT)
    slug = models.SlugField(editable=False)
    meta_keywords = models.TextField(default="")
    meta_description = models.TextField(default="")
    meta_title = models.TextField(default="")
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.text)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.text


class Sub_Category(models.Model):
    heading_image = models.ImageField(upload_to="d2c/category")
    image = models.ImageField(upload_to="d2c/category")
    registration_deadline = models.DateTimeField(default=now)
    start_date = models.DateTimeField(default=now)
    end_date = models.DateTimeField(default=now)
    last_update = models.DateTimeField(default=now)
    location = models.TextField()
    event = models.CharField(max_length=200)
    fee = models.CharField(max_length=200)
    isFeautered = models.BooleanField(default=False)
    company = models.CharField(max_length=300 , default="")
    prize_money = models.IntegerField(default=0)
    participation = models.IntegerField(default=1)
    category = models.ForeignKey(Category , models.PROTECT)
    eligibility = models.TextField()
    register_url = models.URLField(default="#")
    slug = models.SlugField(editable=False)
    meta_keywords = models.TextField(default="")
    meta_description = models.TextField(default="")
    meta_title = models.TextField(default="")
    def __str__(self):
        return self.event
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.event)
        return super().save(*args, **kwargs)


# class Recent(models.Model):


