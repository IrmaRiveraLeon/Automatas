adf = { 
'estados':  { 'P', 'Q', 'R'},
'alfabeto': {'a', 'b'},
'transiciones':     {
    'P': {'a': 'P', 'b': 'Q'},
    'Q': {'a': 'P', 'b': 'R'},
    'R': {'a': 'P', 'b': 'R'}
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

cadena = input("Escribe una cadena (admite a y b pero al final debe haber doble b): ")
if verificar(adf, cadena):
    print("Cadena válida ✅")
else:
    print("Cadena inválida ❌")
