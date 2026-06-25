""" 
List adalah salahs atu tipe data yang digunakan untuk menyimpan beberapa item / nilai dalam 1 variabel.
# list dibuat menggunakan tand kurung siku [] dan antar item dipisahkan menggunakan koma.
list bisa menyimpan lebih dari 1 tipe data
untuk mendapatkan value sebuah list, menggunakan indeks.
indeks pada list selalu dimulai dari 0.
"""

my_list = ["Hello", 1, 2, True, 3.14]

print(my_list)

# Mendapatkan valu dengan Indeks
print("\nMendapatkan Value dengan Indeks")
print(f"Isi dari my_list[0] : {my_list[0]}")
print(f"Isi dari my_list[2] : {my_list[2]}")
print(f"Isi dari my_list[4] : {my_list[4]}")
print(f"Isi dari my_list[-1] : {my_list[-1]}")
print(f"Isi dari my_list[-3] : {my_list[-3]}")

print("\nMendapatkan Value dengan Slice")
print(f"Isi dari my_list_2[ : 3] : {my_list[ : 3]}")
my_list_2 = [12, 100, 23, "indonesia", True]
print(f"Isi dari my_list_2[2 : 4] : {my_list_2[2 : 4 ]}")
# print(f"Isi dari my_list_2[1 : 5] : {my_list_2[1 : 5]}")
print(f"Isi dari my_list_2[1 : ] : {my_list_2[1 : ]}")


""" 
Latihan List
my_list_3 = ["Ratna", 0, 100, 32, False, [99,88], True]

1. Tampilkan item ke 3
2. Dapatkan nilai false dengan negatif indexing 
3. Dapatkan nilai [99,88]
4. Dapatkan nilai [100, 32, False, [99, 88]]
5. Dapatkan Nilai ["Ratna", 100, False, True]
"""
my_list_3 = ["Ratna", 0, 100, 32, False, [99,88], True]
# print(my_list_3[7])#Out of Range

print("\nMengubah Value Pada List")
nama_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

print(nama_hari)

# ubah sabtu menjadi saturday 
nama_hari[-2] = "Saturday"
print(nama_hari)
nama_hari[3 : 5] = ["Thursday", "Friday"]
print(nama_hari)
nama_hari[:3:2] = ["Monday", "Wednesday"]
print(nama_hari)


print("\nMenambah Item Pada List")
numbers = [1, 2, 3, 4, 5]
print(numbers)
# 1. Append 
numbers.append(6)
print(numbers)
numbers.append(7)
print(numbers)


# 2. Insert
numbers.insert(1, 10)
print(numbers)
numbers.insert(4, "Bingo")
print(numbers)

# 3 extend 
hari = ["Senin", "Selasa"]
bulan = ["Jan", "Feb"]
print(f"List Hari isinya : {hari}")
print(f"List Bulan isinya : {bulan}")
hari.extend(bulan)
print('Setelah di Extend')
print(f"List Hari isinya : {hari}")
print(f"List Bulan isinya : {bulan}")

""" 
months = ["Januari", "April", "September", "Desember"]
- Lengkapi list months dengan menambahkan bulan yang kosong menggunakan bahasa inggris (cth, February, March, May, dst)
- Ubah Januari, Aparil, September, Desember ke bahasa inggris juga

"""


print("\nMenghapus Item Pada List")
my_list_4 = ["Ani", 33, 44, 55]
print(f"My list 4 : {my_list_4}")
# 1. pop()
# Dia akan menghapus item terakhir, kalau tidak ada indeksnya, kalau ada indeksnya, dia akan menghapus sesuai indeks
hasil_pop = my_list_4.pop() # tdk ada indeks, berarti item terakhir yang akan di hapus
print(f"My list 4 setelah di pop() : {my_list_4} item yang di hapus : {hasil_pop}")
hasil_pop_2 = my_list_4.pop(1) # ada indeks, berarti item sesuai indeks yang akan di hapus
print(f"My list 4 setelah di pop(1) : {my_list_4} item yang di hapus : {hasil_pop_2}")

# 2. remove() 
# Menghapus item mana yang dipilih dalam parameter remove 
my_list_5 = [100, 200, 300, 400, 500]
my_list_6 = my_list_5.copy() 
print(f"\nMy list 5 : {my_list_5}")

hasil_remove = my_list_5.remove(300)
print(f"My list 5 setelah di remove() : {my_list_5} item yang di hapus : {hasil_remove}")


print("\nLooping Item Pada List")
print(f"My list 6 : {my_list_6}")
# Looping dengan for 
print("Looping dengan for")
indeks = 0
for number in my_list_6 : 
    print(f"Number : {number} atau {my_list_6[indeks]} pada indeks {indeks}")
    indeks += 1
    
print("Looping dengan for range")
for i in range(len(my_list_6)):
     print(f"Number :  {my_list_6[i]} pada indeks {i}")
     
print("Looping dengan for enumerate")
for indeks, item in enumerate(my_list_6):
    print(f"Number :  {item} pada indeks {indeks}")
    

print("Looping dengan While")
n = 0 
panjang_list = len(my_list_6)

while n < panjang_list : 
    print(f"Number :  {my_list_6[n]} pada indeks {n}")
    n += 1
    
""" 
mahasiswa = ["Andi", "Joko", "Pardi", "Aziz"]
1. Looping bebas (for / while) dapatkan indeks dan valuenya

nilai = [60, 70, 75, 99, 90, 89, 99, 87]
2. buat list kosong bernama nilai_lulus 
3. gunakan looping untuk memeriksa setiap nilai, jika lebih besar atau sama dengan 80, masukkan nilai ke dalam nilai_lulus
4. tampilkan nilai lulus

kontak_kotor = ["Andi", "Budi", "Andi", "Siti", "Budi", "Dewi", "Siti"]
5. buat list kosong bernama kontak_bersih
6. gunakan looping untuk mengiterasi daftar kontak_kotor, cek apakah nama belum ada di kontak bersih, jika belum, masukkan ke kontak bersih,kalau sudah, tidak perlu di masukkan 
7. cetak isi kontak_bersih
"""

# List comprehension
print("\nList Comprehension")
numbers = [1,2,3,4]
pangkat_numbers = []
print(f"Isi list numebrs : {numbers}")
# membuat pangkat dari item" di list 
for number in numbers: 
    pangkat_numbers.append(number ** 2) 
    
print(f"Isi list Pangkat numbers menggunakan for biasa : {pangkat_numbers}")

pangkat_numbers = [number ** 2 for number in numbers]
print(f"Isi list Pangkat numbers menggunakan list comprehension : {pangkat_numbers}")

my_numbers = [ 100, 151, 200, 251, 100]
my_numbers_ganjil = [ item if item % 2 == 1 else "genap" for item in my_numbers]
my_numbers_ganjil = [ item for item in my_numbers if item % 2 == 1 ]
print(my_numbers_ganjil)

""" 
celcius = [0, 10, 20, 30, 40]
1. Buat list comprehension untuk konversi ke fahrenheit
    fahrenheit = [......]
    print(fahrenheit)

id_karyawan = [102, 105, 201, 304, 307, 408, 511]
2. Buat list comprehension dengan if di akhir untuk id genap
    id_genap = [.......]
    print(id_genap)
    
data_sensor = [20, 75, 45, 110, 15]
3. Buat list comprehension untuk menentukan jarak detkat atau aman, jika jarak kurang dari 50 berarti DEKAT, selain itu, AMAN 
    status_objek = [.......]
    print(status_objek)

"""