umur = 40

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
- Buat program untuk mengecek apakah bilagngan itu 0, positif atau negatif
- Jika nol print "NOL"
- Jika Positif print "POSITIF"
- Jika Negatif print "NEGATIF"

Latihan 2. 
- Buat program untuk mencari number terbesar dari 3 variable
- print variabel terbesar tersebut

a = 15
b = 8 
c = 20



Latihan 3. 
- Buat program untuk menghitung konversi Suhu dari celcius ke fahrenheit, celcius ke reamur, dan celcius ke kelvin
- buat inputan suhu celciusnya menggunakan method input()
- jangan lupa konversi ke float karene input selalu bertipe string 
- print pilihan tujuan konversi, misal : 
    Pilih Tujuan Konversi
    1: Fahrenheit
    2: Reamur
    3: Kelvin
- buat inputan lagi untuk menampung pilihan dari user, mau di konversi ke apa
- buat logika pengkondisian dari user memilih konversi yang apa
- di masing masing kondisi, jika memilih 
    1. Fahrenheit, rumusnya (suhu_celcius * 9/5) + 32, lalu print "{suhu_celcius} sama dengan {suhu_fahrenheit}"
    2. Reamur, rumusnya suhu_celcius * 4/5, lalu print "{suhu_celcius} sama dengan {suhu_reamur}"
    3. Kelvin, rumusnya suhu_celcius + 273.15, lalu print "{suhu_celcius} sama dengan {suhu_kelvin}"
- Jika pilihan tidak valid, print "Pilihan tidak valid, silahkan pilih 1, 2, atau 3"
"""