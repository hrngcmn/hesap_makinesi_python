import math # kök alma işlemini yaptırabilmek için math kütüphanesi çağırılır.
sonuc = 0
sayi = float(input("Bir sayı girişi yapınız:")) # kullanıcıdan sayı girişi yaptırır.
#ondalıklı sayılarla işlem yapabilmesi için float çevrimi yapılmıştır.
sonuc = sonuc + sayi # sonuc değişkenine sayiyi atar.
print(sonuc) # Amaç yazılan sayının ilk başta gözükmesidir.
while( 1 ): # sonsuz döngüye sokulmuştur. işlemin sürekliliği için.
    isaret = input("..  +, -, *, / ,kök, üs, mutlak, %(mod)  .. işaretlerinden birini gir:")
    if(isaret=="+" or "-" or "*" or "/"):
        if(isaret== "+"):
            sayi = float(input("Sayı girişi yapınız:"))
            sonuc = sonuc +sayi
            print(sonuc)
        if(isaret =="-"):
            sayi = float(input("Sayı girişi yapınız:"))
            sonuc= sonuc - sayi
            print(sonuc)
        if(isaret == "*"):
            sayi = float(input("Sayı girişi yapınız:"))
            sonuc= sonuc * sayi
            print(sonuc)
        if(isaret=="/"):
            sayi = float(input("Sayı girişi yapınız:"))
            sonuc=sonuc / sayi
            print(sonuc)
    if(isaret=="kök"):
        sonuc = math.sqrt(sonuc)
        print(sonuc)
    if(isaret=="üs"):
        üs = float(input("üs sayınızı giriniz:"))
        sonuc = sonuc**üs
        print(sonuc)
    if(isaret=="mutlak"):
        sonuc = abs(sonuc)
        print(float(sonuc))
    if(isaret=="%"):
        sayi=float(input("Modu aldıracak sayiyi giriniz"))
        sonuc = sonuc%sayi
        print(sonuc)



