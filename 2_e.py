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
JDs = 0

#t hesabı
t = (JDs - JD) / 36525
#print("t: ", t)
a = 2306.2181 * t + 0.30188 * t * t + 0.017998 * t * t * t
a = a / 3600
#print("a: ", a)
b = 2004.3109 * t - 0.42665 * t * t - 0.041833 * t * t * t
b = b / 3600
#print("b: ", b)
c = 2306.218 * t + 1.09468 * t * t + 0.018203 * t * t * t
c = c / 3600
#print("c: ", c)
#Grad = (Radyan * pi) / 200
a = (a * pi) / 200
b = (b * pi) / 200
c = (c * pi) / 200

#Presesyon Matrisi
Pmatris_1_1 = cos(a) * cos(b) * cos(c) - sin(a) * sin(c)
Pmatris_1_2 = - sin(a) * cos(b) * cos(c) - cos(a) * sin(c)
Pmatris_1_3 = - sin(b) * cos(c)
Pmatris_2_1 = cos(a) * cos(b) * cos(c) + sin(a) * sin(c)
Pmatris_2_2 = - sin(a) * cos(b) * cos(c) + cos(a) * sin(c)
Pmatris_2_3 = - sin(b) * sin(c)
Pmatris_3_1 = cos(a) * sin(b)
Pmatris_3_2 = - sin(a) * sin(b)
Pmatris_3_3 = cos(b)
#Ekrana yazdırma
print("       |   {:f}    {:f}    {:f}  |" .format(Pmatris_1_1, Pmatris_1_2, Pmatris_1_3))
print("P(t) = |   {:f}     {:f}    {:f}  |" .format(Pmatris_2_1, Pmatris_2_2, Pmatris_2_3))
print("       |   {:f}    {:f}     {:f}  |" .format(Pmatris_3_1, Pmatris_3_2, Pmatris_3_3))
print("------------------------------------------------")


#Tu hesabı
Tu = (JD - 2451545.0) / 36525
#print("Tu: ", Tu)
N = (125 + 2 / 60 + 40.280 / 3600) - ((1934 + 8 / 60 + 10.539 / 3600) * Tu) + ((7.455 / 3600) * Tu * Tu * Tu) + ((0.008 / 3600) * Tu * Tu * Tu)
D = (297 + 51 / 60 + 1.307 / 3600) + ((445267 + 6 / 60 + 41.328 / 3600) * Tu) - ((6.891 / 3600) * Tu * Tu) + ((0.019 / 3600) * Tu * Tu * Tu)
F = (93 + 16 / 60 + 18.877 / 3600) + ((483202 + 1 / 60 + 3.137 / 3600) * Tu) - ((13.257 / 3600) * Tu * Tu) + ((0.011 / 3600) * Tu * Tu * Tu)
#Grad = (Radyan * pi) / 200
N = (N * pi) / 200
D = (D * pi) / 200
F = (F * pi) / 200
a = (23 + 26 / 60 + 21.448 / 3600) - ((46.815 * Tu) / 3600 - 0.00059 * Tu * Tu) + (0.001813 * Tu * Tu * Tu)
#print("a: ", a)
b = ((9.2025 / 3600) * cos(N)) + ((0.5736 / 3600) * cos(2 * F - 2 * D - 2 * N)) + ((0.0927 / 3600) * cos(2 * F - 2 * N))
#print("b: ", b)
c = -((17.199 / 3600) * sin(N)) - ((1.3187 / 3600) * sin(2 * F - 2 * D - 2 * N)) - ((0.2274 / 3600) * sin(2 * F - 2 * N))
#print("c: ", c)
#Grad = (Radyan * pi) / 200
a = (a * pi) / 200
b = (b * pi) / 200
c = (c * pi) / 200

#Nutasyon Matrisi
Nmatris_1_1 = cos(b)
Nmatris_1_2 = - cos(c) * sin(b)
Nmatris_1_3 = - sin(c) * sin(b)
Nmatris_2_1 = cos(a) * sin(b)
Nmatris_2_2 = cos(c) * cos(a) * cos(b) + sin(c) * sin(a)
Nmatris_2_3 = sin(c) * cos(a) * cos(b) - cos(c) * sin(a)
Nmatris_3_1 = sin(a) * sin(b)
Nmatris_3_2 = cos(c) * sin(a) * cos(b) - sin(c) * cos(a)
Nmatris_3_3 = sin(c) * sin(a) * cos(b) + cos(c) * cos(a)
#Ekrana yazdırma
print("       |   {:f}    {:f}    {:f}  |" .format(Nmatris_1_1, Nmatris_1_2, Nmatris_1_3))
print("N(t) = |   {:f}     {:f}     {:f}  |" .format(Nmatris_2_1, Nmatris_2_2, Nmatris_2_3))
print("       |   {:f}    {:f}     {:f}  |" .format(Nmatris_3_1, Nmatris_3_2, Nmatris_3_3))

