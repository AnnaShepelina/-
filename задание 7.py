def calculate_cylinder_volume(radius, height):
    volume = 3.14159 * radius ** 2 * height
    return volume


volume1 = calculate_cylinder_volume(2, 5)
volume2 = calculate_cylinder_volume(3, 10)
volume3 = calculate_cylinder_volume(1.5, 7)

print("Объем цилиндра 1:", volume1)
print("Объем цилиндра 2:", volume2)
print("Объем цилиндра 3:", volume3)
