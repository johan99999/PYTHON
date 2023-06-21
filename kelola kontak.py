class Kontak:
    def __init__(self, nama, nomor):
        self.nama = nama
        self.nomor = nomor

    def __str__(self):
        return f"Nama: {self.nama}, Nomor: {self.nomor}"

def tambah_kontak(kontak_list, nama, nomor):
    kontak = Kontak(nama, nomor)
    kontak_list.append(kontak)
    print("Kontak ditambahkan.")

def lihat_kontak(kontak_list):
    if len(kontak_list) == 0:
        print("Tidak ada kontak dalam daftar.")
    else:
        for kontak in kontak_list:
            print(kontak)


def simpan_kontak_ke_file(kontak_list, nama_file):
    with open(nama_file, "w") as file:
        for kontak in kontak_list:
            file.write(f"{kontak.nama},{kontak.nomor}\n")
    print("Kontak disimpan dalam file.")



def baca_dari_file(nama_file):
    kontak_list = []
    try:
        with open(nama_file, "r") as file:
            for line in file:
                nama, nomor = line.strip().split(",")
                kontak = Kontak(nama, nomor)
                kontak_list.append(kontak)
    except FileNotFoundError:
        print("File tidak ditemukan.")
    return kontak_list



def main():
    nama_file = "kontak.txt"
    kontak_list = baca_dari_file(nama_file)

    while True:
        print(10*"=", "Menu Pengelolan Kontak", 10*"=")
        print("""
        1. Lihat Kontak
        2. Tambah Kontak
        3. Simpan Kontak ke File
        4. Keluar
        """)

        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == "1" :
            print("\nDaftar Kontak:")
            lihat_kontak(kontak_list)
        elif pilihan == "2" :
            nama = input("Masukkan nama : ")
            nomor = input("Masukan nomor : ")
            tambah_kontak(kontak_list, nama, nomor)
        elif pilihan == "3" :
            simpan_kontak_ke_file(kontak_list, nama_file)
        elif pilihan == "4" :
            break
        else:
            print("Pilihan tidak valid.Silahkan pilih menu yang tersedia.")

if __name__ == "__main__":
    main()
            