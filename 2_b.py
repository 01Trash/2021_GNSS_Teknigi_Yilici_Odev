"""Tüm GNSS sistemlerinin zaman (epok) bilgisini hesaplayınız!"""
"""Tarih: 18.11.2020; Saat: 06:02:00"""
from math import *

saat = 6
dakika = 2
saniye = 0
"""saat = int(input("Saat: "))
dakika = int(input("Dakika: "))
saniye = int(input("Saniye: "))"""

#GPS = UTC + 18 saniye
saat = saat + 0
dakika = dakika + 0
saniye = saniye + 18
if saniye >= 60:
    saniye = saniye % 60
    dakika = dakika + 1
print("GPS => {:.0f}:{:.0f}:{:.0f}" .format(saat, dakika, saniye))

#GLONASS = UTC + 3 saat
saat = saat + 3
dakika = dakika + 0
saniye = saniye + 0
print("GLONASS => {:.0f}:{:.0f}:{:.0f}" .format(saat, dakika, saniye))

#BEIOU = UTC + 4 saniye
saat = saat + 0
dakika = dakika + 0
saniye = saniye + 4
if saniye >= 60:
    saniye = saniye % 60
    dakika = dakika + 1
print("BEIOU => {:.0f}:{:.0f}:{:.0f}" .format(saat, dakika, saniye))

#GALILEO = UTC + 18 saniye
saat = saat + 0
dakika = dakika + 0
saniye = saniye + 18
if saniye >= 60:
    saniye = saniye % 60
    dakika = dakika + 1
print("GALILEO => {:.0f}:{:.0f}:{:.0f}" .format(saat, dakika, saniye))

