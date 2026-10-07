daftar_barang = ["Buku", "Pensil"]

while True:
    print("\n=== MENU ===")
    print("1. Lihat Data")
    print("2. Edit Data")
    print("3. Keluar")
    #tambah data
    #hapus data
    pilihan = input("Pilih menu (1/2/3): ") #input pilihan

    if pilihan == "1": #Lihat data
        print("Daftar barang:")
        for i in range(len(daftar_barang)):
            print(f"{i + 1}. {daftar_barang[i]}")

    elif pilihan == "2": #Edit data
        print("Daftar barang:")
        for i in range(len(daftar_barang)):
            print(f"{i + 1}. {daftar_barang[i]}")

        nomor = int(input("Masukkan nomor data yang mau diedit: "))
        indeks = nomor - 1   # nomor tampilan dimulai dari 1, indeks list dari 0

        if 0 <= indeks < len(daftar_barang):
            data_baru = input(f"Ganti '{daftar_barang[indeks]}' menjadi: ") #input data
            daftar_barang[indeks] = data_baru
            print("Data berhasil diubah!")
        else:
            print("Nomor tidak ditemukan.")

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")