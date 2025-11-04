adf = { 
'estados':  { 'P', 'Q', 'R'},
'alfabeto': {'a', 'b'},
'transiciones':     {
    'P': {'a': 'P', 'b': 'Q'},
    'Q': {'a': 'Q', 'b': 'R'},
    'R': {'a': 'R', 'b': 'Q'},
    }, 
    'estado_inicial': 'P',
    'estado_final': {'Q'}
}

def verificar(adf, cadena):
    estado_actual = adf['estado_inicial']
    for simbolo in cadena:
        if simbolo not in adf['alfabeto']:
            print(f"El símbolo '{simbolo}' no pertenece al alfabeto")
            return False
        estado_actual = adf['transiciones'][estado_actual][simbolo]
        print({simbolo}, estado_actual)
    return estado_actual in adf['estado_final']

cadena = input("Escriba una cadena de 'a' y 'b' (Condición: Debe de contener una cantidad impar de símbolos de 'b' \n")
if verificar(adf, cadena):
    print("Cadena válida")
else:
    print("Cadena inválida")
