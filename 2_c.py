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
TAI = 0 + 37
#print("TAI: 06:02:37")
TT = 37 + 32.183
print("TT => 06:03:09.184")


