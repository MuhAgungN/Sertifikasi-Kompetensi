import mysql.connector

# Konfigurasi koneksi
host = "localhost"
database = "db_sekolah"
user = "root"
password = ""  # sesuaikan jika punya password

# Membuat koneksi
try:
    db = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    if db.is_connected():
        print("Berhasil terkoneksi ke database", database)

except mysql.connector.Error as err:
    print("Gagal terkoneksi ke database:", err)

cursor = db.cursor()

# Fungsi validasi ID siswa
def cek_id_siswa(id_siswa):
    sql = "SELECT COUNT(*) FROM siswa WHERE id_siswa = %s"
    cursor.execute(sql, (id_siswa,))
    hasil = cursor.fetchone()
    return hasil[0] > 0

# Tambah siswa
def tambah_siswa():
    nama = input("Nama siswa: ")
    kelas = input("Kelas: ")
    sql = "INSERT INTO siswa (nama, kelas) VALUES (%s, %s)"
    cursor.execute(sql, (nama, kelas))
    db.commit()
    print("✅ Siswa berhasil ditambahkan.\n")

# Tampilkan daftar siswa
def lihat_siswa():
    print("\n--- Daftar Siswa ---")
    cursor.execute("SELECT id_siswa, nama, kelas FROM siswa")
    hasil = cursor.fetchall()
    if hasil:
        for row in hasil:
            print(f"ID: {row[0]} | Nama: {row[1]} | Kelas: {row[2]}")
    else:
        print("Belum ada data siswa.")
    print()

# Input nilai
def input_nilai():
    id_siswa = input("ID Siswa: ")
    if not cek_id_siswa(id_siswa):
        print("❌ ID Siswa tidak ditemukan.\n")
        return
    mapel = input("Mata Pelajaran: ")
    nilai = int(input("Nilai: "))
    sql = "INSERT INTO nilai (id_siswa, mata_pelajaran, nilai) VALUES (%s, %s, %s)"
    cursor.execute(sql, (id_siswa, mapel, nilai))
    db.commit()
    print("✅ Nilai berhasil ditambahkan.\n")

# Tampilkan data nilai
def lihat_nilai():
    print("\n--- Data Nilai ---")
    cursor.execute("""
        SELECT siswa.nama, siswa.kelas, nilai.mata_pelajaran, nilai.nilai
        FROM nilai
        JOIN siswa ON nilai.id_siswa = siswa.id_siswa
    """)
    hasil = cursor.fetchall()
    if hasil:
        for row in hasil:
            print(f"Nama: {row[0]} | Kelas: {row[1]} | Mapel: {row[2]} | Nilai: {row[3]}")
    else:
        print("Belum ada data nilai.")
    print()

# Input absensi
def input_absensi():
    id_siswa = input("ID Siswa: ")
    if not cek_id_siswa(id_siswa):
        print("❌ ID Siswa tidak ditemukan.\n")
        return
    tanggal = input("Tanggal (YYYY-MM-DD): ")
    status = input("Status (Hadir/Izin/Alpa): ")
    sql = "INSERT INTO absensi (id_siswa, tanggal, status) VALUES (%s, %s, %s)"
    cursor.execute(sql, (id_siswa, tanggal, status))
    db.commit()
    print("✅ Absensi berhasil ditambahkan.\n")

# Tampilkan data absensi
def lihat_absensi():
    print("\n--- Data Absensi ---")
    cursor.execute("""
        SELECT siswa.nama, absensi.tanggal, absensi.status
        FROM absensi
        JOIN siswa ON absensi.id_siswa = siswa.id_siswa
        ORDER BY absensi.tanggal DESC
    """)
    hasil = cursor.fetchall()
    if hasil:
        for row in hasil:
            print(f"Nama: {row[0]} | Tanggal: {row[1]} | Status: {row[2]}")
    else:
        print("Belum ada data absensi.")
    print()

# Menu utama
while True:
    print("\n=== MENU APLIKASI SEKOLAH ===")
    print("1. Tambah Siswa")
    print("2. Lihat Siswa")
    print("3. Input Nilai")
    print("4. Lihat Nilai")
    print("5. Input Absensi")
    print("6. Lihat Absensi")
    print("7. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_siswa()
    elif pilihan == "2":
        lihat_siswa()
    elif pilihan == "3":
        input_nilai()
    elif pilihan == "4":
        lihat_nilai()
    elif pilihan == "5":
        input_absensi()
    elif pilihan == "6":
        lihat_absensi()
    elif pilihan == "7":
        print("Keluar dari aplikasi.")
        break
    else:
        print("❌ Pilihan tidak valid.")