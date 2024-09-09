# SECTION PREDICTION CALCULATOR

# Jumlah siswa yang dapat ditampung dalam satu bagian
students_per_section = 30

# Meminta input dari pengguna untuk jumlah siswa terdaftar
total_students = int(input("Enter the number of students enrolled: "))

# Menghitung jumlah bagian yang diperlukan dan sisa siswa
num_sections = total_students // students_per_section
remaining_students = total_students % students_per_section

# Menampilkan hasil perhitungan
print(f"\nNumber of students enrolled: {total_students}")
print(f"Number of sections required: {num_sections}")
print(f"Number of students left over: {remaining_students}")
