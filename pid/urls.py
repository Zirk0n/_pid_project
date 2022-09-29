from django.urls import path
from .views import ListProdejniMisto

app_name = "pid"

urlpatterns = [
    path("prodejni-mista/", ListProdejniMisto.as_view(), name="ListProdejniMisto"),
    path("prodejni-mista/<slug:slug>",views., name=""),
]