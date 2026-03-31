# ================================
# DEKLARASI VARIABEL DAN TIPE DATA
# ================================

nama_mahasiswa = "Stefani Kelin"                                              # String
umur = 20                                                                   # Integer
ipk = 3.60                                                                 # Float
status_mahasiswa = True                                                     # Boolean
mata_kuliah = ["Pemrograman", "Teknologi IOT ", "Basis Data", "Jaringan", "AI"] # List

print("=" * 50)
print("PROGRAM DEMONSTRASI TIPE DATA DAN OPERASI PYTHON")
print("=" * 50)

# ================================
# MANIPULASI STRING
# ================================
print("\n1. MANIPULASI STRING:")
print(f"Nama asli: {nama_mahasiswa}")
print(f"Panjang nama: {len(nama_mahasiswa)} karakter")
print(f"Nama huruf besar: {nama_mahasiswa.upper()}")
print(f"Nama huruf kecil: {nama_mahasiswa.lower()}")

# Menggabungkan string
gelar = "S.Kom"
nama_lengkap = nama_mahasiswa + ", " + gelar
print(f"Nama lengkap: {nama_lengkap}")

# ================================
# OPERASI MATEMATIKA SEDERHANA
# ================================
print("\n2. OPERASI MATEMATIKA:")
angka1 = 25
angka2 = 4

print(f"Angka1: {angka1}, Angka2: {angka2}")
print(f"Penjumlahan (+): {angka1} + {angka2} = {angka1 + angka2}")
print(f"Pengurangan (-): {angka1} - {angka2} = {angka1 - angka2}")
print(f"Perkalian (*): {angka1} * {angka2} = {angka1 * angka2}")
print(f"Pembagian (/): {angka1} / {angka2} = {angka1 / angka2}")
print(f"Floor Division (//): {angka1} // {angka2} = {angka1 // angka2}")
print(f"Modulo (%): {angka1} % {angka2} = {angka1 % angka2}")

# ================================
# LIST DAN AKSES ELEMEN
# ================================
print("\n3. OPERASI LIST:")
print(f"List mata kuliah awal: {mata_kuliah}")

# Tampilkan elemen tertentu
print(f"Elemen pertama: {mata_kuliah[0]}")
print(f"Elemen ketiga: {mata_kuliah[2]}")
print(f"Elemen terakhir: {mata_kuliah[-1]}")

# Tambahkan item baru
mata_kuliah.append("Machine Learning")
print(f"List setelah append 'Machine Learning': {mata_kuliah}")

# Hapus item dengan remove()
mata_kuliah.remove("Teknologi IOT ")
print(f"List setelah remove 'Teknologi IOT ': {mata_kuliah}")

# Hapus item dengan pop()
removed_item = mata_kuliah.pop(1)  # hapus elemen kedua
print(f"List setelah pop index 1: {mata_kuliah}")
print(f"Item yang dihapus: {removed_item}")

# ================================
# PENGGUNAAN INPUT DARI USER
# ================================
print("\n4. INPUT USER:")

# Minta user memasukkan nama dan umur
nama_user = input("Masukkan nama Anda: ")
try:
    umur_user = int(input("Masukkan umur Anda: "))
    
    # Cetak kalimat perkenalan
    print(f"\nHalo, nama saya {nama_user} dan umur saya {umur_user} tahun.")
    
    # Tambahan: validasi umur
    if umur_user < 0:
        print("Umur tidak valid!")
    elif umur_user < 17:
        print("Anda masih remaja.")
    elif umur_user < 60:
        print("Anda sudah dewasa.")
    else:
        print("Anda sudah lanjut usia.")
        
except ValueError:
    print("Error: Masukkan angka untuk umur!")

# ================================
# DEMONSTRASI TAMBAHAN
# ================================
print("\n5. DEMONSTRASI VARIABEL AWAL:")
print(f"Nama mahasiswa: {nama_mahasiswa}")
print(f"Umur: {umur} tahun")
print(f"IPK: {ipk}")
print(f"Status mahasiswa: {status_mahasiswa}")
print(f"Jumlah mata kuliah: {len(mata_kuliah)}")

print("\n" + "=" * 50)
print("PROGRAM SELESAI")
print("=" * 50)