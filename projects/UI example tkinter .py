import tkinter as tk

score = 0
word = "Hello world"

def text():
    global word
    print(word)
    if(word == "Hello world"):
        label2.config(text="See you soon")
        word = "See you soon"
    else:
        label2.config(text="Hello world")
        word = "Hello world"

def points(score):
    label.config(text=str(score))

def score_up():
    global score
    score+=1
    points(score)

def score_down():
    global score
    score-=1
    points(score)

#----main---- 

root = tk.Tk()
root.title("Counting numbers and display text example")

#labels for show values
label = tk.Label(root, fg="dark green")
label.pack()
label2 = tk.Label(root, fg="green")
label2.pack()

#init first time
text()
points(score)

#Generate the IU buttons and link to the procedures 

button = tk.Button(root, text='score +1', width=25, command=score_up)
button.pack()

button = tk.Button(root, text='score -1', width=25, command=score_down)
button.pack()

button = tk.Button(root, text='Change word', width=25, command=text)
button.pack()

button = tk.Button(root, text='End', width=25, command=root.destroy)
button.pack()

#keep the IU working until end the program
root.mainloop()