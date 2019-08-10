from django.shortcuts import render
import subprocess
from .models import Post


def home(request):
    # print('inside home')
    # print('Start parser process')
    # cmd = ['python', 'Parser/test_script.py']
    # subprocess.Popen(cmd).wait()
    # print('ended')
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'ApiWeather/home.html', context=context)


def docs(request):
    print('inside about')
    return render(request, 'ApiWeather/docs.html', {'title': 'Docs'})