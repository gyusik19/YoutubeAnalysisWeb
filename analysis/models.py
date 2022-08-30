from django.db import models


# Create your models here.
class Video(models.Model):
    # video = models.FileField(null=None)
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    link = models.URLField(max_length=50)

    def __str__(self):
        return self.title

class Content(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    timeStart = models.IntegerField()
    timeEnd = models.IntegerField()
    content = models.TextField()
    type = models.CharField(max_length=20, null=True)
    # value = models.JSONField(null=None)

    def __str__(self):
        return self.content
