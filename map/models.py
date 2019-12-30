from django.db import models


class MapMarks(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(default="")
    position_x = models.FloatField(default="")
    position_y = models.FloatField(default="1")
    name = models.CharField(default="", max_length=64)
    comment = models.TextField(default="")
