# Deklarasi fungsi / membuat fungsinya dulu
def say_hello():
    print("Hallo, Selamat pagi.")
    
def my_print(pesan):
    print(pesan)
    
def penjumalahan(angka_1 , angka_2):
    hasil = angka_1 + angka_2
    print(f"Hasil dari {angka_1} + {angka_2} adalah : {hasil}")
    

def luas_segitiga(alas, tinggi):
    hasil = 1/2 * alas * tinggi
    return hasil

#  Baru kita panggil   
say_hello()
my_print("Ini dari fungsi my print")
angka_cantik = 11223344 
my_print(angka_cantik)

angka_1 = 10
angka_2 = 20 
penjumalahan(angka_1, angka_2)


# Jika fungsi tipenya return, cara memanggilnya yang pertama, bisa di print langsung
print(luas_segitiga(20, 10))

# atau cara kedua, simpan ke sebuah variable
# luas_segitiga = luas_segitiga(20, 10)

# print(luas_segitiga)
# Volume prisma segitiga 
alas = 20
tinggi = 10
tinggi_prisma = 30  


volume =  luas_segitiga(alas, tinggi) * tinggi_prisma
print(f"Volume Prisma Segitiga yang memiliki alas = {alas}, tinggi = {tinggi}, dan tinggi prisma = {tinggi_prisma} adalah = {volume}")

# Volume Limas segitiga
alas = 20
tinggi = 10
tinggi_limas = 30  

volume = 1/3 * luas_segitiga(alas, tinggi) * tinggi_limas
print(f"Volume Limas Segitiga yang memiliki alas = {alas}, tinggi = {tinggi}, dan tinggi limas = {tinggi_prisma} adalah = {volume}")


"""Latihan Soal 1. 
- Buat fungsi untuk menampilkan hasil pangkat 2 yang menerima satu parameter berupa angka. tidak perlu mengembalikan nilai, cukup lakukan print di dalamnya. tugasnya hanya mencetak hasil kuadrat dari angka yang diberikan dengan format "hasil kuadrat dari {angka} adalah {hasil}


Latiahn soal 2. 
- Buat fungsi yang menerima 1=2 parameter yaitu panjang dan lebar, lalu fungsi ini bertugas untuk menghitung keliling persegi panjang dan kembalikan nilainya menggunakan kata kunci return. setelah fungsi dibuat, coba panggi fungsi dan simpan hasilnya ke dalam sebuah variabel, lalu cetak variable tersebut


"""
print()
# Default argumen 
def tampilkan_info(nama, kota = "Semarang"):
    print(f"Nama : {nama}")
    print(f"Kota : {kota}")
    
    
tampilkan_info("Aliffian")

print()
# Keyword argumen 
tampilkan_info("Aliffian", "Purwodadi") # ---> Positional argumen
tampilkan_info(nama="Aliffian", kota="Purwodadi") # ---> keyword argumen

# kelebihan keyword argumen adalah, tidak perlu menuliskan argumen secara berurutan
tampilkan_info( kota="Purwodadi", nama="Aliffian") # ---> keyword argumen
# tampilkan_info("Purwodadi", "Aliffian") # ---> Positional argumen