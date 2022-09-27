import json
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","_project.settings")
django.setup()

from pid.models import ProdejniMisto, OteviraciDoba, Dny, TypProdejnihoMista

cesta = r'pointsOfSale.json'

with open(cesta, encoding='utf-8') as file:
    data = json.load(file)
    for misto in data:
        prodejni_misto = ProdejniMisto.objects.update_or_create(
            interni_id=["id"],
            defaults=dict(
                typ=misto["type"],
                nazev=misto["name"],
                adresa=misto["address"],
                lat=misto["lat"],
                lon=misto["lon"],
            )
        )

        for doba in misto['openingHours']:
            print(doba['from'])
            print(doba['to'])
            print(doba['hours'])

