#XI-6
daftar = [["aa","bb"],["cc","dd"],["ee","ff"]]
daftar[1].insert(0, "gg")
daftar[0].remove("bb")
daftar[2].append("hh")
del daftar[2][1]
print(daftar)
daftar.pop()
print(daftar)

#XI-7
daftar = [[11,12,13],[4,5,6], [77, 99]]
#daftar[0][1] = "Ahayy"
daftar.append(101)
daftar[0].insert(1, 100)
print(daftar)
del daftar[0][0] #Delete berdasarkan index
daftar[0].remove(13) #Delete berdasarkan index
daftar[1].pop(1)

print(daftar)