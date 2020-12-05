"""Presesyon ve nutasyon matrisi hesaplayınız!"""
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

a = 2306.2181 * t + 0.30188 * t * t + 0.017998 * t * t * t
print("a: ", a)
b = 2004.3109 * t - 0.42665 * t * t - 0.041833 * t * t * t
print("b: ", b)
c = 2306.218 * t + 1.09468 * t * t + 0.018203 * t * t * t
print("c: ", c)

#Presesyon Matrisi
P_t = 0

#Nutasyon Matrisi
N_t = 0



