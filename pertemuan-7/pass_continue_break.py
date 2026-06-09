# Pass 
angka = 0 

while angka < 20: 
    if angka % 2 == 1 : 
        # pass
        print("SKip dulu, belum tahu mau ngapain")
        # if angka > 0 : 
        #     print(f"{angka} adalah ganjil positif")
        # else :
        #     print(f"{angka} adalah ganjil negatif")
    else :
        print(f"{angka} adalah bilangan genap")
    angka += 1
    
    
    
# Continue
print()
print("Continue") 
for number in range(20): 
    if number  == 5 : 
        # print("Di skip karena continue")
        continue
    else :
        print(f"{number} adalah bilangan genap")
        
        
# Break
print()
print("Break") 
for number in range(20): 
    if number  == 5 : 
        break
    else :
        print(f"{number} adalah bilangan genap")
        
print("Program selesai")