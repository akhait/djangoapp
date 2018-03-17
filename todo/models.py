# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Task(models.Model):
    summary = models.CharField(max_length=60)
    due_date = models.DateTimeField()
    PRIORITIES = (
        (0, 'urgent'),
        (1, 'high'),
        (2, 'medium'),
        (3, 'low'),
    )
    priority = models.IntegerField(
        choices=PRIORITIES,
        default=3,
    )
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.summary

    def is_completed(self):
        return self.completed

    #TODO: raise exception if task is already completed
    def complete(self):
        self.completed = True
        self.save()
