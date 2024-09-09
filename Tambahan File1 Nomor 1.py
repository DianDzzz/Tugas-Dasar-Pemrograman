# Penghitung biaya taksi per mil

print("Penghitung biaya taksi!")
awal_odometer = float(input("Masukkan nilai awal odometer: "))  # Input dari pengguna untuk odometer awal dan akhir
akhir_odometer = float(input("Masukkan nilai akhir odometer "))

jarak = akhir_odometer - awal_odometer                          # Menghitung jarak yang ditempuh

tarif_per_mil = 1.50                                            # Tarif per mil

total_fare = jarak * tarif_per_mil                              # Menghitung total tarif

print(f"Kamu menempuh jarak sejauh {jarak:.1f} mil.")           # Menampilkan hasil perhitungan
print(f"dengan tarif ${tarif_per_mil:.2f} per mile, yang jarus anda bayar adalah ${total_fare:.2f}.")