from django.db import models

#Footer 
class Footer_Columns(models.Model):
    title = models.CharField(max_length=200)
    email = models.EmailField()
    call_number = models.CharField(max_length=20)
    whatsup_number = models.CharField(max_length=20)
    telephone_number = models.CharField(max_length=20)




#Navbar