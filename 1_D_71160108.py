#Surya Nathaniel Kattu
#Nim: 71160108
#Soal No 1

#inputan user
ad = int(input("Masukkan awal deret: "))
ak = int(input("Masukkan akhir deret: "))

#function (seperti pada materi sebelumnya) untuk deret angka
def deretangka():
    #bagian perulangan
    for angka in range (ad, ak):
        #angka genap dan tidak habis dibagi 3 dan 7
        if angka %2 == 0 and angka % 3 != 0 and angka % 7 != 0 :
            print(angka)

deretangka()