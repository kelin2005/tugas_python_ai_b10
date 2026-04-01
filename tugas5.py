def greet(nama: str) -> str:
    """Mengembalikan teks sapaan: 'Halo, <nama>!'."""
    return f"Halo, {nama}!"

def tambah(a: float, b: float = 0.0) -> float:
    """Mengembalikan hasil penjumlahan a + b."""
    return a + b

def rata_rata(angka: list[float]) -> float:
    """Jika list kosong, kembalikan 0.0. Selain itu, kembalikan rata-rata (2 angka di belakang koma)."""
    if not angka:
        return 0.0
    return round(sum(angka) / len(angka), 2)

class Student:
    """Class untuk merepresentasikan mahasiswa."""
    
    def __init__(self, nama: str, nim: str):
        self.nama = nama
        self.nim = nim
        self.nilai: list[float] = []
    
    def tambah_nilai(self, skor: float) -> None:
        """Menambah satu nilai ke list."""
        self.nilai.append(skor)
    
    def rata_nilai(self) -> float:
        """Rata-rata nilai (pakai function rata_rata() di atas)."""
        return rata_rata(self.nilai)
    
    def status(self, threshold: float = 70.0) -> str:
        """'LULUS' jika rata-rata ≥ threshold, selain itu 'TIDAK LULUS'."""
        avg = self.rata_nilai()
        return "LULUS" if avg >= threshold else "TIDAK LULUS"
    
    def __str__(self) -> str:
        """Kembalikan string ringkas seperti: 'Student(nama='Budi', nim='A123', rata=82.5, status=LULUS)'"""
        return f"Student(nama='{self.nama}', nim='{self.nim}', rata={self.rata_nilai()}, status={self.status()})"

if __name__ == "__main__":
    print("=== FUNCTIONS ===")
    
    # Demo fungsi greet
    print(f"greet('Arifian'): {greet('Arifian')}")
    
    # Demo fungsi tambah
    print(f"tambah(5, 7): {tambah(5, 7)}")
    print(f"tambah(10): {tambah(10)}")
    
    # Demo fungsi rata_rata
    print(f"rata_rata([80, 90, 100]): {rata_rata([80, 90, 100])}")
    print(f"rata_rata([]): {rata_rata([])}")
    
    print("\n=== CLASS STUDENT ===")
    
    # Buat 2 mahasiswa
    student1 = Student("Budi", "A123")
    student2 = Student("Ani", "A456")
    
    # Tambah nilai
    student1.tambah_nilai(85)
    student1.tambah_nilai(90)
    student1.tambah_nilai(78)
    
    student2.tambah_nilai(65)
    student2.tambah_nilai(70)
    student2.tambah_nilai(68)
    
    # Cetak objek (akan memanggil __str__)
    print(student1)
    print(student2)
    
    # Cetak rata-rata dan status
    print(f"{student1.nama} - Rata-rata: {student1.rata_nilai()}, Status: {student1.status()}")
    print(f"{student2.nama} - Rata-rata: {student2.rata_nilai()}, Status: {student2.status()}")