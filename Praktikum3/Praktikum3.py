#1. program untuk evaluasi murid
print("1. Program Evaluasi Murid")
while True:
    persen = int(input("Masukkan persentase murid: "))
    if persen >= 90:
        print("Excellent performance")
        break
    elif persen >= 80:
        print("Very Good performance")
        break
    elif persen >= 70:
        print("Good performance")
        break
    elif persen >= 60:
        print("average performance")
        break
    else:
        print("persentase minimal 60, masukkan input lagi")
print('\n')

#2. Program ini akan menunjukkan angka terbesar dari angka yg diinputkan user
print("2. Program Angka Terbesar")
angka1=int(input("Masukkan Angka Pertama: "))
angka2=int(input("Masukkan Angka Kedua: "))
angka3=int(input("Masukkan Angka Ketiga: "))
if angka1 >= angka2 and angka1 >= angka3:
    print("Angka", angka1, "merupakan angka terbesar")
elif angka2 >= angka1 and angka2 >= angka3:
    print("Angka", angka2, "adalah angka terbesar")
else:
    print("Angka", angka3, "merupakan angka terbesar")
print('\n')

#3. Program ini akan menghasilkan deret fibonacci sepanjang yg diinputkan user
print("3. Program Fibonacci")
fibonacci = int(input("Masukkan jumlah angka: "))
x, y = 0, 1
for z in range(fibonacci):
    print(x, end = " ")
    x, y = y, x + y
print('\n')

#4. Program ini menghasilkan angka ganjil hingga batas yg diinputkan user
print("4. Program Angka Ganjil")
Odd = int(input("Mau sampai angka berapa?: "))
for o in range (1, Odd + 1):
    if o % 2 != 0:
        print(o, end = " ")
print('\n')

#5. Program ini akan membuat pola setinggi yg diinputkan user
print("5. Program Pola")
Pattern = int(input("Tinggi pola: "))
for s in range (1, Pattern + 1):
    print((str(s) + " ")*s)
print('\n')