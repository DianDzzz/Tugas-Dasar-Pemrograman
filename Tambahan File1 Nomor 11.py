# PYTHAGOREAN TRIPLE GENERATOR

# Meminta input dari pengguna untuk nilai m dan n
m = int(input("Enter the value for m (m > n): "))
n = int(input("Enter the value for n (n < m): "))

# Memastikan m lebih besar dari n
if m <= n:
    print("Error: m should be greater than n.")
else:
    # Menghitung sisi-sisi dan hipotenusa dari triple Pythagoras
    side1 = m**2 - n**2
    side2 = 2 * m * n
    hypotenuse = m**2 + n**2

    # Menampilkan hasil perhitungan
    print(f"\nPythagorean triple:")
    print(f"Side 1: {side1}")
    print(f"Side 2: {side2}")
    print(f"Hypotenuse: {hypotenuse}")
