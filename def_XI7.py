#Fungsi tanpa parameter
def hi():
    print("hello")
#Memanggil fungsi
hi()

#Fungsi menggunakan parameter
def hitung_persegi(x):
    luas = x * x
    print(luas)
#memanggil fungsi dengan argument
hitung_persegi(5)

#Fungsi menggunakan return
def hitung_segitiga(a,t):
    luas = a * t / 2
    return luas
print(hitung_segitiga(7,8))

#variable lokal
def hitung_lingkaran(r):
    luas = 3.14 * r * r
    return luas

abd = 100
print(abd)