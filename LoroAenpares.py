adf = { 
'estados':  { 'P', 'Q'},
'alfabeto': {'a', 'b'},
'transiciones':     {
    'P': {'a': 'Q', 'b': 'P'},
    'Q': {'a': 'P', 'b': 'Q'}
    }, 
    'estado_inicial': 'P',
    'estado_final': {'P'}
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

cadena = input("Escribe una cadena (admite a y b pero a debe ser pares): ")
if verificar(adf, cadena):
    print("Cadena válida ✅")
else:
    print("Cadena inválida ❌")

