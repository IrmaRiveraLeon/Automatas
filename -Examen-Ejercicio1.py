adf = { 
'estados':  { 'P', 'Q', 'R', 'S'},
'alfabeto': {'0', '1'},
'transiciones':     {
    'P': {'0': 'Q', '1': 'P'},
    'Q': {'0': 'Q', '1': 'R'},
    'R': {'0': 'S', '1': 'R'},
    'S': {'0': 'S', '1': 'R'}
    }, 
    'estado_inicial': 'P',
    'estado_final': {'S'}
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

cadena = input("Escriba una cadena de '0' y '1' (Condición: Debe de contener subcadena '01' y debe terminar en 0 \n")
if verificar(adf, cadena):
    print("Cadena válida ✅")
else:
    print("Cadena inválida ❌")

