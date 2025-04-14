def check_vowels():
    nombre = input("Ingresa un nombre: ")
    nombre_lower = nombre.lower()

    print(f"Contiene a {'a' in nombre_lower}")
    print(f"Contiene e: {'e' in nombre_lower}")
    print(f"Contiene i: {'i' in nombre_lower}")
    print(f"Contiene o: {'o' in nombre_lower}")
    print(f"Contiene u: {'u' in nombre_lower}")

# Para probarlo, puedes llamar a la función:
check_vowels()


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`

