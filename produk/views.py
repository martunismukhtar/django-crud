from .models import Produk
from .forms import ProdukForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from django.core.paginator import Paginator

from django.views import View

class ProdukList(ListView):
    template_name = 'produk/index.html'
    model = Produk
    context_object_name = 'list'
    # print (model)
    # paginate_by = 15 

class ProdukCreate(CreateView):
    model = Produk
    form_class = ProdukForm
    # fields = "__all__"
    success_url = '/produk.php/'
    template_name = "produk/form.html"

class ProdukUpdate(UpdateView):
    model = Produk
    form_class = ProdukForm
    success_url = '/produk.php/'
    template_name = "produk/form.html"

class ProdukDelete(DeleteView):
    model = Produk
    success_url = '/produk.php/'
    # template_name = "produk/form.html"
    
    def get_object(self, qs):
        obj = super(FooView, self).get_object(qs)
        if obj.can_delete():
            return obj

    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
        # self.object.soft_delete()
        # return HttpResponseRedirect(self.get_success_url())