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
X2_27 = 23312.451
X1_34 = 21756.765
Y2_27 = 27320.592
Y1_34 = 28874.917
k = math.sqrt(((X2_27 - X1_34) ** 2) + ((Y2_27 - Y1_34) ** 2))
print("k: ", k)
#27-32 arası mesafe = l,
X2_27 = 23312.451
X1_32 = 21760.503
Y2_27 = 27320.592
Y1_32 = 25496.384
l = math.sqrt(((X2_27 - X1_32) ** 2) + ((Y2_27 - Y1_32) ** 2))
print("l: ", l)
#34-32 arası mesafe = g,
X2_34 = 21756.765
X1_32 = 21760.503
Y2_34 = 28874.917
Y1_32 = 25496.384
g = math.sqrt(((X2_34 - X1_32) ** 2) + ((Y2_34 - Y1_32) ** 2))
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
beta_grad = 276.62136
beta = (beta_grad * math.pi) / 200
print("beta: ", beta)

"""#gama_grad + alfa_grad + beta_grad + (a4 + a3) = 400
a4_a3 = 400 - (gama_grad + alfa_grad + beta_grad)
print("a4 + a3: ", a4_a3)"""

"""Semt açısı hesabı"""
#27-34 => math.atan(semt_27_34) = (Y2_27 - Y1_34) / (X2_27 - X1_34)
semt_27_34 = math.atan((Y2_27 - Y1_34) / (X2_27 - X1_34))
semt_27_34_grad = (200 * semt_27_34) / math.pi
print("semt_27_34_grad: ", semt_27_34_grad)
print("semt_27_34: ", semt_27_34)

"""#27-133 arası mesafe = m"""

"""#133-34 arası mesafe = t"""

"""#133-32 arası mesade = s"""
