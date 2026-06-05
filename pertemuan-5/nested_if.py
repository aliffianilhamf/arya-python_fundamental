umur = 0

if umur > 0:
    if umur >= 28 :
        print("Anda Sudah tua")
    elif umur >= 18 : 
        print("Anda masih dewasa")
    elif umur >= 12 : 
        print("Anda masih remaja")
    elif umur >= 6 : 
        print("Anda masih anak anak")
    else : 
        print("Anda Masih Balita")
else : 
    print("Umur tidak boleh negatif atau 0")
    
    
print("Program Selesai")

# Suatu program untuk mengkategorikan nilai
#   - A -> >= 85 
#   - B -> >= 79 
#   - C -> >= 60 
#   - D -> >= 40 
#   - E -> >= 1 
#   - 0 -> = 0  

# Buat program untuk mengkategorikan nilai di atas 
#   - A -> >= 85 --> if
#   - B -> >= 79 --> elif
#   - C -> >= 60 --> elif
#   - D -> >= 40 --> elif
#   - E -> >= 1 --> elif
#   - 0 -> = 0  --> else

# Buat program untuk mengkategorikan nilai diatas, namun pastikan tidak ada nilai yang negatif
#  mengecek apakah nilai positif --> if
#   - A -> >= 85 --> if
#   - B -> >= 79 --> elif
#   - C -> >= 60 --> elif
#   - D -> >= 40 --> elif
#   - E -> >= 1 --> elif
#   - 0 -> = 0  --> else
# jika nilai negatif --> else

"""  
Latihan 1. 
- Membuat progran kalkulator sederhana
- memiliki 3 inputan
    1. Angka pertama, buat variable untuk menampung inputan angka pertama
    2. Operator, buat juga variable untuk menampung inputan operator (+, -, x, /)
    3. Angka kedua, buat variable untuk menampung inputan angka kedua
- cek user memasukkan operator apa?
    - jika penjumlahan (+) maka print "{angka_1} + {angka_2} = {hasil}
    - jika penjumlahan (-) maka print "{angka_1} - {angka_2} = {hasil}
    - jika penjumlahan (x) maka print "{angka_1} x {angka_2} = {hasil}
    - jika penjumlahan (/) maka print "{angka_1} / {angka_2} = {hasil}
        - pembagi itu tidak boleh nol (angka_2), oleh karena itu, ada if untuk mengecek agar angka 2 tidak nol
        - jika angka_2 itu nol, maka cukup print saja "Angka kedua tidak boleh nol"
        - tapi kalau angka_2 tidak nol, maka lakukan operasi pembagian seperti biasa.
- Jika operator yang dipilih tidak valid, maka print "operator tida valid (+, -, x, /)"
"""
total_beli = input("Masukkan total belanja : ")
total_beli = float(total_beli)

print(f"Total belanja {total_beli}")
if total_beli > 10000:
    diskon = 20/100 * total_beli
    print(f'Selamat kamu mendapatkan diskon sebesar {diskon}')
else : 
    if total_beli > 5000 : 
        diskon = 10/100 * total_beli
        print(f'Selamat kamu mendapatkan diskon sebesar {diskon}')
    else : 
        if total_beli > 200 : 
            diskon = 5/100 * total_beli 
            print(f'Selamat kamu mendapatkan diskon sebesar {diskon}')
        else : 
            diskon = 0


print(f"Total yang harus di bayar adalah : {total_beli - diskon}")