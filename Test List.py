menu_item = 0
namelist = []
while menu_item != 9:
    print(20*"-")
    print("""
    1. Mencetak List
    2. Menambahkan nama kedalam list
    3. Menghapus nama dari list
    4. Mengubah data dalam list
    9. Keluar
     """)
    menu_item = int(input("Pilih menu : "))
    if menu_item == 1 :
        current = 0
        if len(namelist) > 0 :
            while current < len(namelist) :
                print(current, ".", namelist[current])
                current = current + 1
        else:
            print("List kosong")
    elif menu_item == 2 :
        name = input("Masukan nama : ")
        namelist.append(name)
    elif menu_item == 3 :
        del_name = input("Nama yang ingin dihapus : ")
        if del_name in namelist:
            item_number = namelist.index(del_name)
            del namelist[item_number]
        else:
            print(del_name, "tidak ditemukan")
    elif menu_item == 4 :
            old_name = input("Nama apa yang ingin diubah : ")

            if old_name in namelist :
                item_number = namelist.index(old_name)
                new_name = input("Nama baru : ")
                namelist[item_number] = new_name
            else:
                print(old_name, "tidak ditemukan")

print("Selamat Tinggal")

