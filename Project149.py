
from tkinter import *
import random

root= Tk()
root.title("Random Word Generator")
root.geometry("500x500")

label1 = Label(root)

def random_text():
    alphalist = ["A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J" , "K" , "L" , "M" , "N" , "O" , "P" , "Q" , "R" , "S" , "T" , "U" , "V" , "W" , "X" , "Y" , "Z"]
    random_no1 = random.randint(0, 25)
    random_no2 = random.randint(0, 25)
    random_no3 = random.randint(0, 25)
    random_no4 = random.randint(0, 25)
    random_alpha1 = alphalist[random_no1]
    random_alpha2 = alphalist[random_no2]
    random_alpha3 = alphalist[random_no3]
    random_alpha4 = alphalist[random_no4]
    
    label1["text"] = random_alpha1+random_alpha2+random_alpha3+random_alpha4
    
    
btn1 = Button(root)
btn1 = Button(root, text="Generated Random Words", command = random_text())
btn1.place(relx = 0.5, rely = 0.5, anchor= CENTER)
label1.place(relx = 0.5, rely = 0.8, anchor= CENTER)

root.mainloop()