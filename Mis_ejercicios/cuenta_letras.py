def f_cuenta_letras(text:str):
    """funcion la cantidad de letras v que aparecen en un texto
    """
    text_minusculas:str=text.lower()
    cantidad_letras=0
    for n in text_minusculas:
        if n == "v":
            cantidad_letras+=1
    return cantidad_letras