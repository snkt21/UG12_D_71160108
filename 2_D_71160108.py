#Surya Nathaniel Kattu
#Nim: 71160108
#Soal No 2

hari = str(input("Hi Kiko, Silahkan Masukkan hari yang ingin Anda telusuri: "))

# condition
if hari == "senin":
    #List Mata Kuliah
    matkulsenin = ['ke - 1 Algoritma Graf', 'ke - 3 Sistem Operasi', 'ke - 4 PAK']
    # perulangan
    for hari in range(len(matkulsenin)):
        print("Kelas", matkulsenin[hari])

# condition
elif hari == "selasa":
    #List Mata Kuliah
    matkulselasa = ['ke - 2 Matematika Teknik', 'ke - 4 Bahasa Indonesia', 'ke - 6 PKN']
    # perulangan
    for hari in range(len(matkulselasa)):
        print("Kelas", matkulselasa[hari])

# condition
elif hari == "rabu": 
    #List Mata Kuliah   
    matkulrabu = ['ke - 2 Sistem Basis Data', 'ke - 4 Praktikum Sistem Basis Data']
    # perulangan
    for hari in range(len(matkulrabu)):
        print("Kelas", matkulrabu[hari])

# condition
elif hari == "kamis":   
    #List Mata Kuliah 
    matkulkamis = ['ke - 1 IMK', 'ke - 3 Logmat', 'ke - 4 Praktekkom']
    # perulangan
    for hari in range(len(matkulkamis)):
        print("Kelas", matkulkamis[hari])

# condition
elif hari == "jumat":
    print("Hari Jumat Anda tidak ada kelas")    