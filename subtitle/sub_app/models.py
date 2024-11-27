from django.db import models

class MovieInfo(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    summery = models.TextField()
    poster = models.ImageField(upload_to='poster')

    def __str__(self):
        return self.title
