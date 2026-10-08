#Function tanpa parameter
def hello():
    print("Hello world!")
    
#Function dengan parameter dan tanpa return
def luas_segitiga(alas,tinggi):
    L = alas * tinggi / 2
    print(L)

#Function dengan parameter dan return
def luas_persegi(sisi):
    L = sisi * sisi
    return L

luas_segitiga(3,6) #mengisi argument
# hitung = luas_segitiga(3,6)
print(luas_persegi(5))
