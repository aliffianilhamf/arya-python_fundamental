number = 1

# if number < 10:
#     print("Number anda lebih kecil dari 10")
    
while number < 10 : 
    print(f"Number anda lebih kecil dari 10 - perulangan ke {number}")
    
    # increment / menaikkan angkanya
    number = number + 1
    
print("Akhir dari While loop")

print()
# angka = 0
# while angka < 5 : 
#     print(f"perulangan ke {angka}")
    
#     # increment
#     angka += 1 #  number = number + 1
    
#     print()
    
#     text = "3"
#     while text.isdigit() == True : 
#         text = input("Masukkan angka : ")
#         if text.isdigit() == True : 
#             print(f"Inputkan Kamu {text}")
            
print("Akhir dari Program")

""" 
Latihan 1. 
- Buat program untuk menampilkan bilangan genap yang ada dari range 1 - 20
- print("2 adalah bilangan genap")

Latihan 2. 
- User akan menebak angka rahasia
- lakukan perulangan selama angka tebakan user itu tidak sama dengan angka rahasia
- tebakan user menggunakan fungsi input()
- jika tebakan user terlalu rendah, maka print "tebakan anda terlalu rendah"
- jika tebakan user terlalu tinggi, maka print "tebakan anda terlalu tinggi"
- kita hitung juga berapa kali user telah menebak
- Kalau tebakan benar, keluar dari loop dan print 
"Selamat tebakan anda benar, angka rahasianya adalah 7 dan sudah menebak sebanyak 4 kali"
"""

angka = 1
while (angka <= 20):
    if (angka % 2 == 0 ):
        print(f"{angka} adalah bilangan genap")
    angka += 1
    
    

    
