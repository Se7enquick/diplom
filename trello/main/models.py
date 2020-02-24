from django.db import models
from django.contrib.auth.models import User


class Status(models.Model): 
    name = models.CharField(max_length = 20)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name  


class Task(models.Model):
    article = models.CharField(max_length = 100, default = 1)
    status = models.ForeignKey(Status, on_delete = models.CASCADE, default = 1)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator', default = 1)
    performer = models.ForeignKey(User, on_delete = models.CASCADE, related_name='performer', default = 1)
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.article

