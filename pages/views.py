from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    name = 'rikuta'
    context = {'name': name}
    return render(request, 'pages/index.html', context)


def profile(request):
    return HttpResponse('Profile!')


def jobs(request):
    return HttpResponse('私の仕事は〇〇です｡')


def hobby(request):
    return HttpResponse('My hobby is programming')

