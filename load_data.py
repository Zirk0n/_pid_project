import json
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","_project.settings")
django.setup()

from pid.models import ProdejniMisto, OteviraciDoba, Dny, TypProdejnihoMista

cesta = r'pointsOfSale.json'

with open(cesta, encoding='utf-8') as file:
    data = json.load(file)
    for misto in data:
        prodejni_misto,created = ProdejniMisto.objects.update_or_create(
            interni_id=misto["id"],
            defaults=dict(
                typ=misto["type"],
                nazev=misto["name"],
                adresa=misto["address"],
                lat=misto["lat"],
                lon=misto["lon"],
            )
        )

        for doba in misto['openingHours']:
            casy = doba["hours"].split(",")
            for cas in casy:
                cas_od, cas_do = cas.split("-")
                if cas_do == "24:00":
                    cas_do = "23:59:59"

                oteviraci_doba, created = OteviraciDoba.objects.get_or_create(
                    den_od=doba["from"],
                    den_do=doba["to"],
                    cas_od=cas_od,
                    cas_do=cas_do,
                )
                prodejni_misto.otviraci_doby.add(oteviraci_doba)