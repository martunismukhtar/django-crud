from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    context = {
        'judul':'Python',
        'keterangan':'Belajar Python',
        # 'posts': posts
    }
    print (context)
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse('About/Belajar python')