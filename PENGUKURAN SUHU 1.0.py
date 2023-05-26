def garis():
    print(80*"=")
    print(80*"=")

garis()
print(13*"=","Selamat datang di sistem pengukuran konversi suhu!!!",13*"=")
garis()
print ("""
Silahkan pilih konversi yang ingin di eksekusi!\n
(1). Celcius -> Reamur        (2). Celcius -> Fahrenheit    (3). Celcius -> Kelvin

(4). Reamur -> Celcius        (5). Reamur -> Fahrenheit     (6). Reamur -> Kelvin

(7). Fahrenheit -> Celcius    (8). Fahrenheit -> Reamur     (9). Fahrenheit -> Kelvin

(10). Kelvin -> Celcius       (11). Kelvin -> Reamur        (12). Kelvin - Fahrenheit     
\n
""")
opr = int(input("Masukan pilihan operasi yang anda inginkan (exp :1,2...12) : "))

while opr <= 0 or opr > 12 :
    print("Maaf Pilihan tidak tersedia!")
    opr = int(input("Masukan pilihan operasi yang anda inginkan (exp :1,2...12) : "))


def celcius():
    if opr == 1 :
        c = float(input("Masukan besar celcius yang ingin di konversi : "))
        cr = ((4/5)*c)
        print("hasil dari konversi" ,c , "celcius ke reamur adalah" , cr , "reamur")
        return
    elif opr == 2 :
        c = float(input("Masukan besar celcius yang ingin di konversi : "))
        cf = ((9/5)*c)+32
        print("hasil dari konversi" ,c , "celcius ke fahrenheit adalah" , cf , "fahrenheit")
        return
    elif opr == 3 :
        c = float(input("Masukan besar celcius yang ingin di konversi : "))
        ck = c+273
        print("hasil dari konversi" ,c , "celcius ke kelvin adalah" , ck , "kelvin")
        return


def reamur ():
    if opr == 4 :
        r = float(input("Masukan besar reamur yang ingin di konversi : "))
        rc = ((5/4)*r)
        print("hasil dari konversi" ,r , "reamur ke celcius adalah" , rc , "celcius")
        return
    elif opr == 5 :
        r = float(input("Masukan besar reamur yang ingin di konversi : "))
        rf = ((9/4)*r)+32
        print("hasil dari konversi" ,r , "reamur ke fahrenheit adalah" , rf , "fahrenheit")
        return
    elif opr == 6 :
        r = float(input("Masukan besar reamur yang ingin di konversi : "))
        rk = ((5/4)*r)+273
        print("hasil dari konversi" ,r , "reamur ke kelvin adalah" , rk , "kelvin")
        return

def fahrenheit():
    if opr == 7 :
        f = float(input("Masukan besar fahrenheit yang ingin di konversi : "))
        fc = (5/9)*(f-32)
        print("hasil dari konversi" ,f , "fahrenheit ke celcius adalah" , fc , "celcius")
        return
    elif opr == 8 :
        f = float(input("Masukan besar fahrenheit yang ingin di konversi : "))
        fr = (4/9)*(f-32)
        print("hasil dari konversi" ,f , "fahrenheit ke reamur adalah" , fr , "reamur")
        return
    elif opr == 9 :
        f = float(input("Masukan besar fahrenheit yang ingin di konversi : "))
        fk = (5/9)*(f-32)+273
        print("hasil dari konversi", f, "fahrenheit ke kelvin adalah", fk, "kelvin")
        return

def kelvin():
    if opr == 10 :
        k = float(input("Masukan besar kelvin yang ingin di konversi : "))
        kc = k-273
        print("hasil dari konversi", k, "kelvin ke celcius adalah", kc , "celcius")
        return
    elif opr == 11 :
        k = float(input("Masukan besar kelvin yang ingin di konversi : "))
        kr = (4/5)*(k-273)
        print("hasil dari konversi" ,k , "kelvin ke reamur adalah" , kr , "reamur")
        return
    elif opr == 12 :
        k = float(input("Masukan besar kelvin yang ingin di konversi : "))
        kf = (9/5)*(k-273)+32
        print("hasil dari konversi" ,k , "kelvin ke fahrenheit adalah" , kf , "fahrenheit")
        return

celcius()
reamur()
fahrenheit()
kelvin()

