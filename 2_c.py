"""Yersel (TT) zaman bilgisini hesaplayınız!"""
"""Tarih: 18.11.2020; Saat: 06:02:00"""
from math import *

saat = 6
dakika = 2
saniye = 0
"""saat = int(input("Saat: "))
dakika = int(input("Dakika: "))
saniye = int(input("Saniye: "))"""

"""TT = TAI + 32.184 saniye
TAI = UTC + 37 saniye"""
saat = saat + 0
dakika = dakika + 0
saniye = saniye + 37
if saniye >= 60:
    saniye = saniye % 60
    dakika = dakika + 1
#print("TAI => {:.0f}:{:.0f}:{:.0f}" .format(saat, dakika, saniye))
TAI = saniye

saat = saat + 0
dakika = dakika + 0
saniye = TAI + 32.183
if saniye >= 60:
    saniye = saniye % 60
    dakika = dakika + 1
print("TT => {:.0f}:{:.0f}:{:.3f}" .format(saat, dakika, saniye))


