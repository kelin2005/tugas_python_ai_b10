from pathlib import Path
p = Path(r"C:\Users\acer\Documents\SEMESTER 6\python 6\tugas_python_ai_b10\ringkasan_tugas6.txt")
print('test path:', p)
try:
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('w', encoding='utf-8') as f:
        f.write('hello')
    print('write-success')
except Exception as e:
    import traceback
    traceback.print_exc()
