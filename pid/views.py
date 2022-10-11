from django.shortcuts import render
from functools import cached_property
from django.views import generic
from .models import ProdejniMisto
from django import forms
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

class KontaktForm(forms.Form):
    jmeno = forms.CharField(max_length=100)
    text = forms.CharField(max_length=100, widget=forms.Textarea, required=False)
    soubor = forms.FileField()



def kontaktni_formular(request):
    form = KontaktForm()
    if request.method == "POST":
        print("tady zpracovávám formulř")
        print(request.POST)
        print(request.FILES)
        form = KontaktForm(request.POST)
        print(form.is_valid())
        return redirect("pid:kontaktni_formular")
    else:
        form = KontaktForm()
        print("tady jen vykresluji formulář")
        print(request.headers)
        response = render(request, "pid/kontaktni-formular.html", context={"form":form})
        response["Set-Cookie"] = "mojeCookie=moje_hodnota_cookie"
        return response

