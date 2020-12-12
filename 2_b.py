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
saat_gps = saat + 0
dakika_gps = dakika + 0
saniye_gps = saniye + 18
if saniye_gps >= 60:
    saniye_gps = saniye_gps % 60
    dakika_gps = dakika_gps + 1
print("GPS => {:.0f}:{:.0f}:{:.0f}" .format(saat_gps, dakika_gps, saniye_gps))

#GLONASS = UTC + 3 saat
saat_glonass = saat + 3
dakika_glonass = dakika + 0
saniye_glonass = saniye + 0
if saniye_glonass >= 60:
    saniye_glonass = saniye_glonass % 60
    dakika_glonass = dakika_glonass + 1
print("GLONASS => {:.0f}:{:.0f}:{:.0f}" .format(saat_glonass, dakika_glonass, saniye_glonass))

#BEIOU = UTC + 4 saniye
saat_beiou = saat + 0
dakika_beiou = dakika + 0
saniye_beiou = saniye + 4
if saniye_beiou >= 60:
    saniye_beiou = saniye_beiou % 60
    dakika_beiou = dakika_beiou + 1
print("BEIOU => {:.0f}:{:.0f}:{:.0f}" .format(saat_beiou, dakika_beiou, saniye_beiou))

#GALILEO = UTC + 18 saniye
saat_galileo = saat + 0
dakika_galileo = dakika + 0
saniye_galileo = saniye + 18
if saniye_galileo >= 60:
    saniye_galileo = saniye_galileo % 60
    dakika_galileo = dakika_galileo + 1
print("GALILEO => {:.0f}:{:.0f}:{:.0f}" .format(saat_galileo, dakika_galileo, saniye_galileo))



