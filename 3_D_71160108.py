#Surya Nathaniel Kattu
#Nim: 71160108
#Soal No 3

#inputan angka untuk panjang diagonal
a = int(input("Masukkan angka: "))

#function (seperti pada materi sebelumnya) diamond yang didalamnya ada perulangan 
def diamond(a):
    #perulangan untuk membentuk diamond
    for i in range (a) :
        print(" "* (a-i)+" *"*(i+1))
    for j in range (a) :
        print(" "*(j+2)+" *"*(a-1-j))

diamond(a)