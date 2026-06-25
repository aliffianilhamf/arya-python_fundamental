# Dictionary adalah struktur data yang menyimpan pasangan key-value.
# Setiap key harus unik dan digunakan untuk mengakses nilai, bukan lagi menggunakan indeks.

# membuat dictionary
my_dict = {
    #key    : Value 
    "nama"  : "Sutini",
    "umur"  : 25,
    "alamat": "Semarang"
}

my_dict_2 = {
    10  : "sepuluh",
    20  : "duapuluh",
    30  : "tigapuluh"
}

my_dict_3 = {
    (1, 2) : "pasangan angka"
}

my_dict_4 = dict(nama="Aliffian", umur=23, alamat="Semarang")

keys = ["nama", "umur", "alamat"]
values = ["Aliffian", 23, "Semarang"]
my_dict_5 = dict(zip(keys, values))



my_dict_6 = dict.fromkeys(keys)


print(my_dict)
print(my_dict_2)
print(my_dict_3)
print(my_dict_4)
print(my_dict_5)
print(my_dict_6)



# cara mengakses item dictionary
print(my_dict["nama"]) # Mengakses nilai dengan key 'nama' pada my_dict
print(my_dict.get("umur")) # Mengakses nilai dengan key 'umur'
print(my_dict.get("alama", "Purwodadi")) # Mengakses nilai dengan key 'alamat'


# Update nilai dict 
my_dict_4["umur"] = 25 
my_dict_4.update({"nama": "Ilham", "pekerjaan" : "Mahasiswa"})

print(my_dict_4)


# delete dict 
del my_dict_4["pekerjaan"]
nilai_yang_di_pop = my_dict_4.pop("alamat")
print(f"Nilai yang di pop : {nilai_yang_di_pop}")
print(my_dict_4)


# looping 
students = {
    "Alex" : 90,
    "Indra" : 89,
    "Hanif" : 88
}

for key in students:
    print(f"{key} nilainya : {students[key]}")
    
print(students.items())
for key, value in students.items():
    print(f"{key} nilainya : {value}")
    
print(students.keys())
print(students.values())

print(f"banyaknya item dalam dict students : {len(students)}")
print(f"Aapakah hanif ada dalam dict studens? {'Hanif' in students}")
print(f"Aapakah amel ada dalam dict studens? {'Amel' in students}")

# delete dict 
students.clear() 
print(students)


# Buatlah sebuah dictionary yang menyimpan informasi tentang sebuah buku, 
# seperti judul, penulis, tahun terbit, dan genre. Kemudian, lakukan operasi berikut:
# 1. Tambahkan informasi tentang penerbit buku tersebut.
# 2. Perbarui tahun terbit buku tersebut.
# 3. Hapus informasi tentang genre buku tersebut.
# 4. Tampilkan semua informasi tentang buku tersebut.