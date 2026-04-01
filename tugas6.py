# Import & Setup
import numpy as np
import pandas as pd
import os

# Set seed untuk konsistensi
np.random.seed(42)

# NumPy – Data & Statistik
print("=== NUMPY ===")
# Buat array NumPy berisi nilai ujian (10 data)
nilai_ujian = np.random.randint(50, 100, 10)  # Nilai acak antara 50-99
print(f"Array nilai ujian: {nilai_ujian}")

# Hitung statistik
rata_rata = np.mean(nilai_ujian)
median = np.median(nilai_ujian)
std_dev = np.std(nilai_ujian)
nilai_min = np.min(nilai_ujian)
nilai_max = np.max(nilai_ujian)

print(f"Rata-rata: {rata_rata:.2f}")
print(f"Median: {median:.2f}")
print(f"Standar Deviasi: {std_dev:.2f}")
print(f"Nilai Minimum: {nilai_min}")
print(f"Nilai Maximum: {nilai_max}")

# pandas – DataFrame
print("\n=== PANDAS ===")
# Buat DataFrame dengan kolom nama, nim, nilai
data = {
    'nama': ['Ahmad', 'Siti', 'Budi', 'Dewi', 'Eko', 'Farah', 'Gunawan', 'Hana', 'Iwan', 'Julia'],
    'nim': ['2308561111', '2308561112', '2308561113', '2308561114', '2308561115', 
            '2308561116', '2308561117', '2308561118', '2308561119', '2308561120'],
    'nilai': nilai_ujian
}

df = pd.DataFrame(data)

# Tambahkan kolom status
df['status'] = np.where(df['nilai'] >= 70, 'LULUS', 'TIDAK LULUS')

# Tampilkan 5 baris pertama
print(df.head())

# File I/O – Tulis Ringkasan ke .txt
import pathlib, tempfile
print("\n=== FILE I/O ===")
script_dir = pathlib.Path(__file__).resolve().parent
output_dir = pathlib.Path(os.getenv('RINGKASAN_OUTPUT_DIR', script_dir))
print(f"Target folder output: {output_dir}")
output_dir.mkdir(parents=True, exist_ok=True)
ringkasan_path = output_dir / "ringkasan_tugas6.txt"

# helper tulis ringkasan
def tulis_ringkasan(path):
    with path.open('w', encoding='utf-8') as f:
        f.write("RINGKASAN STATISTIK NILAI UJIAN\n")
        f.write("="*40 + "\n\n")
        f.write("STATISTIK NUMPY:\n")
        f.write(f"Rata-rata: {rata_rata:.2f}\n")
        f.write(f"Median: {median:.2f}\n")
        f.write(f"Standar Deviasi: {std_dev:.2f}\n")
        f.write(f"Nilai Minimum: {nilai_min}\n")
        f.write(f"Nilai Maximum: {nilai_max}\n\n")
        f.write("RINGKASAN DATAFRAME:\n")
        f.write(f"Jumlah total baris: {len(df)}\n")
        f.write(f"Jumlah yang LULUS: {len(df[df['status'] == 'LULUS'])}\n")
        f.write(f"Jumlah yang TIDAK LULUS: {len(df[df['status'] == 'TIDAK LULUS'])}\n")
        f.write(f"Tingkat kelulusan: {len(df[df['status'] == 'LULUS'])/len(df)*100:.1f}%\n")

try:
    tulis_ringkasan(ringkasan_path)
    print(f"Ringkasan telah ditulis ke file: {ringkasan_path}")
except OSError as e:
    print(f"Gagal menulis file ringkasan di '{ringkasan_path}': {e}")
    try:
        ringkasan_path = pathlib.Path(tempfile.gettempdir()) / "ringkasan_tugas6.txt"
        tulis_ringkasan(ringkasan_path)
        print(f"Ringkasan ditulis ke temp folder: {ringkasan_path}")
    except OSError as e2:
        print(f"Gagal menulis file ringkasan di temp: {e2}")
        print("Ringkasan akan dicetak di layar sebagai fallback:\n")
        print("RINGKASAN STATISTIK NILAI UJIAN")
        print("="*40)
        print(f"Rata-rata: {rata_rata:.2f}")
        print(f"Median: {median:.2f}")
        print(f"Standar Deviasi: {std_dev:.2f}")
        print(f"Nilai Minimum: {nilai_min}")
        print(f"Nilai Maximum: {nilai_max}")
        print(f"Jumlah total baris: {len(df)}")
        print(f"Jumlah yang LULUS: {len(df[df['status'] == 'LULUS'])}")
        print(f"Jumlah yang TIDAK LULUS: {len(df[df['status'] == 'TIDAK LULUS'])}")
        print(f"Tingkat kelulusan: {len(df[df['status'] == 'LULUS'])/len(df)*100:.1f}%")
        ringkasan_path = None

# OOP Sederhana
class GradeBook:
    def __init__(self, df: pd.DataFrame): 
        self.df = df
    
    def average(self) -> float:
        """Menghitung rata-rata kolom nilai"""
        return float(self.df['nilai'].mean())
    
    def pass_rate(self, threshold: float = 70.0) -> float:
        """Menghitung persentase kelulusan"""
        passed = len(self.df[self.df['nilai'] >= threshold])
        total = len(self.df)
        return (passed / total) * 100
    
    def save_summary(self, path: str):
        """Menulis ringkasan ke file .txt (append mode)"""
        with open(path, 'a', encoding='utf-8') as f:
            f.write("\n\n" + "="*40 + "\n")
            f.write("RINGKASAN DARI GRADEBOOK OOP:\n")
            f.write("="*40 + "\n")
            f.write(f"Jumlah data: {len(self.df)}\n")
            f.write(f"Rata-rata nilai: {self.average():.2f}\n")
            f.write(f"Tingkat kelulusan: {self.pass_rate():.1f}%\n")
            f.write(f"Threshold kelulusan: 70.0\n")
    
    def __str__(self) -> str:
        """String ringkas memuat jumlah data & rata-rata"""
        return f"GradeBook({len(self.df)} data, rata-rata: {self.average():.2f})"

# Demo
if __name__ == "__main__":
    print("\n=== OOP: GRADEBOOK ===")
    
    # Buat objek GradeBook
    gradebook = GradeBook(df)
    
    # Tampilkan informasi objek
    print(f"Objek GradeBook: {gradebook}")
    print(f"Rata-rata nilai: {gradebook.average():.2f}")
    print(f"Tingkat kelulusan: {gradebook.pass_rate():.1f}%")
    
    # Simpan ringkasan ke file (append)
    if ringkasan_path:
        gradebook.save_summary(ringkasan_path)
        print(f"Ringkasan GradeBook telah ditambahkan ke file: {ringkasan_path}")
    else:
        print("Ringkasan GradeBook tidak disimpan karena masalah file sebelumnya.")
    
    print("\n=== PROGRAM SELESAI ===")