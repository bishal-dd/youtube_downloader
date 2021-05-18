from django.shortcuts import render
from .main import Download


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def search_name(request):
    return request.GET.get('search')


def download(request):
    Download(search_name(request)).youtube_video()
    return render(request, 'index.html')


def searchbar(request):
    if request.method == 'GET':
        item = Download(search_name(request)).thumbnail()
        return render(request, 'searchbar.html', {'item': item, 'search': search_name(request)})



