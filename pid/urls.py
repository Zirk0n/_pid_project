from django.urls import path
from .views import ListProdejniMisto, DetailProdejniMisto, error_view, redirect_301, redirect_302, kontaktni_formular
from django.views.decorators.cache import cache_page

app_name = "pid"

cache_60_sec = cache_page(60*60*24)

urlpatterns = [
    path("prodejni-mista/", ListProdejniMisto.as_view(), name="ListProdejniMisto"),
    path("prodejni-mista/<slug:slug>/", DetailProdejniMisto.as_view(), name="DetailProdejniMisto"),
    path("test-error/", error_view),
    path("redirect-301/", redirect_301),
    path("redirect-302/", redirect_302),
    path("formular/", kontaktni_formular, name="kontaktni_formular"),
]