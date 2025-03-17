adet=int(input("kaç tane alacaksınız"))
birim_fiyat=int(input("ürün birim fiyatını gırınız"))
toplam = adet*birim_fiyat
if toplam >=3000:
    toplam=toplam-toplam*0.20
    print("ürünlerin tutari:",toplam)
else:
    toplam=toplam-100
    print("ürünlerin tutar:",toplam)
