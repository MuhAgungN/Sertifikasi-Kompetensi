# Kasir Sederhana Tanpa Database
import datetime

# Daftar produk (disimpan di memori)
daftar_produk = []

# Tambah Produk ke List
def tambah_produk(nama, harga):
    id_produk = len(daftar_produk) + 1
    daftar_produk.append((id_produk, nama, harga))

# Lihat Semua Produk
def tampilkan_produk():
    return daftar_produk

# Hitung Total Belanja
def hitung_total(daftar_belanja):
    total = 0
    for item in daftar_belanja:
        total += item[2]  # item[2] adalah harga
    return total

# Cetak Struk
def cetak_struk(daftar_belanja):
    print("\n===== STRUK BELANJA =====")
    for item in daftar_belanja:
        print(f"{item[1]} - Rp{item[2]:,.0f}")
    total = hitung_total(daftar_belanja)
    print(f"TOTAL: Rp{total:,.0f}")
    print(f"Waktu: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("========================\n")

# Fungsi Utama
def main():
    while True:
        print("List Menu:")
        print("1. Tambah Produk")
        print("2. Lihat Produk")
        print("3. Belanja")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            nama = input("Nama produk: ")
            harga = float(input("Harga produk: "))
            tambah_produk(nama, harga)
            print("Produk ditambahkan.\n")

        elif pilihan == '2':
            produk = tampilkan_produk()
            print("\nDaftar Produk:")
            for p in produk:
                print(f"{p[0]}. {p[1]} - Rp{p[2]:,.0f}")
            print()

        elif pilihan == '3':
            produk = tampilkan_produk()
            daftar_belanja = []
            while True:
                id_produk = input("Masukkan ID produk (atau 'selesai'): ")
                if id_produk.lower() == 'selesai':
                    break
                item = next((p for p in produk if str(p[0]) == id_produk), None)
                if item:
                    daftar_belanja.append(item)
                    print(f"{item[1]} ditambahkan.")
                else:
                    print("Produk tidak ditemukan.")
            cetak_struk(daftar_belanja)

        elif pilihan == '4':
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid.\n")

if __name__ == "__main__":
    main()
