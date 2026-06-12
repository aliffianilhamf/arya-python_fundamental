def get_data(**keywords_data):
    # print(keywords_data)
    nama = keywords_data['nama']
    tinggi = keywords_data['tinggi']
    berat = keywords_data['berat']
    
    print(f"Hallo {nama}, tinggi kamu {tinggi} cm berat kamu {berat} kg")


def get_biodata(**biodata) : 
    # for key in biodata:
    #     # print(key)
    #     # print(type(key))
    #     print(f"{key} : {biodata[key]}")
    
    for key, value in biodata.items() :
        print(f"{key} : {value}") 
    
    
get_data(nama="Aliffian", tinggi=165, berat=60)
get_biodata(nama="Aliffian", tinggi=165, berat=60, alamat="Purwodadi", hobi="badminton")