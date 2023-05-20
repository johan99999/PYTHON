print(200*"#")
print("\t\t\t\t\t\t\t\tSELAMAT DATANG DI SISTEM UJI PENDAFTARAN MAHASISWA")
print(200*"#")
print("""
Silahkan isi data diri anda pada form yang tersedia di bawah ini 
(Catatan : Isi data-data sesuai dengan data diri anda yang sebenarnya)
""")
print(200*"#")
nama = input("NAMA : ")
umur = int(input("UMUR : "))
pdkn = input("PENDIDIKAN TERAKHIR : ")
agm = input("AGAMA : ")
nr = float(input("NILAI RATA-RATA : "))
print("Halo",",", nama, "," , "dengan usia", umur, ",", "Pendidikan Terakhir yaitu,",pdkn, ",", "Beragama", agm, "dengan nilai rata-rata,",nr )

if umur <= 17 :
    print("Maaf. anda tidak lolos, dikarenakan umur anda belum mencukupi!")
elif nr <= 18.00 :
    print("Maaf. anda tidak lolos, dikarenakan nilai rata-rata anda belum mencukupi")
else :
    print("Selamat anda lolos")