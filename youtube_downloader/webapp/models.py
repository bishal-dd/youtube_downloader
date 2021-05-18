from django.db import models


class Video(models.Model):
    search_link = models.CharField(max_length=1000, null=False)
