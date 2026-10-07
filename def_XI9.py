#Menulis funtion tanpa parameter
def hi():
    print("Hello world!") #argumen

#Memanggil function: hi()

def hitung_luas_persegi():
    sisi = int(input("masukkan sisi persegi: "))
    print(sisi*sisi)
    
def hitung_luas_persegi_panjang(p,l):
    luas = p*l
    print(luas)
    
#panjang = int(input("Masukkan panjang: "))
#lebar = int(input("Masukkan lebar: "))
# hitung_luas_persegi_panjang(panjang,lebar)

def hitung_luas_segitiga(a,t):
    luas = a * t / 2
    return luas

def hitung(a):
    return a * a

cetak = hitung(12)
print(cetak)

    



