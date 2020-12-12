"""GPS haftasını ve gününü hesaplayınız!"""
"""Tarih: 18.11.2020; Saat: 06:02:00"""
from math import *

y = 2020
m = 11
d = 18
h = 6
minute = 2
second = 0
"""y = int(input("Yıl: "))
m = int(input("Ay: "))
d = int(input("Gün: "))
h = int(input('Saat: '))
minute = int(input('Dakika: '))
second = int(input('Saniye: '))"""
# Eğer ay değeri (m) küçük eşit 2 olursa m + 12 ve y - 1 işlemi uygulanır
if m <= 2:
    m = m + 12
    y = y - 1
# Jülyen günü hesabı
JD = floor(365.25 * y) + floor(30.6004 * (m + 1)) + d + ((h + minute/60 + second/3600) / 24) + 1720981.5
print("Jülyen günü: {:.4f}" .format(JD))
# GPS haftası hesabı
GW = floor((JD - 2444244.5) / 7)
print("GPS haftası: ", GW)



