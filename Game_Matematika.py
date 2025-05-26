import random
import time

print("=GAME MATEMATIKA=")
time.sleep(1)

# Menu pilihan level
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Menu Pilihan Level : ")
print("1. Level 1 (Penjumlahan)")
print("2. Level 2 (Pengurangan)")
print("3. Level 3 (Perkalian)")
print("4. Level 4 (Pembagian)")
print("5. Exit")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
time.sleep(1)

try:
    nomorpilihan = int(input("Pilih Nomor Pilihan : "))
except ValueError:
    print("Input tidak valid. Harus angka.")
    exit()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

skor = 0
lives = 3

while True:
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    
    # Hindari pembagian dengan nol
    while nomorpilihan == 4 and y == 0:
        y = random.randint(1, 100)

    jml = x + y
    krg = x - y
    kl = x * y
    bg = round(x / y, 2)

    if nomorpilihan == 1:
        try:
            jumlah = int(input("Hasil dari {} + {} adalah : ".format(x, y)))
            if jumlah == jml:
                skor += 2
                print("Hore... jawaban Anda benar !!! skor Anda", skor, "( lives :", lives, ")")
            else:
                lives -= 1
                print("Yaaah... jawaban Anda salah, skor Anda", skor, "( lives :", lives, ")")
        except ValueError:
            print("Input tidak valid. Harus angka.")
            continue

    elif nomorpilihan == 2:
        try:
            kurang = int(input("Hasil dari {} - {} adalah : ".format(x, y)))
            if kurang == krg:
                skor += 2
                print("Hore... jawaban Anda benar !!! skor Anda", skor, "( lives :", lives, ")")
            else:
                lives -= 1
                print("Yaaah... jawaban Anda salah, skor Anda", skor, "( lives :", lives, ")")
        except ValueError:
            print("Input tidak valid. Harus angka.")
            continue

    elif nomorpilihan == 3:
        try:
            kali = int(input("Hasil dari {} * {} adalah : ".format(x, y)))
            if kali == kl:
                skor += 2
                print("Hore... jawaban Anda benar !!! skor Anda", skor, "( lives :", lives, ")")
            else:
                lives -= 1
                print("Yaaah... jawaban Anda salah, skor Anda", skor, "( lives :", lives, ")")
        except ValueError:
            print("Input tidak valid. Harus angka.")
            continue

    elif nomorpilihan == 4:
        try:
            bagi = float(input("Hasil dari {} / {} adalah (2 angka desimal): ".format(x, y)))
            if round(bagi, 2) == bg:
                skor += 2
                print("Hore... jawaban Anda benar !!! skor Anda", skor, "( lives :", lives, ")")
            else:
                lives -= 1
                print("Yaaah... jawaban Anda salah, skor Anda", skor, "( lives :", lives, ")")
                print("Jawaban yang benar adalah:", bg)
        except ValueError:
            print("Input tidak valid. Harus angka (desimal).")
            continue

    elif nomorpilihan == 5:
        print("Terima kasih telah bermain!")
        break

    else:
        print("Maaf Pilihan Anda Salah")
        break

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # Menang
    if skor >= 10:
        print("SELAMAT! Anda mencapai skor maksimum! SKOR AKHIR:", skor)
        break

    # Kalah
    if lives == 0:
        print("GAME OVER")
        break