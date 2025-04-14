def check_vowels(nombre):
    nombre_lower = nombre.lower()
    resultados = {
        "a": "a" in nombre_lower,
        "e": "e" in nombre_lower,
        "i": "i" in nombre_lower,
        "o": "o" in nombre_lower,
        "u": "u" in nombre_lower,
    }
    return resultados

if __name__ == "__main__":
    nombre_usuario = input("Ingresa un nombre: ")
    resultados_usuario = check_vowels(nombre_usuario)
    for vocal, presente in resultados_usuario.items():
        print(f"Contiene {vocal}: {presente}")