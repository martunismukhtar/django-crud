from django.shortcuts import render

from .models import Post

# Create your views here.
def index(request):
    pass
    # posts = Post.objects.all()
    # context = {
    #     'judul':'Python',
    #     'keterangan':'Belajar Python',
    #     # 'posts': posts
    # }
    # print (context)
    return render(request, 'blog.html')

def tentang(request):
    return render(render, 'blog/index.html')

def recent(request, **params):
    print(params)
    return render(request, 'blog.html')

def ab(request):
    return render(request, 'blog/about.html')

def tentangkami(request):
    return render(request, 'blog/about.html') 