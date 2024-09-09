# IV INFUSION CALCULATOR

# Meminta input dari pengguna untuk volume cairan dalam ml dan waktu infus dalam menit
volume_ml = float(input("Volume to be infused (ml) => "))
infusion_minutes = float(input("Minutes over which to infuse => "))

# Menghitung laju infus dalam ml/jam
infusion_rate_ml_per_hour = (volume_ml / infusion_minutes) * 60

# Menampilkan hasil perhitungan
print(f"\nVTBI: {volume_ml:.0f} ml")
print(f"Rate: {infusion_rate_ml_per_hour:.0f} ml/hr")