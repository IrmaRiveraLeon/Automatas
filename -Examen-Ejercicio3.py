afd = { 
    'estados':  {'P', 'Q', 'R'},
    'alfabeto': {'0', '1'},
    'transiciones': {
        'P': {'0': 'P', '1': 'Q'},
        'Q': {'0': 'P', '1': 'R'},
        'R': {'0': 'R', '1': 'R'}
    }, 
    'estado_inicial': 'P',
    'estado_final': {'P', 'Q'}  
}

def verificar(afd, cadena):
    estado_actual = afd['estado_inicial']
    for simbolo in cadena:
        if simbolo not in afd['alfabeto']:
            print(f"El símbolo '{simbolo}' no pertenece al alfabeto")
            return False
        estado_actual = afd['transiciones'][estado_actual][simbolo]
        print({simbolo}, estado_actual)
    return estado_actual in afd['estado_final']

cadena = input("Ingrese una cadena de 0 y 1 (Condición: No repita el 1 en la subcadena) \n")
if verificar(afd, cadena):
    print("✅ Cadena válida")
else:
    print("❌ Cadena inválida")
