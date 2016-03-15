
from django.db import models

class User(models.Model):

    user_name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = True
        db_table = 'user'
        ordering = ('user_name',)

class Category(models.Model):

    category_id = models.CharField(max_length=255, blank=True)
    category_name = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = True
        db_table = 'category'
        ordering = ('category_name',)


class Task(models.Model):
    task_name = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = True
        db_table = 'task'
        ordering = ('task_name',)

