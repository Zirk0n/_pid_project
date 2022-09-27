from django.db import models

# Create your models here.
class TypProdejnihoMista:
    ticketMachine = 'ticketMachine'
    trainStation = 'trainStation'
    informationCenter = 'informationCenter'
    ticketOfficeMetro = 'ticketOfficeMetro'
    carrierOffice = 'carrierOffice'
    chipCardDispense = 'chipDardDispense'

    choices = [
        (ticketMachine, ticketMachine),
        (trainStation, trainStation),
        (informationCenter, informationCenter),
        (ticketOfficeMetro, ticketOfficeMetro),
        (carrierOffice, carrierOffice),
        (chipCardDispense, chipCardDispense),



    ]

class ProdejniMisto(models.Model):
    interni_id = models.CharField(max_length=10, db_index=True, unique=True)
    typ = models.CharField(max_length=20)
    nazev = models.CharField(max_length=100)
    adresa = models.CharField(max_length=100)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)



class Dny:
    po = 0
    ut = 1
    st = 2
    ct = 3
    pa = 4
    so = 5
    ne = 6

    choises = [
        (po, 'pondělí'),
        (ut, 'úterý'),
        (st, 'středa'),
        (ct, 'čtvrtek'),
        (pa, 'pátek'),
        (so, 'sobota'),
        (ne, 'neděle'),

    ]


class OteviraciDoba(models.Model):
    den_od = models.PositiveSmallIntegerField(choices=Dny.choises)
    den_do = models.PositiveSmallIntegerField(choices=Dny.choises)
    cas_od = models.TimeField()
    cas_do = models.TimeField(choices=Dny.choises)

class Sluzby():
    pass




class PlatebniMetody():
   pass
