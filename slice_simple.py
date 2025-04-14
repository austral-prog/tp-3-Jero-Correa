def slice_simple():
    texto = "Awesome"

    texto_lower = texto.lower()
    Punto_awe = texto_lower[0:3:1]
    Punto_eso = texto_lower[2:5:1]
    Punto_awesome = texto_lower[0:7:1]

    print(Punto_awe)
    print(Punto_eso)
    print(Punto_awesome)
slice_simple()

    #awe
    #eso
    #awesome
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
