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


# Latihan 2
"""  
1. Membuat dictionary awal untuk template, isinya kosongan dulu tidak apa - apa --> fromkeys
    - nama_mahasiswa --> str
    - nim --> str
    - sks --> int
    - beasiswa --> bool
    - tahun lahir --> int 
    - bulan lahir --> int 
    - tanggal lahir --> int 
    
2. buat dictionary kosongan yang menyimpan informasi beberapa siswa
3. lakukan looping menggunakan while loop, agar bisa looping terus menerus sampai ada perintah break
    4. didalam looping, buat dictionarry baru untuk menampung 1 mahasiswa, keysnya bisa diambil dari dictionarry no 1.
    5. buat inputan nama dan masukkan ke dicstionary mahasiswa dengan key = "nama"
    6. buat inputan nim dan masukkan ke dicstionary mahasiswa dengan key = "nim"
    7. buat inputan sks dan masukkan ke dicstionary mahasiswa dengan key = "sks"
    8. buat inputan beasiswa dan masukkan ke dicstionary mahasiswa dengan key = "beasiswa"
    9. buat inputan tahun lahir dan simpan ke variabale tahun_lahir
    10. buat inputan bulan lahir dan simpan ke variabale bulan_lahir
    11. buat inputan tanggal lahir dan simpan ke variabale tanggal_lahir
    12 buat variable birthday yang isinya konversi waktu dari tahun, bulan, dan hari yang di dapatkan dari input, menggunakan library datetime di python
        import datetime as dt
        dt.datetime(tahun_lahir, bulan_lahir, tanggal_lahir)
    13. buat key unik untuk masing masing mahasiswa yang akan di masukkan ke dictionarry yang di buat di nomor 2 
        import random
        key = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
        dict_mhs.update({key, mahasiswa})
        
    14. print data mahasiswa 
    15. buat inputan lanjut / tidak dan pastikan user mengisikan y/n 
    16. jika y, maka user akan tetap menambahkan mahasiswa baru, jika n maka program berhenti (break)
.strftime("%x")
"""


student = {
    "nama" : "Aliffian",
    "NIM" : 1000000
}
student = {
    "nama" : "Ilham",
    "NIM" : 1000000
}

students = {
    "Aliffian" : {
        "nama" : "Aliffian",
        "NIM" : 1000000
    },
    
    "Ilham" : {
        "nama" : "Ilham",
        "NIM" : 1000000
    }
    
}

import datetime as dt
mhs_template = {
    'nama' : 'Jawil jalangkung',
    'nim' : 'A11.2022.14155',
    'sks' : 142,
    'beasiswa' : True, 
    'lahir' : dt.datetime(2001,1,1)
}

students = {} 

while True : 
    mahasiswa = dict.fromkeys(mhs_template.keys())
    mahasiswa['nama'] = input("Masukkan Nama Anda: ")