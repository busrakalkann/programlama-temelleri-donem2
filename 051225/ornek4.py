not = []
zayif_sayisi=0
for i in range(6):
    not.append(int(input("bir sayi girin")))
for j in not:
    toplam=toplam+j
    if j <50:
        zayif_sayisi=zayif_sayisi+1
print(ortalama)