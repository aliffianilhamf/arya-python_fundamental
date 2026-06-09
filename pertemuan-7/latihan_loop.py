# for i in range(1, 6) : 
#     for j in range(0, i) : 
#         print("*", end=" ")
        
#     print()
   
#    c++ code 
# for(int i = 1; i < 6 ; i++){
#     for(int j = 0; j < i; j++ ){
#         std::cout << "* ";
#     }
    
#     std::cout << "";
# }

# latihan bintang 1 
for i in range(1, 6):
    print("*" * i)
    
# latihan bintang 2 
for i in range(5, 0, -1):
    print("*" * i)
    
# latihan bintang 3
jumlah_bintang = 5
for bintang in range(1, jumlah_bintang + 1): 
    spasi = jumlah_bintang - bintang 
    print(f"{' ' * spasi}{'*' * bintang}")
    
# latihan bintang 5
jumlah_baris = 5
for i in range(1, jumlah_baris + 1): 
    spasi = jumlah_baris - i 
    bintang = (2 * i) - 1
    print(f"{' ' * spasi}{'*' * bintang}")