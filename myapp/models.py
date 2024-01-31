from django.db import models

# Create your models here.
class AnnounceText(models.Model):
    text=models.CharField(max_length=500)
    # courseoutcome=models.CharField(max_length=100)
    # knowledge_level=models.CharField(max_length=5,default='K1')
    # course_code=models.CharField(max_length=15)
class StoreImages(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/',blank=True) 
    boolval=models.IntegerField(default=0)
class Dummy(models.Model):
    val=models.IntegerField(default=1)
class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')    
    boolval=models.IntegerField(default=0)
