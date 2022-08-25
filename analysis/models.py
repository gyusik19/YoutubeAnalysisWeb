from django.db import models


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=20)


class Content(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    timeStart = models.IntegerField()
    timeEnd = models.IntegerField()
    content = models.TextField()
