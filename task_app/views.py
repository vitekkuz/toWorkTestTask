from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'text': 'Hello!'}
    return render(request, 'task_app/base.html', context=context)