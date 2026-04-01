# ==============================================================================
# DEMONSTRASI STRUKTUR DATA PYTHON
# ==============================================================================

print("=" * 60)
print("DEMONSTRASI STRUKTUR DATA PYTHON")
print("=" * 60)

# ==============================================================================
# 1. LIST – AKSES & MANIPULASI
# ==============================================================================
print("\n1. LIST – AKSES & MANIPULASI")
print("-" * 40)

# Membuat list dengan ≥ 6 elemen campuran
data_list = ["apel", 25, "jeruk", 3.14, "mangga", 42, "pisang"]
print(f"List awal: {data_list}")

# Menampilkan elemen pertama & terakhir
print(f"Elemen pertama: {data_list[0]}")
print(f"Elemen terakhir: {data_list[-1]}")

# Slicing [start:stop:step]
print(f"Slicing [1:5]: {data_list[1:5]}")
print(f"Slicing [::2]: {data_list[::2]}")
print(f"Slicing [::-1]: {data_list[::-1]}")

# Operasi manipulasi
print("\nOperasi manipulasi list:")
print(f"Sebelum manipulasi: {data_list}")

# append() - menambah di akhir
data_list.append("semangka")
print(f"Setelah append('semangka'): {data_list}")

# insert() - menyisipkan di posisi tertentu
data_list.insert(2, "anggur")
print(f"Setelah insert(2, 'anggur'): {data_list}")

# extend() - menambahkan multiple elements
data_list.extend(["kiwi", "melon"])
print(f"Setelah extend(['kiwi', 'melon']): {data_list}")

# pop() - menghapus dan mengembalikan elemen terakhir
removed = data_list.pop()
print(f"Setelah pop(): {data_list} (removed: {removed})")

# remove() - menghapus elemen pertama yang cocok
data_list.remove("apel")
print(f"Setelah remove('apel'): {data_list}")

# ==============================================================================
# 2. TUPLE – IMMUTABILITY & UNPACKING
# ==============================================================================
print("\n\n2. TUPLE – IMMUTABILITY & UNPACKING")
print("-" * 40)

# Membuat tuple dengan ≥ 5 elemen
data_tuple = ("John Doe", 12345, "Informatika", "Jakarta", 3.8)
print(f"Tuple: {data_tuple}")

# Menampilkan panjang
print(f"Panjang tuple: {len(data_tuple)}")

# Akses indeks
print(f"Elemen indeks 0: {data_tuple[0]}")
print(f"Elemen indeks 2: {data_tuple[2]}")

# Unpacking dengan *rest
nama, nim, jurusan, *rest = data_tuple
print(f"Nama: {nama}")
print(f"NIM: {nim}")
print(f"Jurusan: {jurusan}")
print(f"Rest: {rest}")

# Unpacking minimal 3 variabel
first, second, third, fourth, fifth = data_tuple
print(f"First: {first}, Second: {second}, Third: {third}")

# ==============================================================================
# 3. SET – KEUNIKAN & OPERASI HIMPUNAN
# ==============================================================================
print("\n\n3. SET – KEUNIKAN & OPERASI HIMPUNAN")
print("-" * 40)

# Membuat dua set dengan elemen tumpang tindih
set1 = {1, 2, 3, 4, 5, "apel", "jeruk"}
set2 = {4, 5, 6, 7, 8, "jeruk", "mangga"}
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Union (|)
union_set = set1 | set2
print(f"Union: {union_set}")

# Intersection (&)
intersection_set = set1 & set2
print(f"Intersection: {intersection_set}")

# Difference (-)
diff1 = set1 - set2
diff2 = set2 - set1
print(f"Set1 - Set2: {diff1}")
print(f"Set2 - Set1: {diff2}")

# Symmetric difference (^)
sym_diff = set1 ^ set2
print(f"Symmetric difference: {sym_diff}")

# Menunjukkan duplikat otomatis hilang
duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_set = set(duplicates)
print(f"List dengan duplikat: {duplicates}")
print(f"Set (duplikat hilang): {unique_set}")

# ==============================================================================
# 4. DICTIONARY – KEY/VALUE DASAR
# ==============================================================================
print("\n\n4. DICTIONARY – KEY/VALUE DASAR")
print("-" * 40)

# Membuat dict data mahasiswa
mahasiswa = {
    "nama": "Stefani Kelin Martha Ampak",
    "nim": "2308561119",
    "angkatan": 2023,
    "kota": "Bali"
}
print(f"Data mahasiswa: {mahasiswa}")

# Tambah key baru
mahasiswa["jurusan"] = "Informatika"
print(f"Setelah tambah jurusan: {mahasiswa}")

# Ubah nilai key
mahasiswa["kota"] = "Bali"
print(f"Setelah ubah kota: {mahasiswa}")

# Hapus key
del mahasiswa["angkatan"]
print(f"Setelah hapus angkatan: {mahasiswa}")

