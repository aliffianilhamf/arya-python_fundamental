# sebelumnya kita sudah belajar comparison operator

print("-"*20)
print("AND")
print("-"*20)
number_1 = 10

# Bagaimana jika kita ingin membuktikan apakah number 1 itu Bilangan bulat ganjil/genap positif atau ganjil/genap negatif
apakah_genap = (number_1 % 2) == 0
apakah_positif = number_1 > 0

# Ada dua kondisi yang harus kita cek
# Cek apakah angka itu genap dan positif
hasil = apakah_genap and apakah_positif # True
print(hasil)

number_1 = -10
apakah_genap = (number_1 % 2) == 0 #True
apakah_positif = number_1 > 0 # False
hasil = apakah_genap and apakah_positif # False
print(hasil)

print("-"*20)
print("OR")
print("-"*20)

nilai = 80 
persentase_kehadiran = 70 

# syarat kenaikan kelas
syarat_nilai = nilai > 90 
# ATAU
syarat_persentase_kehadiran = persentase_kehadiran > 85

# kira kira kalau kita pakai AND, apa hasilnya?
# apakah_lulus = syarat_nilai and syarat_persentase_kehadiran #Tidak LULUS
# or 
apakah_lulus = syarat_nilai or syarat_persentase_kehadiran # True
print(f"Nilai > 90 ? {syarat_nilai}")
print(f"Persentase Kehadiran > 85 ? {syarat_persentase_kehadiran}")
print(f"Syarat lulus adalah Nilai > 90 ATAU persentase kehadiran > 85")
print(f"Apakah lulus ? {apakah_lulus}")

print("-"*20)
print("NOT")
print("-"*20)

bawa_sim = True 
not_bawa_sim = not bawa_sim # False
print(not_bawa_sim) 

bawa_stnk = False 
not_bawa_stnk = not bawa_stnk # True 
print(not_bawa_stnk)