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



# Para probarlo, puedes llamar a la función:
check_vowels()


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`

