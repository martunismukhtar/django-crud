from django.shortcuts import render, redirect, get_object_or_404
from .forms import PenerbitForm
from .models import Penerbit, Book
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
# from django.views.generic import CreateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from django.core.paginator import Paginator

from django.views import View

# Create your views here.
# def index(request):
#     penerbit = Penerbit.objects.all().order_by('-id')
    
#     paginator = Paginator(penerbit, 25)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     content = {
#         'judul':'Belajar python',
#         'penerbit':page_obj
#     }

#     return render(request, 'book/index.html', content)

# def formAdd(request):
#     form = PenerbitForm()
#     content = {
#         # 'url':"{% url \"simpan\" %}",
#         'url':'/book/store/',
#         'form':form
#     }
#     return render(request, 'book/form.html', content)

# def formEdit(request, id):
#     penerbit = Penerbit.objects.get(id=id)

#     form = PenerbitForm(instance=penerbit)
#     content = {
#         'url':'/book/update/'+str(id),
#         'form':form
#     }
#     return render(request, 'book/form.html', content)

# def store(request):
#     form = PenerbitForm(request.POST or None)
#     form.save()
#     print(form)
#     return redirect(index)

# def update(request, id):
#     penerbit = Penerbit.objects.get(id=id)
#     f = PenerbitForm(request.POST, instance=penerbit)
#     f.save()
#     return redirect(index)

# def delete (request, id):
    # print(request.POST.cl)
    # penerbit = get_object_or_404(Penerbit, id=id).delete()
    # return HttpResponse(penerbit)

class IndexClassView(View):
    # pass
    template = 'penerbit/index.html'
    content = {
        # 'judul':'Belajar python',
        # 'penerbit':page_obj
    }
    def get(self, request, id=None):
        self.content['form'] = PenerbitForm()

        if id!=None:
            penerbit = Penerbit.objects.get(id=id)
            self.content['form'] = PenerbitForm(instance=penerbit)
        else:    
            self.content['penerbit'] = Penerbit.objects.all()

        return render(request, self.template, self.content)

    def post(self, request):
        form = PenerbitForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/penerbit.php/')

        return render(request, self.template, self.content)

    def put(self, request, id=None):
        penerbit = Penerbit.objects.get(id=id)
        f = PenerbitForm(request.POST, instance=penerbit)
        f.save()
        return HttpResponseRedirect('/penerbit.php/')

        
class PenerbitListView(ListView):
    template_name = 'penerbit/index.html'
    queryset = Penerbit.objects.all()
    context_object_name = 'penerbit'

class BookCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': PenerbitForm()}
        return render(request, 'book/form.html', context)

    def post(self, request, *args, **kwargs):
        form = PenerbitForm(request.POST)
        if form.is_valid():
            book = form.save()
            book.save()
            return HttpResponseRedirect(reverse_lazy('books:detail', args=[book.id]))
        return render(request, 'book/form.html', {'form': form})