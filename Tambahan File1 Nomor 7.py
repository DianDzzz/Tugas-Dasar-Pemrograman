# BTU HEAT CALCULATOR

# Konstanta
OIL_BARREL_GALLONS = 42
ENERGY_PER_BARREL_BTU = 5800000

# Meminta input dari pengguna untuk jumlah galon minyak dan efisiensi furnace
gallons_of_oil = float(input("Enter the number of gallons of oil burned: "))
efficiency = float(input("Enter the efficiency of the oil furnace (as a decimal): "))

# Menghitung jumlah BTU yang disalurkan
energy_per_gallon_btu = ENERGY_PER_BARREL_BTU / OIL_BARREL_GALLONS
total_energy_btu = gallons_of_oil * energy_per_gallon_btu
heat_delivered_btu = total_energy_btu * efficiency

# Menampilkan hasil perhitungan
print(f"\nTotal BTUs delivered to the house: {heat_delivered_btu:.2f} BTU")
