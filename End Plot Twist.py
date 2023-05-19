print(100*"~")
print(100*"~")
print('"ada seorang penjahat sedang menahan seorang tawanan,\ndan akan mengancam menembak tawanan tersebut..."')
print('\n"kau hanya membawa sebuah pistol yang berisi sebuah peluru..."')
print("Catatan : untuk melanjutkan apa yang terjadi, masukan angka kemungkinan yang akan membawa mu ke beberapa plot twist berbeda ,exp : 1, 2,...5")
print(100*"~")
print(100*"~")
End = int(input("masukan salah satu angka dari 1-3 : "))
print(100*"~")


def end1():
    print('\n"Kau mulai Membidik Kepalanya, dan mencari momentum dimana bidikanmu benar-benar mengenai kepala sang penjahat..."')
    print('\n"Bang!, timah panas keluar dari selongsong pistol, dan mulai menembus kepala sang penjahat"...')
    print('\n"Sang Penjahat pun tumbang, dan tawanan pun berhasil selamat..."')
    print('=========================GOOD ENDING==============================')

def end2():
    print('\n"Kau mulai Membidik Kepalanya, dan mencari momentum dimana bidikanmu benar-benar mengenai kepala sang penjahat..."')
    print('\n"Tetapi Tanganmu benar-benar bergetar hebat, sehingga hal buruk terjadi".....')
    print('\n"Bang!, timah panas keluar dari selongsong pistol tanpa sengaja, meleset dan mulai menembus kepala sang Tawanan"...')
    print('\n"Sang tawanan pun tumbang, nyawa sang tawanan di akhiri oleh sebuah peluru pistol yang tidak berniat sedikitpun membunuh dirinya"... ')
    print('=========================BAD ENDING============================')

def end3():
    print('\n"Saat kau mencari momentum, Kau mulai membidik kemaluan sang penjahat"...')
    print('\n"Dan saat itulah, teriakan kencang dari sang penjahat, yang menandakan pelernya sudah petjah,"AARARHAHRGRHGRHRGAHRGAHRGRHG!!!!"')
    print('\n"Sang Tawanan berhasil selamat, namun dia agak kasihan dengan sang penjahat, tahu bahwa pelernya petjah..."')
    print('\n"Sang Penjahat mati dengan kondisi peler petjah, sangat mengenaskan"...')
    print('================AWKWARD ENDING====================')



if End == 1 :
    end1()
elif End == 2 :
    end2()
elif End == 3 :
    end3()
else :
    print("???")