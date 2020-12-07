"""Gerçek yıldız zamanı hesaplayınız!"""
"""Tarih: 18.11.2020; Saat: 06:02:00"""
from math import *

saat = 6
dakika = 2
saniye = 0
"""saat = int(input("Saat: "))
dakika = int(input("Dakika: "))
saniye = int(input("Saniye: "))"""

#GMT = 06:02:00 - 3 saat => GMT = 03:02:00
#GMST0 = 03:49:58.857
#Delta_R = 29.9 saniye
"""GMST = GMT - 12 + (GMST0 + 12) + Delta_R"""
GMST0_saat = 3
GMST0_dakika = 49
GMST0_saniye = 58.857
Delta_R = 29.9
GMST_saat = saat + GMST0_saat
GMST_dakika = dakika + GMST0_dakika
GMST_saniye = saniye + GMST0_saniye + Delta_R
if GMST_saniye >= 60:
    GMST_saniye = GMST_saniye % 60
    GMST_dakika = GMST_dakika + 1
if GMST_dakika >= 60:
    GMST_saat = GMST_saat % 60
print("GMST => {:.0f}:{:.0f}:{:.3f}" .format(GMST_saat, GMST_dakika, GMST_saniye))

