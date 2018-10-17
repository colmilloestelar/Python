#Filter logs Power BI v1.1 - Filter data from large data text in old format and generate 2 separated CSV friendly file
import glob
import os
import fileinput
import re
import itertools
import shutil
import datetime

now = datetime.datetime.now() #Used to get data and create a new file every day without overwrite
path = '..\LogFiles' #Data directory.
path2 = 'LogSaves' #save directory

contar = 0
x = ["Nombre fichero; Tipo; Fecha; Hora; Datos;\n"] #reporting
y = ["Nombre Fichero; Fecha; Hora; Tipo; Información;\n"]#Rsp
copiar = []
#aux vars to build a list
a1 = ''
a2 = ''
a3 = ''
a4 = ''

def logReporting():
    for filename in glob.glob(os.path.join(path, 'Repo*.log')):
        f = open(filename, 'r', encoding='utf16') #this file need to encode to utf16
        print(filename)
        filename2 = filename[12:]

        for line in f:
            if "schedule!" in line:  # format correctly
                a1 = line[0:8]
                a2 = line[32:42]

                if "8" in line[40]:
                    a2 = line[31:41]
                if "-" in line[40]:
                    a2 = line[30:40]
                if "-" in line[39]:
                    a2 = line[29:39]
                if "-" in line[38]:
                    a2 = line[28:38]
                if "-" in line[37]:
                    a2 = line[27:37]

                a3 = line[42:47]
                if ":" in line[45]:
                    a3 = line[43:48]
                if ":" in line[44]:
                    a3 = line[42:47]
                if ":" in line[43]:
                    a3 = line[41:46]
                if ":" in line[42]:
                    a3 = line[40:45]

                a4 = line[59:]
                if " " in line[59]:
                    a4 = line[60:]
                if " " in line[60]:
                    a4 = line[61:]
                if " " in line[61]:
                    a4 = line[62:]
                if " " in line[62]:
                    a4 = line[63:]

                x.append(filename2 + ';' + a1 + ';' + a2 + ';' + a3 + ';' + a4)

            if "library!" in line:  # Formateado bien
                a1 = line[0:7]
                a2 = line[31:41]

                if "8" in line[39]:
                    a2 = line[30:40]
                if "-" in line[39]:
                    a2 = line[29:39]
                if "-" in line[38]:
                    a2 = line[28:38]
                if "-" in line[37]:
                    a2 = line[27:37]
                if "-" in line[36]:
                    a2 = line[26:36]

                a3 = line[41:46]

                if ":" in line[44]:
                    a3 = line[42:47]
                if ":" in line[43]:
                    a3 = line[41:46]
                if ":" in line[42]:
                    a3 = line[40:45]
                if ":" in line[41]:
                    a3 = line[39:44]

                a4 = line[56:]
                if " " in line[56]:
                    a4 = line[57:]
                if " " in line[57]:
                    a4 = line[58:]
                if " " in line[58]:
                    a4 = line[59:]
                if " " in line[59]:
                    a4 = line[60:]
                if " " in line[60]:
                    a4 = line[61:]
                if " " in line[61]:
                    a4 = line[62:]

                x.append(filename2 + ';' + a1 + ';' + a2 + ';' + a3 + ';' + a4)

            if "notification!" in line:  # Formateado bien
                a1 = line[0:12]
                a2 = line[36:46]  # fecha

                if "8" in line[46]:
                    a2 = line[36:46]
                if "-" in line[46]:
                    a2 = line[36:46]
                if "-" in line[45]:
                    a2 = line[35:45]
                if "-" in line[44]:
                    a2 = line[34:44]
                if "-" in line[43]:
                    a2 = line[33:43]

                a3 = line[46:51]  # hora
                if ":" in line[49]:
                    a3 = line[47:52]
                if ":" in line[48]:
                    a3 = line[46:51]
                if ":" in line[47]:
                    a3 = line[45:50]
                if ":" in line[46]:
                    a3 = line[44:49]

                a4 = line[63:]
                if " " in line[63]:
                    a4 = line[64:]
                if " " in line[64]:
                    a4 = line[65:]
                if " " in line[65]:
                    a4 = line[66:]

                x.append(filename2 + ';' + a1 + ';' + a2 + ';' + a3 + ';' + a4)

            if "dataextension!" in line:  # formateado bien
                a1 = line[0:13]
                a2 = line[37:47]  # fecha
                if "8" in line[47]:
                    a2 = line[37:47]
                if "-" in line[47]:
                    a2 = line[37:47]
                if "-" in line[46]:
                    a2 = line[36:46]
                if "-" in line[45]:
                    a2 = line[35:45]
                if "-" in line[44]:
                    a2 = line[34:44]

                a3 = line[47:52]  # hora
                if ":" in line[50]:
                    a3 = line[48:53]
                if ":" in line[49]:
                    a3 = line[47:52]
                if ":" in line[48]:
                    a3 = line[46:51]
                if ":" in line[47]:
                    a3 = line[45:50]

                a4 = line[64:]
                if " " in line[64]:
                    a4 = line[65:]
                if " " in line[65]:
                    a4 = line[66:]
                if " " in line[66]:
                    a4 = line[67:]

                x.append(filename2 + ';' + a1 + ';' + a2 + ';' + a3 + ';' + a4)

            if "processing!" in line:  #
                a1 = line[0:10]
                a2 = line[34:44]

                if "8" in line[42]:
                    a2 = line[33:43]
                if "-" in line[42]:
                    a2 = line[32:42]
                if "-" in line[41]:
                    a2 = line[31:41]
                if "-" in line[40]:
                    a2 = line[30:40]
                if "-" in line[39]:
                    a2 = line[29:39]

                a3 = line[44:49]
                if ":" in line[47]:
                    a3 = line[45:50]
                if ":" in line[46]:
                    a3 = line[44:49]
                if ":" in line[45]:
                    a3 = line[43:48]
                if ":" in line[44]:
                    a3 = line[42:47]

                a4 = line[61:]
                if " " in line[61]:
                    a4 = line[62:]
                if " " in line[62]:
                    a4 = line[63:]
                if " " in line[63]:
                    a4 = line[64:]
                if " " in line[64]:
                    a4 = line[65:]

                x.append(filename2 + ';' + a1 + ';' + a2 + ';' + a3 + ';' + a4)

    # Save the data.
    # x.append(schedule+library+notification+dataextension+processing)
    archivo = open(path2 + '\ ' + 'filtrologs' + str(now.day) + '-' + str(now.month) + '-' + str(now.year) + '.csv', 'w')

    for item in x:
        archivo.write("%s" % item)

    #f.close()
    archivo.close()
    return 0

def logRsp():
    for filename in glob.glob(os.path.join(path, 'Rsp*.log')):
        f = open(filename, 'r')
        filename2 = filename[12:]

        for line in f:
            cabecera = line[25:29]
            if 'INFO' in cabecera:
                a2 = line[0:10]
                a3 = line[12:16]

                a1 = line[29:32]
                a4 = line[32:]

                if '|' in line[32]:
                    a1 = line[29:33]
                    a4 = line[33:]
                if '|' in line[33]:
                    a1 = line[29:34]
                    a4 = line[34:]
                if '|' in line[34]:
                    a1 = line[29:35]
                    a4 = line[35:]
                if '|' in line[35]:
                    a1 = line[29:36]
                    a4 = line[36:]

                y.append(filename2 + ';' + a2 + ';' + a3 + ';' + a1 + ';' + a4)

    #save data.
    archivo = open(path2 + '\ ' +'filtrologsRSP' + str(now.day) + '-' + str(now.month) + '-' + str(now.year) + '.csv', 'w')

    for item in y:
        archivo.write("%s" % item)

    f.close()
    archivo.close()

logReporting()
logRsp()











