# 1.For Loops untuk string

print("For Loop String")
judul = "Kakekku Pahlawan Negara Untuk Mengabdi"
# for nama_alias in nama_variabel

for karakter in judul:
    print(karakter, end='')
    
print()
# Saya ingin menampilkan huruf vokal saja
for huruf_vokal in judul : 
    if huruf_vokal.lower() in 'aiueo' : 
        print(huruf_vokal)
        
# 2. For loop untuk List
print("For Loop Untuk List")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] # tipe data list
for number in numbers : 
    if (number % 2 == 0):
        print(f"{number} adalah bilangan genap")
        
# 3. For loop untuk range 
print("For loop untuk range")
# batas = range(16)
# batas = range(0, 16)
# batas = range(0, 16, 5)
# batas = range(15, 0, -2)

# for number in batas : 
#     print(number)



for number in range(15, 0, -2) : 
    print(number)
    
    
    
""" 
Latihan Soal 1. 
- kalimat = "Dokumen ini berisi latihan-latihan sederhana menggunakan Python"
- print hanya huruf konsonan saja (selain aiueo) dan juga print berapa jumlah hurufnya

Latihan Soal 2. 
- numbers = [30, 23, 33, 45, 54, 6, 55]
- cari nilai maksimum dari list diatas, tanpa menggunakan fungsi max() dari python

Latihan Soal 3. 
- numbers = [30, 23, 33, 45, 54, 6, 55]
- Hitung total nilai dari yang ada di list

"""

# iterasi 1 : max = 30, number = 30, number > max ? skip 
# iterasi 2 : max = 30, number = 23, number > max ? skip 
# iterasi 3 : max = 30, number = 33, number > max ? max = number
# iterasi 4 : max = 33, number = 45, number > max ? max = number
# iterasi 5 : max = 45, number = 54, number > max ? max = number
# iterasi 6 : max = 54, number = 6, number > max ? skip
# iterasi 7 : max = 54, number = 55, number > max ? max = number

# max = 55 --- Benar

numbers = [30, 23, 33, 45, 54, 6, 55]
max = 30    
for number in numbers : 
    if (number > max):
        max = number 
    else :
        print("skip")
    
print(f"Nilai maksimal {max}")