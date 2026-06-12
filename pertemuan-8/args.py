def kalkulasi_jumlah(angka_1, angka_2, angka_3, angka_4, angka_5):
    hasil = angka_1 + angka_2 + angka_3 + angka_4 + angka_5
    
    return hasil 

# *args (arguments)
def hasil_args(*numbers): 
    # print(numbers)
    angka_1 = numbers[0]
    angka_2 = numbers[1]
    angka_3 = numbers[2]
    angka_4 = numbers[3]
    angka_5 = numbers[4]
    
    return  angka_1 + angka_2 + angka_3 + angka_4 + angka_5

def hasil_args_loop(*numbers): 
    # print(numbers)
    hasil = 0 
    for number in numbers : 
        hasil = hasil + number
    
    return  hasil


result = kalkulasi_jumlah(10, 20, 30, 40, 50)
print(f"hasil dari fungsi adalah : {result}")

result_2 = hasil_args_loop(10, 20, 30, 40, 50,60, 70, 80, 90, 00)
print(f"hasil dari fungsi adalah : {result_2}")

""" 
latihan Soal 1. 
- buatlah fungsi yang menerima *args sebagai parameternya. fungsi ini harus mampu menerima berapapun jumlah argumen angka, lalu kemablikan nilai total perkalian dari seluruh angka tersebut


Latihan soal 2.
- Buat fungsi yang menerima 2 parameter : 
    1. toko (string)
    2. *args untuk daftar barang
- Fungsi ini harus mencetak nama toko terlebih dahulu, kemudian mencetak setiap barang yang ada di dalam args satu per satu
"""