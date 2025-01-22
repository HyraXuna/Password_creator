import string
from random import randint, choice
from tkinter import *

def generate_password():
    password_min=8
    password_max=16
    all_chars= string.ascii_letters + string.digits + string.punctuation
    password="".join(choice(all_chars) for x in range(randint(password_min,password_max)))
    password_entry.delete(0,END)
    password_entry.insert(0, password)
    

#créer fenêtre
window = Tk()
window.title("Générateur de mot de passe")
window.geometry("1080x720")
window.config(bg='#696969')


#créer la frame principale
frame=Frame(window, bg='#696969')

#création d'image
width=500
height=500
image = PhotoImage(file="image_mdp.png").zoom(25).subsample(25)
canvas = Canvas(frame, width=width, height=height, bg='#696969', bd=10,highlightbackground = "#00FF00", highlightcolor='#00FF00')
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

#créer un sous boite
right_frame=Frame(frame, bg='#696969')

#créer un titre
label_title=Label(right_frame, text="Mot de passe", font=("Arial", 30), bg='#696969', fg='#00FF00')
label_title.pack()

#créer un champ
password_entry=Entry(right_frame, font=("Arial", 30), bg='#696969', fg='#00FF00')
password_entry.pack()

#créer un bouton
generate_password_button=Button(right_frame, text="Générer", font=("Arial", 40), bg='#696969', fg='#00FF00', command=generate_password)
generate_password_button.pack(fill=X)

#on place la sous boite à droite de la frame principale
right_frame.grid(row=0, column=1, sticky=W)


#afficher la frame
frame.pack(expand=YES)

#afficher fenêtre
window.mainloop()
