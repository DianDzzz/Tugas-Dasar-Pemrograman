# FREEZER TEMPERATURE ESTIMATOR

# Meminta input dari pengguna untuk jam dan menit sejak kegagalan daya
hours = int(input("Enter hours since power failure: "))
minutes = int(input("Enter minutes since power failure: "))

# Mengonversi waktu total ke dalam jam (dengan menambahkan menit sebagai pecahan jam)
total_time_in_hours = hours + (minutes / 60)

# Menghitung suhu freezer menggunakan rumus yang diberikan
T = (4 * total_time_in_hours**2) / (total_time_in_hours + 2) - 20

# Menampilkan hasil suhu freezer
print(f"\nElapsed time: {total_time_in_hours:.2f} hours")
print(f"Estimated freezer temperature: {T:.2f} 'C")