from django.shortcuts import render, redirect, get_object_or_404
from .forms import PelangganForm
from .models import Pelanggan
from django.http import HttpResponse, HttpResponseRedirect

from django.core.paginator import Paginator

# Create your views here.
def index(request):
    data = Pelanggan.objects.all().order_by('-id')
    
    paginator = Paginator(data, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    content = {
        'judul':'Daftar Pelanggan',
        'data':page_obj
    }

    return render(request, 'pelanggan/index.html', content)

def formAdd(request):
    pass
    # form = PenerbitForm()
    # content = {
    #     'url':'/book/store/',
    #     'form':form
    # }
    # return render(request, 'book/form.html', content)

def formEdit(request, id):
    pass
    pelanggan = Pelanggan.objects.get(id=id)

    form = PelangganForm(instance=pelanggan)
    content = {
        'url':'/pelanggan/update/'+str(id),
        'form':form
    }
    return render(request, 'pelanggan/form.html', content)

def store(request):
    form = PelangganForm(request.POST or None)
    form.save()
    print(form)
    return redirect(index)

def update(request, id):
    # penerbit = Penerbit.objects.get(id=id)
    # f = PenerbitForm(request.POST, instance=penerbit)
    # f.save()
    return redirect(index)

def delete (request, id):
    pass
    # print(request.POST.cl)
    # penerbit = get_object_or_404(Penerbit, id=id).delete()
    # return HttpResponse(penerbit)