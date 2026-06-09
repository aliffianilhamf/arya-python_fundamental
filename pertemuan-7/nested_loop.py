# For 
months = ["Januari", "Februari", "Maret"]
days = ["Senin", "Selasa", "Rabu"]

for bulan in months : 
    for hari in days : 
        print(f"{hari} {bulan}")
        
# Iterasi 1 : Senin Januari 
# Iterasi 2 : Selasa Januari 
# Iterasi 3 : Rabu Januari 
# Iterasi 4 : Senin Februari
# Iterasi 5 : Selasa Februari
# Iterasi 6 : Rabu Februari
# Iterasi 7 : Senin Maret
# Iterasi 8 : Selasa Maret 
# Iterasi 9 : Rabu Maret


i = 1 
j = 1 

while i <= 5 :
    while j <= 5: 
        hasil = i * j
        print(hasil)
        
        j += 1
        
    print("")
    i += 1
    j = 1
    
print()
for i in range(1, 6):
    for j in range(1, 6):
        result = i * j 
        print(result, end="\t")
    
    print()
    
print() 
count = 0
while True :
    tebakan = int(input("Masukkan Tebakkan Anda : ")) 
    count += 1
    
    if tebakan > 10 : 
        print("Tebakan Terlalu tinggi")
    elif (tebakan < 10) : 
        print("Tebakan Terlalu Rendah")
    else : 
        print(f"Tebakan Benar, sebanyak {count} percobaan")
        break