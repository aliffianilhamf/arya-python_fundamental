# Set merupakan tipe data yanag menyimpan nilai yang unik dan tidak memiliki urutan tertentu
# Set juga tidak dapat diakses menggunakan indeks

my_set = {1,2,3,4,5,1}
print(my_set)

# Mengakses set
for item in my_set:
    print(item)
    
print()
# Menambahkan value pada set 
my_set.add(2)
print("Set setelah di tambah 2")
print(my_set)
my_set.add(6)
print("Set setelah di tambah 6")
print(my_set)

# Menghapus item dari set 
my_set.remove(2)
print('Setelah menghapus item 2')
print(my_set)
