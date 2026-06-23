from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class Position(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    class Meta:
        ordering = ('first_name',)


class TaskType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


    class Meta:
        ordering = ('name',)


class Task(models.Model):


    class PriorityChoices(models.TextChoices):
        URGENT = "Urgent", "Urgent"
        HIGH = "High", "High"
        MEDIUM = "Medium", "Medium"
        LOW = "Low", "Low"


    name = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)

    priority = models.CharField(
        max_length=10,
        choices=PriorityChoices,
        default=PriorityChoices.MEDIUM,
    )

    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    assignees = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='tasks'
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
