# -*- coding: utf-8 -*-
from datetime import timedelta
from django.utils import timezone
from django.test import TestCase
from .models import Task

class TaskModelTests(TestCase):

    def test_is_complete(self):
        due = timezone.now() + timedelta(days=7)
        task = Task(due_date=due)
        self.assertIs(task.is_completed(), False)

    def test_complete_task(self):
        due = timezone.now() + timedelta(days=7)
        task = Task(due_date=due)
        task.complete()
        self.assertIs(task.is_completed(), True)

    #TODO: should raise exception instead
    def test_complete_completed_task(self):
        due = timezone.now() + timedelta(days=7)
        task = Task(due_date=due, completed=True)
        task.complete()
        self.assertIs(task.is_completed(), True)
