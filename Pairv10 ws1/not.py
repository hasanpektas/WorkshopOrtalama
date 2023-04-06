vize = float(input("Vize notunuzu giriniz:"))
final = float(input("Final notunuzu giriniz: "))
ortalama = (vize* 0.4) + (final* 0.6) 

if ortalama<50:
    print("Ortalaman:",ortalama)
    print("Notun:FF")
elif ortalama>49 and ortalama<60 :
    print("Ortalaman:",ortalama)
    print("Notun:DD")
elif ortalama>59 and ortalama<70 :
    print("Ortalaman:",ortalama)
    print("Notun:CC")
elif ortalama>69 and ortalama<80 :
    print("Ortalaman:",ortalama)
    print("Notun:BB")
else:
    print("Ortalaman:",ortalama)
    print("Notun:AA")
