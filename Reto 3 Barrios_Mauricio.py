car = {
    "brand":"ford",
    "model":"mustang",
    "year": 1964
}
 
x = car.keys()
print(x)

car["color"]="white"

print(x)

print(car["color"])

Producto={
    "Id":123,
    "Nombre":"Libreta",
    "Precio": 12.500,
    "Id_cat":1

},

{
    "Id":345,
    "Nombre":"Jabón",
    "Precio": 10.500,
    "Id_cat":2
}

Categoria={
    "Id":1,
    "Nombre":"Utilez Escolares",
},

{
    "id":2,
    "Nombre":"Aseo",
}

Resultante={
    "Id":123,
    "Nombre":"Libreta",
    "Categoría":"Utiles Escolares",

},

{
    "Id":345,
    "Nombre":"Jabón",
    "Categoría":"Aseo"
}

a =int(input("Ingrese la id del Producto a buscar"))

if a in Resultante:
    print(
        Producto
          
          )