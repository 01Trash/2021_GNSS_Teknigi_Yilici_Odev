"""Kutup hareketi hesaplayınız!"""
"""Tarih: 18.11.2020; Saat: 06:02:00"""
"""ECEF sistemine göre sayılar alınmıştır."""
import numpy as np

x_p = 0.00009
y_p = 0.00009
Wmatris_1_1 = 1
Wmatris_1_2 = 0
Wmatris_1_3 = x_p
Wmatris_2_1 = 0
Wmatris_2_2 = 1
Wmatris_2_3 = - y_p
Wmatris_3_1 = - x_p
Wmatris_3_2 = y_p
Wmatris_3_3 = 1
#Ekrana yazdırma
print("       |   {:.5f}     {:.5f}     {:.5f}  |" .format(Wmatris_1_1, Wmatris_1_2, Wmatris_1_3))
print("W(t) = |   {:.5f}     {:.5f}    {:.5f}  |" .format(Wmatris_2_1, Wmatris_2_2, Wmatris_2_3))
print("       |  {:.5f}     {:.5f}     {:.5f}  |" .format(Wmatris_3_1, Wmatris_3_2, Wmatris_3_3))
print("---------------------------------------------")

#Determinant hesabı
matrix = np.array([[1,0,0.00009],[0,1,-0.00009],[-0.00009,0.00009,1]])
print("Determinant W(t): {:.13f}" .format(np.linalg.det(matrix)))
