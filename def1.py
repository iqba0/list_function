#Fungsi tanpa parameter
def luas_persegi():
    sisi = int(input("Masukkan sisi: "))
    luasP = sisi * sisi
    print(luasP)
def luas_PP():
    l = int(input("Masukkan lebar: "))
    p = int(input("Masukkan panjang: "))
    print(l*p)

#Fungsi dengan parameter
def luas_persegi(sisi):
    luasP = sisi * sisi
    print(luasP)
def luas_persegi_panjang(l, p):
    luasP = l * p
    return luasP
print(luas_persegi(6)) #tanpa return
print(luas_persegi_panjang(6,10))


# n = int(input("Pilih menu program:\n1. Persegi\n2. Persegi Panjang\n "))
# if n == 1:
#     luas_persegi()
# elif n == 2:
#     luas_PP()
# else:
#     print("Salah input angka")