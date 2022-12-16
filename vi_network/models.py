from django.db import models

class Vi_Network_Page(models.Model):
    meta_keywords = models.TextField(default="")
    meta_description = models.TextField(default="")
    meta_title = models.TextField(default="")



class Vi_Network(models.Model):
    title = models.CharField(max_length=200)
    paragraph = models.TextField()
    serial_number = models.IntegerField(default=0)
    def __str__(self) :
        return self.title

class Vi_Network_card(models.Model):
    parent = models.ForeignKey(Vi_Network , on_delete=models.CASCADE)
    heading = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(default='#')
    image = models.ImageField(upload_to="vi_network")

