def calcular_area_perimetro(base, altura):
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro

area, perimetro = calcular_area_perimetro(5, 10)
print(f"A area é {area} e o perímetro é {perimetro}")