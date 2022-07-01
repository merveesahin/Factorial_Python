# def faktoriyel (sayi):
# if sayi==0:
#    return 1
# else:
#    return sayi * faktoriyel (sayi-1) 


sayi = int(input("sayı giriniz:"))
deger = 1
for i in range(sayi):
    deger = deger * (i+1)
 
print("Faktoriyel : ", deger)
