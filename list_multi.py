daftar = [["aa","bb"],["cc","dd"],["ee","ff"]]
daftar[1].insert(0, "gg")
daftar[0].remove("bb")
daftar[2].append("hh")
del daftar[2][1]
print(daftar)
daftar.pop()
print(daftar)