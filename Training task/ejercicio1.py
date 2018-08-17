import _datetime
nombre = input("como te llamas?")
edad = int(input("cuantos años tienes?"))

now = _datetime.datetime.now()
#print (now.year)
calculo= str((100-edad)+now.year)
print("hola "+nombre+" vas a cumplir 100 años para "+calculo)

repetir = int(input("Cuantas veces te lo repito?"))

for x in range(repetir):
    print(calculo)