from django.shortcuts import render
from .models import *


def index(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    # return HttpResponse("Hello, world. You're at the tasks index.")
    return render(request, 'list.html', context)