# Tampilkan keys(), values(), items()
print(f"Keys: {list(mahasiswa.keys())}")
print(f"Values: {list(mahasiswa.values())}")
print(f"Items: {list(mahasiswa.items())}")

# Iterasi menampilkan key: value
print("\nIterasi key: value:")
for key, value in mahasiswa.items():
    print(f"  {key}: {value}")

# ==============================================================================
# 5. NESTED STRUCTURES
# ==============================================================================
print("\n\n5. NESTED STRUCTURES")
print("-" * 40)

# Membuat list berisi ≥ 4 dict (daftar buku)
daftar_buku = [
    {"judul": "Cantik Itu Luka", "penulis": "Eka Kurniawan", "tahun": 2016},
    {"judul": "Laut Bercerita", "penulis": "Leila S. Chudori", "tahun": 2020},
    {"judul": "Bumi Manusia", "penulis": "Pramoedya Ananta Toer", "tahun": 2019},
    {"judul": "Dongeng dari negeri awan", "penulis": "Kak Aini", "tahun": 2024},
    {"judul": "Kisah dari Lautan Pasifik: Dongeng Pulau ke Pulau", "penulis": "Kak Ipang", "tahun": 2025}
]
print("Daftar buku:")
for i, buku in enumerate(daftar_buku, 1):
    print(f"  {i}. {buku['judul']} ({buku['tahun']})")

# Cetak semua judul dengan loop
print("\nSemua judul buku:")
for buku in daftar_buku:
    print(f"  - {buku['judul']}")

# Filter buku terbit ≥ tahun tertentu menggunakan list comprehension
tahun_min = 2025
buku_modern = [buku for buku in daftar_buku if buku["tahun"] >= tahun_min]
print(f"\nBuku terbit ≥ {tahun_min}:")
for buku in buku_modern:
    print(f"  - {buku['judul']} ({buku['tahun']})")

# ==============================================================================
# 6. COMPREHENSION & UTILITAS
# ==============================================================================
print("\n\n6. COMPREHENSION & UTILITAS")
print("-" * 40)

# List comprehension: daftar angka 1–20, buat list genap dan list kuadrat
angka = list(range(1, 21))
genap = [x for x in angka if x % 2 == 0]
kuadrat = [x**2 for x in angka]
print(f"Angka 1-20: {angka}")
print(f"Genap: {genap}")
print(f"Kuadrat: {kuadrat}")

# Dict comprehension: mapping {angka: "genap"/"ganjil"} untuk 1–10
paritas = {x: "genap" if x % 2 == 0 else "ganjil" for x in range(1, 11)}
print(f"\nParitas 1-10: {paritas}")

# Set comprehension: huruf unik (lowercase) dari sebuah kalimat
kalimat = "Hello World! Python Programming is Fun and Exciting"
huruf_unik = {char.lower() for char in kalimat if char.isalpha()}
print(f"Huruf unik dari kalimat: {sorted(huruf_unik)}")

# ==============================================================================
# 7. KEANGGOTAAN & PENCARIAN SEDERHANA
# ==============================================================================
print("\n\n7. KEANGGOTAAN & PENCARIAN SEDERHANA")
print("-" * 40)

# Data untuk testing
test_list = ["apel", "jeruk", "mangga", "pisang", "anggur"]
test_set = {"apple", "orange", "banana", "grape", "watermelon"}

# Cek keanggotaan (in) pada list
print(f"List: {test_list}")
print(f"'apel' in list: {'apel' in test_list}")
print(f"'durian' in list: {'durian' in test_list}")

# Cek keanggotaan (in) pada set
print(f"\nSet: {test_set}")
print(f"'apple' in set: {'apple' in test_set}")
print(f"'mango' in set: {'mango' in test_set}")

# Gunakan index() untuk melaporkan posisi item
print(f"\nPosisi item dalam list:")
try:
    posisi_mangga = test_list.index("mangga")
    print(f"'mangga' ditemukan di indeks: {posisi_mangga}")
except ValueError:
    print("'mangga' tidak ditemukan dalam list")

try:
    posisi_durian = test_list.index("durian")
    print(f"'durian' ditemukan di indeks: {posisi_durian}")
except ValueError:
    print("'durian' tidak ditemukan dalam list")

# Pencarian ringkas dengan if-else
item_to_find = "pisang"
result = f"ditemukan di indeks {test_list.index(item_to_find)}" if item_to_find in test_list else "tidak ditemukan"
print(f"\nPencarian '{item_to_find}': {result}")

item_to_find2 = "strawberry"
result2 = f"ditemukan" if item_to_find2 in test_set else "tidak ditemukan"
print(f"Pencarian '{item_to_find2}' dalam set: {result2}")

print("\n" + "=" * 60)
print("DEMONSTRASI SELESAI")
print("=" * 60)