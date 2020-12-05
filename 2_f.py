"""Kutup hareketi hesaplayınız!"""
"""Tarih: 18.11.2020; Saat: 06:02:00"""
from math import *

y = 2020
m = 11
d = 18
h = 6
"""y = int(input("Yıl: "))
m = int(input("Ay: "))
d = int(input("Gün: "))
h = int(input('Saat: '))"""
# Eğer ay değeri (m) küçük eşit 2 olursa m + 12 ve y - 1 işlemi uygulanır
if m <= 2:
    m = m + 12
    y = y - 1
# Jülyen günü hesabı JD
JD = floor(365.25 * y) + floor(30.6004 * (m + 1)) + d + (h / 24) + 1720981.5
#print("Jülyen günü: ", JD)

#t hesabı
t = (JD - 2451545.0) / 36525
print("t: ", t)

#Kutup Hareket Matrisi
W_t = 0
