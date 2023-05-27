#masukan = float(input("masukan input yang ingin di konversi : "))
#b = masukan * (10*10)
#print(b)

#####################################################################
print("Selamat datang di sistem perhitungan konversi jarak!")
print("""
\n
    Silahkan pilih konversi yang anda inginkan!
\n
    (1). km -> hm   (2). km -> dam  (3). km -> m    (4). km -> dm   (5). km -> cm   (6). km -> mm
    """)
# \n  (7). hm -> km   (8). hm -> dam  (9). hm -> m    (10). hm -> dm  (11). hm -> cm  (12). hm -> mm
# \n  (13). dam -> km (14). dam -> hm (15). dam -> m  (16). dam -> dm (17). dam -> cm (18). dam -> mm
# \n  (19). m -> km   (20). m -> hm   (21). m -> dam  (22). m -> dm   (23). m -> cm   (24). m -> mm
# \n  (25). dm -> km  (26). dm -> hm  (27). dm -> dam (28). dm -> m   (29). dm -> cm  (30). dm -> mm
# \n  (31). cm -> km  (32). cm -> hm  (33). cm -> dam (34). cm -> m   (35). cm -> dm  (36). cm -> mm
# \n  (37). mm -> km  (38). mm -> hm  (39). mm -> dam (40). mm -> m   (41). mm -> dm  (42). mm -> cm


opr = int(input("Pilih operasi yang ingin di eksekusi : "))
while opr < 1 or opr > 42 :
    print("""
    Input Tidak Sesuai!
    Input harus berada dalam lingkup 1-42!
    Silahkan ulangi kembali!
             """)
    opr = int(input("Pilih operasi yang ingin di eksekusi : "))


def km():
    if opr == 1 :
        km = float(input("Masukan Nilai Km yang ingin di konversi : "))
        km1 = km * 10
        print("Hasil konversi dari", km ,"km ke hm adalah", km1 , "hm")
        return
    elif opr == 2 :
        km = float(input("Masukan Nilai Km yang ingin di konversi : "))
        km2 = km * (10**2)
        print("Hasil konversi dari", km ,"km ke dam adalah", km2 , "dam")
        return
    elif opr == 3 :
        km = float(input("Masukan Nilai Km yang ingin di konversi : "))
        km3 = km * (10**3)
        print("Hasil konversi dari", km ,"km ke m adalah", km3 , "m")
        return
    elif opr == 4 :
        km = float(input("Masukan Nilai Km yang ingin di konversi : "))
        km4 = km * (10**4)
        print("Hasil konversi dari", km ,"km ke dm adalah", km4 , "dm")
        return
    elif opr == 5 :
        km = float(input("Masukan Nilai Km yang ingin di konversi : "))
        km4 = km * (10**5)
        print("Hasil konversi dari", km ,"km ke cm adalah", km4 , "cm")
        return
    elif opr == 6 :
        km = float(input("Masukan Nilai Km yang ingin di konversi : "))
        km4 = km * (10**6)
        print("Hasil konversi dari", km ,"km ke mm adalah", km4 , "mm")
        return
# ########################################################################
# def hm():
#     if opr == 7 :
#         hm = float(input("Masukan Nilai Hm yang ingin di konversi : "))
#         hm1 = hm / 10
#         print("Hasil konversi dari", hm ,"hm ke km adalah", hm1 , "km")
#         return
#     elif opr == 8 :
#         hm = float(input("Masukan Nilai Hm yang ingin di konversi : "))
#         hm2 = hm * 10
#         print("Hasil konversi dari", hm, "hm ke dam adalah", hm2, "dam")
#         return
#     elif opr == 9 :
#         hm = float(input("Masukan Nilai Hm yang ingin di konversi : "))
#         hm3 = hm * (10**2)
#         print("Hasil konversi dari", hm, "hm ke m adalah", hm3, "m")
#         return
#     elif opr == 10 :
#         hm = float(input("Masukan Nilai Hm yang ingin di konversi : "))
#         hm4 = hm * (10**3)
#         print("Hasil konversi dari", hm, "hm ke dm adalah", hm4, "dm")
#         return
#     elif opr == 11 :
#         hm = float(input("Masukan Nilai Hm yang ingin di konversi : "))
#         hm5 = hm * (10**4)
#         print("Hasil konversi dari", hm, "hm ke cm adalah", hm5, "cm")
#         return
#     elif opr == 12 :
#         hm = float(input("Masukan Nilai Hm yang ingin di konversi : "))
#         hm6 = hm * (10**5)
#         print("Hasil konversi dari", hm, "hm ke mm adalah", hm6, "mm")
#         return


km()
# hm()