import sys, subprocess

def usia():
    tahun_lahir = int(input("Masukan Tahun Lahir : "))
    tahun_now = int(input("Masukan Tahun Sekarang : "))
    umur = (tahun_now - tahun_lahir)
    print("Terhitung umur anda dari tahun " + str(tahun_lahir) + " sampai " + str(tahun_now) + " adalah " + str(umur) + " tahun")
    if umur == 19 :
                print("Selamat Ulang Tahun yang ke-19!!!")

    elif umur >= 25 :
                print("Kawin-kawin la, sampai kapan mak ki nunggu nk dapet cucu...")

    if tahun_lahir == tahun_now :
        print("Tahun Lahir dan Tahun sekarang tidak boleh sama")
        input("Tekan tombol apa saja untuk melanjutkan...")
# subprocess.run(clear, shell=True)
usia()




usia()

