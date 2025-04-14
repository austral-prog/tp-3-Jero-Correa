def slice_advanced(texto):
    resultado = texto[4::2]
    return resultado

if __name__ == "__main__":
    texto_usuario = input("Ingrese texto: ")
    resultado_usuario = slice_advanced(texto_usuario)
    print(resultado_usuario)