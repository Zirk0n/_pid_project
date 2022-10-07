from django.shortcuts import render
from functools import cached_property
from django.views import generic
from .models import ProdejniMisto
from django.shortcuts import redirect, reverse

class ListProdejniMisto(generic.ListView):
    template_name = "pid/prodejnimisto_list.html"
    model = ProdejniMisto

    def get(self,*args, **kwargs):
        return super(ListProdejniMisto,self).get(*args,**kwargs)

    @cached_property
    def moje_hodnota(self):
        print("vracím moje_hodnota")
        return[1,2,3,4,5]

    def html(self):
        return '<a href="#">Toto je můj link</a>'

class DetailProdejniMisto(generic.DetailView):
    model = ProdejniMisto
    slug_field = 'interni_id'

def error_view(request):
    raise ValueError("moje chyba")

def redirect_301(request):
    cesta = reverse("pid:ListProdejniMisto")
    return redirect()

def redirect_302(request):
    cesta = reverse("pid:ListProdejniMisto")
    return redirect(cesta)
