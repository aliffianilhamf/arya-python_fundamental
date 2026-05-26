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

# Splitting (Memisah string)
# Pengecekan tipe konten
# Replacing