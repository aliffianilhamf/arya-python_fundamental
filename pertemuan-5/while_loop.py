number = 1

# if number < 10:
#     print("Number anda lebih kecil dari 10")
    
while number < 10 : 
    print(f"Number anda lebih kecil dari 10 - perulangan ke {number}")
    
    # increment / menaikkan angkanya
    number = number + 1
    

print()
angka = 0
while angka < 5 : 
    print(f"perulangan ke {angka}")
    
    # increment
    angka += 1 #  number = number + 1
    
    print()
    
    text = "3"
    while text.isdigit() == True : 
        text = input("Masukkan angka : ")
        if text.isdigit() == True : 
            print(f"Inputkan Kamu {text}")
            
print("Akhir dari Program")