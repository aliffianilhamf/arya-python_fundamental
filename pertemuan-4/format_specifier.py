nilai_pi = 3.14159265 

# 1. Mengatur presisi / jumlah angka dibelakang koma
print(f"Nilai PI (2 desimal) : {nilai_pi:.2f}") # 3.14
print(f"Nilai PI (5 desimal) : {nilai_pi:.5f}") # 3.14159

# 2 Menambahkan koma sebagai pemisah ribuan 
# Rp. 1,250,000.00
harga = 1250000
print(f"Harga barang : Rp. {harga:,.2f}")

# 3. Jika ingin menampilkan persentase
persentase_diskon = 0.05 
print(f"Diskon : {persentase_diskon:.0%}")

# 4. mengatur perataan dan lebar kolom 
nama = "ilham"
print(f"Nama siswa (rata kiri) : '{nama:<10}'")
print(f"Nama siswa (rata kanan) : '{nama:>10}'")
print(f"Nama siswa (rata tengah) : '{nama:^10}'")