
from django.db import models

class User(models.Model):
    user_name = models.TextField()
    email = models.EmailField()

    class Meta:
        db_table = 'user'
        ordering = ('user_name',)

class Category(models.Model):
    category_id = models.IntegerField()
    category_name = models.TextField()

    class Meta:
        db_table = 'category'
        ordering = ('category_name',)


class Task(models.Model):
    task_name = models.TextField()

    class Meta:
        db_table = 'task'
        ordering = ('task_name',)

