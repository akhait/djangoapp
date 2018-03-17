# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
