import datetime as dt


print(10 * "=" + " OPERASI HITUNG UMUR " + 10 * "=")
tgl = int(input("Masukan Tanggal Lahir Anda : "))
bln = int(input("Masukan Bulan Lahir Anda   : "))
thn = int(input("Masukan Tahun Lahir Anda   : "))

harilahir = dt.date(thn, bln, tgl)
hariapa = f"harinya adalah hari, {harilahir:%A}"
umur_hari = dt.date.today() - harilahir
umur_tahun = umur_hari.days // 365
ultahun = f"Usia anda sekarang adalah {umur_tahun}"
##################################################

#print(harilahir)
#print(harilahir, hariapa, umur_hari)
#print(umur_tahun)

mon = "Senin"
tus = "Selasa"
wed = "Rabu"
thu = "Kamis"
fri = "Jumat"
sat = "Sabtu"
sun = "Minggu"

if harilahir == "Monday" :
    print(mon)
elif harilahir == "Tuesday" :
    print(tus)
elif harilahir == "Wednesday" :
    print(wed)
elif harilahir == "Thursday" :
    print(thu)
elif harilahir == "Friday" :
    print(fri)
elif harilahir == "Saturday" :
    print(sat)
elif harilahir == "Sunday" :
    print(sun)



print(harilahir)
print(hariapa)
print(ultahun)

