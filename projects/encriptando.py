F = open('workfile.txt','w')

key = 'abcdefghijklmnopqrstuvwxyz' #characters for encode

#ini
def f_basic(text):
    text2 ='' #store encoded input
    n=1 #this number must be betwen1 and max len of the key, this chose the encode displacement
    keyl = len(key) #obtain key length

    #this funcion replace every position based on the key and n
    for l in text.lower():
        try:
            i = (key.index(l) + n) % keyl
            text2 += key[i]
        except ValueError:
            text2 += l

    return text2.lower()

#main
print("Write your text for a basic encode")
word = input()

print("encripting..."+word)

word2 = f_basic(word)

print("Encripted word is: "+word2)

#end
F.close()
