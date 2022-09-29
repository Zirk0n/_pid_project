from django.shortcuts import render
from django.views import generic
from .models import ProdejniMisto

class ListProdejniMisto(generic.ListView):
    model = ProdejniMisto


class DetailProdejniMisto(generic.DetailView):
    model = ProdejniMisto
    slug_field = "interni_id"