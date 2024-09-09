# GRASS CUTTING TIME CALCULATOR

# Meminta input dari pengguna untuk panjang dan lebar halaman dan rumah
yard_length = float(input("Enter the length of the rectangular yard (in feet): "))
yard_width = float(input("Enter the width of the rectangular yard (in feet): "))
house_length = float(input("Enter the length of the rectangular house (in feet): "))
house_width = float(input("Enter the width of the rectangular house (in feet): "))

# Menghitung luas halaman dan rumah
yard_area = yard_length * yard_width
house_area = house_length * house_width

# Menghitung luas rumput yang perlu dipotong
grass_area = yard_area - house_area

# Laju pemotongan rumput dalam kaki persegi per detik
cutting_rate = 2  # square feet per second

# Menghitung waktu yang diperlukan untuk memotong rumput dalam detik
time_required_seconds = grass_area / cutting_rate

# Mengubah waktu ke dalam format menit dan detik
minutes = int(time_required_seconds // 60)
seconds = int(time_required_seconds % 60)

# Menampilkan hasil perhitungan
print(f"\nTime required to cut the grass: {minutes} minutes and {seconds} seconds")
