# Memanipulasi Huruf 
text = 'belaJar pyThOn FundAmenTal'

print(f"Original  : {text}")
print(f"Lower     : {text.lower()}")
# replace
# text = text.lower()
# membuat variable baru
text_lower = text.lower()
print(f"Original  : {text}")
print(f"lower yang disimpan di variable baru  : {text_lower}")
print(f"Capitalize  : {text.capitalize()}") # Huruf pertama kapital 
print(f"Upper   : {text.upper()}")
print(f"Title   : {text.title()}") # Tiap kata diawali huruf kapital
print(f"Swapcase    : {text.swapcase()}")

""" 
Latihan 1. 
"semangatku tIdak Pernah PudAR"
- Buat menjadi Capitalize dan Title case

"""

print()
# Pembersihan spasi
data_kotor = "  Data Ini Sangat Kotor   "
print(f"Data Ori : '{data_kotor}'")
print(f"Strip : '{data_kotor.strip()}'")
print(f"Left Strip : '{data_kotor.lstrip()}'")
print(f"Right Strip : '{data_kotor.rstrip()}'")

""" 
Latihan 2. 
"   SemaRang"
- Rapikan Menggunakan Strip dan Lower

"""

print()
# Splitting (Memisah string)
judul = "Pangeran dari kota selatan"
judul_split = judul.split(" ")
print(f"Original Judul : {judul}")
print(f"Judul hasil split {judul_split}")

kode_barang = "XII-FGC-123"
kode_barang_split = kode_barang.split("-")
print(f"Original Kode Barang {kode_barang}")
# kode_barang_split.append(1)
# kode_barang_split.append(False)
print(f"Kode barang hasil split {kode_barang_split}")

print()
# Pengecekan tipe konten
string_1 = "Python3"
# isalnum (mengecek apakah string berisi alpa numerik - campuran huruf dan angka)
print(f"Apakah Alnum ? {string_1.isalnum()}")
# isalpha (Mengecek apakah string berisikan alpha /huruf)
print(f"Apakah is alpa? {string_1.isalpha()}")
# isdigit (Mengecek apakah string hanya berisikan angka)
print(f"Apakah angka saja? {string_1.isdigit()}")

print()
# Replacing
kode_barang = "XII-FGC-123"
kode_barang_replace = kode_barang.replace("-", " ")
print(f"Original Kode Barang : {kode_barang}")
print(f"Kode barang hasil replace : {kode_barang_replace}")

nama = "Aliffian Ilham Febriyana"
nama_replace = nama.replace("Ilham", "Hanif")
print(f"Original nama : {nama}")
print(f"Nama hasil replace : {nama_replace}")
print(f"Original nama : {nama}")

kode_barang_lower_replace = kode_barang.lower().replace("-", "**")
print(f"Original Kode Barang : {kode_barang}")
print(f"Kode barang hasil lower + replace : {kode_barang_lower_replace}")


""" 
Latihan Soal 1. 
Bersihkan spasi diawal /akhir dan ubah menjadi huruf kecil semua 
- input : " JaKaRtA  "
- target : "jakarta"

Latihan Soal 2. 
Hapus "Rp" (termasuk spasi setelah Rp) dan hapus tanda titik "."
- input : "Rp 15.000.000"
- Target : "15000000"

Latihan Soal 3.
Pecah String berdasarkan karakter strip (-)
- input : "IPHONE13-RED-256GB 
- Target : ['IPHONE13', 'RED', '256GB']

Latihan Soal 4. 
gabungkan list menggunakan separator tanda hubung (-)
- input : ['belajar', 'python', 'untuk', 'pemula']
- target : "belajar-python-untuk-pemula"

Latihan Soal 5. 
Pisahkan string berdasarkan |, bersihkan spasi diawal dan akhir setiap item, ubah jadi huruf kecil, ubah spase di tengah menjadi udnerscore (_), hapus tanda kurung
- input : " Nama Customer | Total Belanja (IDR) | Alamat Pengiriman  "
- target : ['nama_customer_', '_total_belanja_idr_', '_alamat_pengiriman']
"""

print()
# 1
string_1 = " JaKaRtA  "
print(f"{string_1.lower().strip()}")

# 2
string_2 = "Rp 15.000.000"
result = string_2.replace(".", "").replace("Rp ", "")
print(result)

# 3
string_3 = "IPHONE13-RED-256GB" 
result = string_3.split("-")
print(result)

# 4
string_4_list = ['belajar', 'python', 'untuk', 'pemula']
result = "-".join(string_4_list)
print(result)

# 5 
string_5 = " Nama Customer | Total Belanja (IDR) | Alamat Pengiriman  "
result = string_5.lower().strip().replace(" ", "_").replace("(", "").replace(")", "").split("|")
print(result)