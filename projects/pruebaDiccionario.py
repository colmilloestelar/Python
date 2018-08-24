#depeloped by Raul Villar
#You are free to use any of my scripts in github for any purpose.
#external libs: openpyxl
#Ddatos24A.xlsx is my xlsx file
#Extract data from Extel to generate a text file
#This scripts was used to solve a real work challenge in a small time.

import openpyxl
doc = openpyxl.load_workbook('Ddatos24A.xlsx')

#only has 1 sheet
sheet = doc.active

#i will collet dat from some cols, F, J,I,B,D and E
#varios(nombre) F, descripcion J, database B, locat1 C, locat2 D, loc3 E, formula I
varNombre = sheet['F']
varDescrip = sheet['J']
varFormula = sheet['I']
varLocal = sheet['B1':'C490']
varLocal2 = sheet['D1':'E490']

#my list to save the cols
nombre = []
descripcion = []
formula = []
localizacion = ['']

#this for combine the data in the correct format.
combinado = []

#collect all data to list
for v1 in varNombre:
    if (v1.value != None):
        nombre.append("Nombre: "+v1.value)

for v1 in varDescrip:
    if(v1.value != None):
        descripcion.append("Descripcion: "+v1.value)

for v1 in varFormula:
    if(v1.value != None):
        formula.append("Formula: "+v1.value)

for v1, v2 in varLocal:
    if(v1.value != None):
        localizacion.append("Localizacion: "+v1.value+"/"+v2.value)


cont = 1
for v1, v2 in varLocal2:
    if(v1.value != None):
        localizacion[cont] = localizacion[cont]+"/"+v1.value+"/"+v2.value
    cont+=1

#ahora combinar todoslosdatos en el formato correcto :
#nombre
#Definicion
#formula
#localizacion.
#clean the first field, i init the list with '' because a small problem on the first data bucle.
# "The compiler trows me error if i dont use '' in this col"
localizacion.remove('')

#debug for check the length all must be same length or the next loop will crash.
print("a"+str(len(nombre)))
print("b"+str(len(descripcion)))
print("c"+str(len(formula)))
print("d"+str(len(localizacion)))
print(localizacion)

cont = 0
for elem in nombre:
    combinado.append( elem + '\n\n' + descripcion[cont] + '\n\n' + formula[cont] + '\n\n' + localizacion[cont])
    cont+=1

#Generate the list in the correct format for end users.
#Save the data.
archivo = open('diccionario.txt', 'w')

for item in combinado:
    archivo.write("%s\n\n" % item +"\n -----------------------------\n")



