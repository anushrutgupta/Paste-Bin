from django.db import models

class Paste(models.Model):
    title = models.CharField(max_length=30,null=True,blank=True)
    text = models.TextField()
    time = models.DateTimeField(auto_now=True)
    url_key = models.CharField(max_length = 10)
    def __unicode__(self):
        return self.title
