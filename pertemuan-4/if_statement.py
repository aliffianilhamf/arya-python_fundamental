suhu = 42 

print("Program Dimulai")
if suhu < 36 : 
    print("Anda Normal")

if (suhu > 40 ):
    print("Anda harus segera ke rumah sakit")


operator = input("masukkan operator : ")
angka_1 = 10
angka_2 = 20
if (operator == "+"):
    hasil = angka_1 + angka_2
    print(f"Hasil penjumlahan dari {angka_1} + {angka_2} adalah {hasil}")
    
    
# kita ingin mencari apakah suatu bilangan itu ganjil positif 
bilangan = 30 
if ((bilangan % 2 == 1) and (bilangan > 0)): 
    print(f"Bilangan {bilangan} merupakan bilangan Ganjil Positif")
    
# kita ingin mencari apakah suatu bilangan itu genap positif 
if ((bilangan % 2 == 0) and (bilangan > 0)) : 
    print(f"Bilangan {bilangan} merupakan bilangan Genap Positif")
    
# kita ingin mencari apakah suatu bilangan itu  genap negatif
# kita ingin mencari apakah suatu bilangan itu  ganjil negatif
print("Program Selesai")