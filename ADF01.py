adf = { 
'estados':  { 'P', 'Q', 'R'},
'alfabeto': {'0', '1'},
'transiciones':     {
    'P': {'0': 'Q', '1': 'P'},
    'Q': {'0': 'Q', '1': 'R'},
    'R': {'0': 'Q', '1': 'P'}
    }, 
    'estado_inicial': 'P',
    'estado_final': {'R'}
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

cadena = input("Escribe una cadena (admite 0 y 1): ")
if verificar(adf, cadena):
    print("Cadena válida ✅")
else:
    print("Cadena inválida ❌")

