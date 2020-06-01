from django.db import models

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    User_name = models.TextField(default='NOT NULL')
    comment = models.TextField(default='NOT NULL')