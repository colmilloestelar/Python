#Filter logs v2.0 - Filter data from huge data text and generate CSV friendly file
import glob
import os
import fileinput
import itertools

path = 'Badmail'

total = 0
x = ["Nombre Fichero; Fecha; Alerta; Correos; Archivo Enviado;  \n"]

for filename in glob.glob(os.path.join(path, '*.BAD')):
    total+=1 #control how much files we read - Debug only.
    date=1
    cont=0 #used to avoid copy wrong mails from first list.
    with open(filename) as f:
        nam = str(filename)
        x.append(nam[8:])
        #x.append(";")

        preline="--"
        for line in itertools.islice(f, 0, 100):
            if not "From" in line\
                    and not "Final" in line\
                    and not "Return" in line\
                    and not "Encoding:" in line\
                    and not "Cc:" in line\
                    and not "Message-ID" in line \
                    and not "Arrival" in line\
                    and not "Subject" in line:

                    if "Date:" in line\
                            and date==1:
                        date=2 # we alrready have date, avoid duplicate
                        line2 = str(line)
                        line2 = line2.replace('\n','')
                        line2 = line2.replace('Date:', '')

                        z = list(line2[6:17])

                        if " " in z[1]:
                            z.insert(0,'0')
                            z[2] = '/'
                            z[6] = '/'
                            z[11]=""
                            x.append(';' + "".join(z))
                        else:
                            z[2]='/'
                            z[6]='/'
                            x.append(';'+"".join(z))

                    if "following" in line:
                        line2 = str(line)
                        line2 = line2.replace('\n', '')
                        x.append(";"+line2 + ";")

                    if "@" in line:
                        if not "," in line \
                                and not "To:" in line\
                                and not "ignore" in preline:
                            line2 = str(line)
                            line2 = line2.replace('\n', '')
                            line2 = line2.replace(' ','')
                            x.append(line2)
                            x.append('|')
                        if "To:" in line:
                            preline="ignore"
                            cont=0 #set to 0 for ignore next close lines.

                    if "pdf;" in line:
                        if not '.pdf' in line:
                            line2 = str(line)
                            line2 = line2.replace('\n', '')
                            line2 = line2.replace('pdf;','pdf')
                            line2 = line2.replace('Content-Type: application/pdf name=', ';')
                            x.append(line2)

                    if ".pdf" in line:
                        line2 = str(line)
                        line2 = line2.replace('\n', '')
                        line2 = line2.replace('pdf;', 'pdf')
                        #line2 = line2.replace('=', ':')
                        line2 = line2.replace('Content-Type: application/pdf name=', ';')
                        x.append(line2 + ";")

                    #Counter used to avoid get mails in the next 2 lines after 'To:'
                    cont+=1
                    if cont>=2 :
                        preline="" #after 2 lines we can get more mails


    x.append("\n")
print(total)
print (x)



#Save the data.
archivo = open('filtro.csv', 'w')

for item in x:
    archivo.write("%s" % item)

f.close()
archivo.close()

#clean |; in last mail
print(" - -- -- - - - - ")
z=[]
with open('filtro.csv') as a1:

    for line in a1:
        line2 = line.replace('|;',';')
        z.append(line2)
        print(line2)

a2 = open('filtro.csv', 'w')

for item in z:
    a2.write("%s" % item)