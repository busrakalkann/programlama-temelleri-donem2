not1=int(input("sınav notu girin:"))
not2=int(input("sınav notu girin:"))
performans=int(input("performans notu girin:"))
ortalama=(not1+not2+performans)/3
if ortalama>50:
    print("başarılı")
else:
    print("başarısz")