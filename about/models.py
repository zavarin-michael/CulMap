from django.db import models

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    id_mark = models.IntegerField(default='-1')
    username = models.TextField(default='NOT NULL')
    comment = models.TextField(default='NOT NULL')