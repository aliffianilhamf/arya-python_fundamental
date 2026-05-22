"""
Data terdiri dari beberapa jenis tipenya : 
1. string - teks : Diapit oleh petik 2, atau petik 1
2. integer (int) - angka : Berupa angka bilangan bulat bisa positif, negatif, atau nol 
3. float - angka : Berupa bilangan pecahan / desimal, ada komanya.
4. boolean (bool) : isinya hanya 2 yakni True dan False
"""

# 1. String (str)
print("Belajar python!")
print('Belajar Python')

print("Jum'at") # gunakan petik 2, kalau di dalam teks terdapat petik 1
# print('Jum'at')

print("")
# 2. Integer (int)
print(23)
print(5) 
print(-10)
print(0)

print("")
# 3. Float
print(165.7)
print(5.55) 

print("")
# 4. Boolean (bool)
print(True)
print(False)


""" LATIHAN
1. tampilkan biodatamu sesuai format berikut : 
Aliffian Ilham Febriyana -> string
23 -> int 
165.7 -> float
False -> bool
"""

print("")
# Mengecek tipe data
print(type("Aliffian Ilham Febriyana"))
print(type(23))
print(type(165.7))
print(type(False))
