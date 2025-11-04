adf = { 
'estados':  { 'P', 'Q', 'R', 'S'},
'alfabeto': {'a', 'b'},
'transiciones':     {
    'P': {'a': 'Q', 'b': 'P'},
    'Q': {'a': 'Q', 'b': 'R'},
    'R': {'a': 'S', 'b': 'Q'},
    'S': {'a': 'Q', 'b': 'R'}
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

cadena = input("Escribe una cadena (admite a y b pero debe terminar en aba): ")
if verificar(adf, cadena):
    print("Cadena válida ✅")
else:
    print("Cadena inválida ❌")

