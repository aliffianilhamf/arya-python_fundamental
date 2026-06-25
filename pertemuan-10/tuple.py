
# Tuple adalah tiped ata di python yang hampir mirip dengan LIST
#  Tapi dia immutable (Tidak bisa diubah, setelah di deklarasikan)

my_tup = (1, 1, 2, 3, 4)
print(my_tup)


# kita ingin mengakses item ke 3
print(f"Akses item ke 3 : {my_tup[2]}")
print(f"Akses item ke terakhir : {my_tup[-2]}")

# coba mengubah tuple 
# my_tup[0] = 10
# print(my_tup)

# Kita akali dengan konversi menjadi list dulu 
my_tup_list = list(my_tup)
updated_list = [value * 2 for value in my_tup_list]
updated_tuple = tuple(updated_list)
print(updated_tuple)

# unpack tuple
tup_hari = ("Senin", "Selasa", "Rabu", "Kamis")
*a, b, c = tup_hari
print(a)

# Looping pada tupe 
for item in tup_hari:
    print(item)
    

# Jebakan di tuple
tup_bulan = ("Januari")
tup_bulan_2 = ("Januari",)

print(f"Tuple yang bukan tuple : {tup_bulan} tipenya {type(tup_bulan)}")
print(f"Tuple yang asli tuple : {tup_bulan_2} tipenya {type(tup_bulan_2)}")

# method yang ada di tuple 
my_tup_2 = (1,2,3,3,2,1)

print(f"Jumlah angka 1 pada my_tup_2 adalah : {my_tup_2.count(1)}") # menghitung banyaknya item dari suatu tuple
print(f"Indeks angka 3 pada my_tup_2 : {my_tup_2.index(3)}") # mencari indeks pertama munculnya angka 3 


# Fungsi zip - menggabungkan data dari beberapa iterable (perulangan) menjadi 1 varibale yang berisi tuple 
print() 
nama_produk = ["Laptop", "Mouse", "Keyboard"]
harg_produk = [12000000, 200000, 500000]

# for item in nama_produk:
#     for harga in harg_produk:
#     print(f"{item} harga {harg_produk}")



# gabungkan dengan method zip 
produk_tergabung = zip(nama_produk, harg_produk)
for nama, harga in produk_tergabung:
    print(f"{nama} harga : {harga}")
    
print(type(produk_tergabung)) # zip 
produk = list(zip(nama_produk, harg_produk))
print(produk)