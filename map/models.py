from django.db import models


class MapMarks(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='', default='Color_Bars_HD_16x9.tif', blank=True)
    position_x = models.FloatField(default="")
    position_y = models.FloatField(default="")
    name = models.CharField(default="", max_length=64)
    comment = models.TextField(default="", blank=True)
    id_comment = models.TextField(default="", blank=True, null=True)
