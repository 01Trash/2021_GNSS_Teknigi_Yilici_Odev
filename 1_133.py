"""133 	nolu noktanın koordinatlarını hesaplayınız!"""
import math

"""
27-34 arası mesafe = k,
27-32 arası mesafe = l,
27-133 arası mesafe = m,
133-34 arası mesafe = t,
133-32 arası mesade = s,
27, 133, 34 arası açı = alfa / (α => Alfa İşareti),
32, 133, 27 arası açı = gama / (Ɣ => Gama İşareti),
27, 133, 32 arası açı = beta / (β => Beta İşareti),
"""
"""
Koordinatları bilinen iki nokta arası mesafe:
Ara_Mesafe = math.sqrt(((X2 - X1) ** 2) + ((Y2 - Y1) ** 2))
"""
#27-24 arası mesafe = k
X2 = 23312.451
X1 = 21756.765
Y2 = 27320.592
Y1 = 28874.917
k = math.sqrt(((X2 - X1) ** 2) + ((Y2 - Y1) ** 2))
print("k: ", k)

#27-32 arası mesafe = l,
X2 = 23312.451
X1 = 21760.503
Y2 = 27320.592
Y1 = 25496.384
l = math.sqrt(((X2 - X1) ** 2) + ((Y2 - Y1) ** 2))
print("l: ", l)

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


"""#27-133 arası mesafe = m"""

"""#133-34 arası mesafe = t"""

"""#133-32 arası mesade = s"""
