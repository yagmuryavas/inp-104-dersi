nokta1 = (0, 0)
nokta2 = (3, 4)
x_farki = nokta2[0] - nokta1[0]
y_farki = nokta2[1] - nokta1[1]
toplam = (x_farki ** 2) + (y_farki ** 2)
import math 
mesafe = math.sqrt(toplam)
print( "Mesafe:", mesafe)