print("Praktikum 2 if statement")
print()

bil1 = int(input("Masukan Bilangan Ke-1: "))
bil2 = int(input("Masukan Bilangan Ke-2: "))
bil3 = int(input("Masukan Bilangan Ke-3: "))

hasil = 0

if bil1 > bil2:
    hasil = bil1
else:
    hasil = bil2

if bil3 > hasil:
    hasil = bil3

print("Bilangan Terbesar adalah ", hasil)