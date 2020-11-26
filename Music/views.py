from django.shortcuts import render

from .models import Album
# Create your views here.

def index(request):
    album = Album.objects.all()
    content = {
        'judul':'python',
        'album':album
    }
    print (content)
    return render(request, 'music/index.html', content)

def formAdd(request):
    if request.method == 'POST' :
        print(request.POST)
    return render(request, 'music/form.html')