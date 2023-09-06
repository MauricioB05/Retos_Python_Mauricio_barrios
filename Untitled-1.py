a =float(input("ingrese a que hora ingresó al aparcamiento(en horario de 24)"))
b =float(input("Ingrese a que hora salió del aparcamiento "))
hora=b-a

d =int(input("Ingrese 1 si su día es Lunes, martes o miercoles - 2 si su día es jueves o viernes - 3 3 si su día es sabado o domingo  "))

resultado = int(0)

print("El tiempo en el aparcamiento fue de: ")
print(hora)

if d==1:
   resultado = 2*hora
print("Su precio a pagar es: ")
print(resultado)

if d==2:
   resultado = 2.5*hora
   print("Su precio a pagar es: ")
   print(resultado)

if d==3: 
   resultado= 3*hora
   print("Su precio a pagar es: ")
   print(resultado)

      


