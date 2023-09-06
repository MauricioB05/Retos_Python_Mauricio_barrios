def es_palindromo(palabra):
    
    palabra = palabra.replace(" ", "").lower()
    
  
    if palabra == palabra[::-1]:
        return True
    else:
        return False


entrada = input("Ingrese una palabra: ")


if es_palindromo(entrada):
    print(f"'{entrada}' es un palíndromo.")
else:
    print(f"'{entrada}' no es un palíndromo.")