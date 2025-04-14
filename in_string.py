def check_vowels():
    nombre = input("Ingresá tu nombre: ")
    nombre = nombre.lower()
    contador = 0
    for letra in nombre:
        if letra in 'aeiou':
            contador += 1
    print(f"Tu nombre tiene {contador} vocales.")