""" 
Typecasting adalah suatu proses untuk mengubah tipe data suatu variable, ke tipe data yang laiinya.
contohnya : string ke int (hanya bisa string ang), int ke float, float ke int
yang tidak bisa di konversi, string yang mengandung character ke int / float
"""

print("Konversi string ke INT")
#1.  Konversi string ke INT
nama = "Aliffian"
# konversi
# nama_int = int(nama) # menghasilkan error
number_str = "10"
print(f"{number_str} tipe data sebelum dikonversi adalah : {type(number_str)}")
number_int = int(number_str)
print(f"{number_int} tipe data setelah dikonversi adalah : {type(number_int)}")

print()
# 2. String ke Float
print("Konversi string ke FLOAT")
number_str = "10"
print(f"{number_str} tipe data sebelum dikonversi adalah : {type(number_str)}")
number_float = float(number_str)
print(f"{number_float} tipe data setelah dikonversi adalah : {type(number_float)}")

print()
# 3. String ke BOOLEAN
print("Konversi string ke BOOLEAN")
nilai_str = "True"
print(f"{nilai_str} tipe data sebelum dikonversi adalah : {type(nilai_str)}")
nilai_bool = bool(nilai_str)
print(f"{nilai_bool} tipe data setelah dikonversi adalah : {type(nilai_bool)}")


nilai_str_2 = "False"
print(f"{nilai_str_2} tipe data sebelum dikonversi adalah : {type(nilai_str_2)}")
nilai_bool_2 = bool(nilai_str_2)
print(f"{nilai_bool_2} tipe data setelah dikonversi adalah : {type(nilai_bool_2)}")

# Karena konversi string ke boolean, akan selamanya TRUE jika valuenya ada. kalau valuenya kosong, baru false
nilai_str_3 = ""
print(f"{nilai_str_3} tipe data sebelum dikonversi adalah : {type(nilai_str_3)}")
nilai_bool_3 = bool(nilai_str_3)
print(f"{nilai_bool_3} tipe data setelah dikonversi adalah : {type(nilai_bool_3)}")

print()
# 3. Int ke float 
print("Konversi INT ke FLOAT")
number_int = 20 
print(f"{number_int} tipe data sebelum dikonversi adalah : {type(number_int)}")
number_float = float(number_int)
print(f"{number_float} tipe data setelah dikonversi adalah : {type(number_float)}")

print()
# 3. Float ke int 
print("Konversi FLOAT ke INT")
number_float = 20.99
print(f"{number_float} tipe data sebelum dikonversi adalah : {type(number_float)}")
number_int = int(number_int)
print(f"{number_int} tipe data setelah dikonversi adalah : {type(number_int)}")

