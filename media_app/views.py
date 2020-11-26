from django.shortcuts import render

from .models import Media
# Create your views here.

def index(request):
    media = Media.objects.all()
    content = {
        'judul':'python',
        'media':media
    }
    print (content)
    return render(request, 'media.html', content)