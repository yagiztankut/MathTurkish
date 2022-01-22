pi_standart=3.141592653589793

pi_basit=3.14

karekok = lambda x: x**(1/2)

dairecevre= lambda y: 2*pi_standart*y

kok2= karekok(2)

altinoran=(1+karekok(5))/2

gauss=((1+karekok(2))/2)**-1

hipotenus=lambda kenar1,kenar2:karekok(kenar1**2+kenar2**2)

bolunebilme= lambda bolunen,bolen: bolunen%bolen==0

def faktoryel(x):
    deger = 1
    for i in range(x):
        deger = deger * (i + 1)
    return deger

sayitoplami=lambda x:(x(x+1))/2

ciftsayitoplami=lambda x:x(x+1)

terimsayisi=lambda ilkterim,sonterim,artismiktari:(sonterim-ilkterim)/artismiktari+1

def asalmi(sayi):
    if sayi > 1:

        for i in range(2, sayi):
            if (sayi % i) == 0:
                return False
        else:
            return True

    else:
        return False
oran=lambda x,y:x/y

ucgenalan = lambda b,h:(1 / 2) * (b * h)

dairealan = lambda r:pi_standart*r^2

dikdortgenalan= lambda x,y:x*y

yamukmidsegment = lambda b1,b2:(1 / 2) * (b1 + b2)

dikdortgenprizmahacim =lambda l,w,h :l * w * h

ucgenprizmahacim = lambda b,h:((1 / 2) * (b * h)) * h

silindirhacim = lambda r,h:(pi_standart * (r * r)) * h

konihacim =lambda r,h: (1 / 3) * (pi_standart * (r * r)) * h

dikdortgenpiramithacim = lambda l,w,h:(1 / 3) * l * w * h

ucgenpiramithacim =lambda  b,h: (1 / 3) * ((1 / 2) * b * h) * h

kurehacim =lambda r: (4 / 3) * pi_standart * (r * r * r)

yarikurehacim = lambda r:(2 / 3) * pi_standart * (r * r * r)
