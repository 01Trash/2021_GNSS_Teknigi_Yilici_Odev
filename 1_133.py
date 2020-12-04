"""133 	nolu noktanın koordinatlarını hesaplayınız!"""
import math

"""
27-34 arası mesafe = k,
27-32 arası mesafe = l,
34-32 arası mesafe = g,
27-133 arası mesafe = m,
133-34 arası mesafe = t,
133-32 arası mesade = s,
32, 27, 24 arası açı = teta / (Ɵ => Teta işareti),
27, 133, 34 arası açı = alfa / (α => Alfa İşareti),
32, 133, 27 arası açı = gama / (Ɣ => Gama İşareti),
27, 133, 32 arası açı = beta / (β => Beta İşareti),
"""
"""
NN  |    x (m)    |    y (m)    |  Doğrultu (gon)
27  |  23312.451  |  27320.592  |     0.00000
34  |  21756.765  |  28874.917  |    80.18273
32  |  21760.503  |  25496.384  |    276.62136
"""
"""
Koordinatları bilinen iki nokta arası mesafe:
Ara_Mesafe = math.sqrt(((X2 - X1) ** 2) + ((Y2 - Y1) ** 2))
"""
#27-34 arası mesafe = k
X_27 = 23312.451
X_34 = 21756.765
Y_27 = 27320.592
Y_34 = 28874.917
k = math.sqrt(((X_27 - X_34) ** 2) + ((Y_27 - Y_34) ** 2))
print("k: ", k)
#27-32 arası mesafe = l,
X_27 = 23312.451
X_32 = 21760.503
Y_27 = 27320.592
Y_32 = 25496.384
l = math.sqrt(((X_27 - X_32) ** 2) + ((Y_27 - Y_32) ** 2))
print("l: ", l)
#34-32 arası mesafe = g,
X_34 = 21756.765
X_32 = 21760.503
Y_34 = 28874.917
Y_32 = 25496.384
g = math.sqrt(((X_34 - X_32) ** 2) + ((Y_34 - Y_32) ** 2))
print("g: ", g)

#32, 27, 24 arası açı = teta / (Ɵ => Teta işareti)
"""Kosinüs teoreminden Ɵ (Teta) açısını hesaplayalım
g ** 2 = (k ** 2) + (l ** 2) - 2 * k * l * math.cos(teta)
Teta açısı tek bir tarafa alınırsa =>
teta = math.acos((k ** 2 + l ** 2 - g **2) / (2 * k * l))"""
teta = math.acos((k ** 2 + l ** 2 - g **2) / (2 * k * l))
teta_grad = (200 * teta) / math.pi
print("teta_grad: ", teta_grad)
print("teta: ", teta)

"""Python trigonometrik hesaplarda, radyan ile hesap yaptığı için gradı radyana çevirelim:
radyan = (grad * math.pi) / 200"""
#27, 133, 34 arası açı = alfa / (α => Alfa İşareti)
#alfa = 80.18273 grad
alfa_grad = 80.18273
alfa = (alfa_grad * math.pi) / 200
print("alfa: ", alfa)

#32, 133, 27 arası açı = gama / (Ɣ => Gama İşareti)
#gama = (400 - 276.62136) grad
gama_grad = (400 - 276.62136)
gama = (gama_grad * math.pi) / 200
print("gama: ", gama)

#27, 133, 32 arası açı = beta / (β => Beta İşareti)
#beta = 276.62136 grad
beta_grad = 276.62136 - 80.18273
beta = (beta_grad * math.pi) / 200
print("beta: ", beta)

"""Semt açısı hesabı"""
#27-34 => math.atan(semt_27_34) = (Y_34 - Y_27) / (X_34 - X_27)
semt_27_34 = math.atan((Y_34 - Y_27) / (X_34 - X_27)) + math.pi
semt_27_34_grad = (200 * semt_27_34) / math.pi
print("semt_27_34_grad: ", semt_27_34_grad)
print("semt_27_34: ", semt_27_34)

#27-32 => math.atan(semt_27_32) = (Y_32 - Y_27) / (X_32 - X_27)
semt_27_32 = math.atan((Y_32 - Y_27) / (X_32 - X_27)) + math.pi
semt_27_32_grad = (200 * semt_27_32) / math.pi
print("semt_27_32_grad: ", semt_27_32_grad)
print("semt_27_32: ", semt_27_32)

#beta = a4 + a3 + teta => a4 + a3 = beta - teta
a4_a3_toplam_grad = beta_grad - teta_grad
a4_a3_toplam_yarim_grad = a4_a3_toplam_grad / 2
a4_a3_toplam_yarim = (a4_a3_toplam_yarim_grad * math.pi) / 200
print("a4 + a3: ", a4_a3_toplam_grad)
print("(a4 + a3) / 2: ", a4_a3_toplam_yarim_grad)

#u hesabı
u = math.atan((l * math.sin(alfa)) / (k * math.sin(gama)))
u_grad = (200 * u) / math.pi
print("u_grad: ", u_grad)

#math.tan((a4 - a3) / 2) = math.tan((a4 + a3) / 2) * math.cot(50 + u)
a4_a3_fark_yarim = math.atan(math.tan(a4_a3_toplam_yarim) * (1 / math.tan((math.pi / 2) + u)))
a4_a3_fark_yarim_grad = (200 * a4_a3_fark_yarim) / math.pi
print("(a4 - a3) / 2: ", a4_a3_fark_yarim)
print("(a4 - a3) / 2: ", a4_a3_fark_yarim_grad)

"""(a4 + a3) / 2 + (a4 - a3) / 2 = a4_a3_toplam_yarim_grad + a4_a3_fark_yarim_grad =>
a4 / 2 + a4 / 2 = a4_a3_toplam_yarim_grad + a4_a3_fark_yarim_grad"""
a4_grad = a4_a3_toplam_yarim_grad + a4_a3_fark_yarim_grad
print("a4: ", a4_grad)

"""#27-133 arası mesafe = m"""

"""#133-34 arası mesafe = t"""

"""#133-32 arası mesade = s"""
