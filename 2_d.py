"""Gerçek yıldız zamanı hesaplayınız!"""
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
#print("Jülyen günü: {:.2f}" .format(JD))

#T0 hesabı
T0 = (JD - 2451545) / 36525
#print("T0: ", T0)
#GMST hesabı
a1 = 6 * 3600 + 41 * 60 + 50.54841
#print(a1)
a2 = 8640184.812866 * T0
#print(a2)
a3 = 0.093104 * T0 * T0
#print(a3)
a4 = (6.2 * pow(10, -6)) * T0 * T0 * T0
#print(a4)
GMST = a1 + a2 + a3 - a4
#print("GMST => {:.2f}" .format(GMST))

GMST_hour = 0
while GMST > 3600:
    GMST = GMST - 3600
    GMST_hour = GMST_hour + 1
GMST_minute = 0
while GMST > 60:
    GMST = GMST - 60
    GMST_minute = GMST_minute + 1
GMST_second = GMST

#print(GMST_hour)
#print(GMST_minute)
#print(GMST_second)
print("GMST => {:.0f} h {:.0f} m {:.4f} s" .format(GMST_hour, GMST_minute, GMST_second))

