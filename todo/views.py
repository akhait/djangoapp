# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *


class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        return Task.objects.order_by('-priority')


class DetailView(generic.DetailView):
    model = Task
    template_name = 'todo/detail.html'


def done(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if task.is_completed():
        return render(request, 'todo/detail.html', {
            'task': task,
            'error_message':"Can't complete a task that's alreadycompleted!",
        })
    else:
        task.complete()
        return HttpResponseRedirect(reverse('todo:detail', args=(task.id,)))
