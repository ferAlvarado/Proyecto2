from tkinter import *
from tkinter import ttk
import os

class aplicacion(): 
    def __init__(self):
        self.ventana_principal=Tk()
        self.ventana_principal.geometry('800x500')
        self.v_principal()
        self.ventana_principal.resizable(0,0)
        self.ventana_principal.title("Relaciones de Etimología")
        self.ventana_principal.mainloop()
    def v_principal(self):
        self.lbl_bienvenido = Label( self.ventana_principal, text="Bienvenido", font=("Helvetica", 16),relief=RAISED)
        self.lbl_bienvenido.pack()
        self.cmbox_opcion_value = StringVar()
        self.cmbox_opcion = ttk.Combobox(self.ventana_principal, textvariable=self.cmbox_opcion_value)
        self.cmbox_opcion['values'] =("Dos palabras","Palabra-Idioma","Idiomas")
        self.cmbox_opcion.current(0)
        self.cmbox_opcion.place(y=200,x=300)
        self.btn_opcion=Button(self.ventana_principal,text="LISTO",command=self.opciones)
        self.btn_opcion.place(y=240,x=305)
    def opciones(self):
        if (self.cmbox_opcion_value.get()=="Dos palabras"):
            self.dos_palabras_interfaz()
        elif (self.cmbox_opcion_value.get()=="Palabra-Idioma"):
            self.palabra_Idioma_interfaz()
        else:
            self.idioma_interfaz()
    def dos_palabras_interfaz(self):
        self.lbl_bienvenido["text"]="Dos palabras"
        self.cmbox_opcion.place(x=3000,y=3000)
        self.btn_opcion.place(x=3000,y=3000)
    def palabra_Idioma_interfaz(self):
        self.lbl_bienvenido["text"]="Palabra-Idioma"
        self.cmbox_opcion.place(x=3000,y=3000)
        self.btn_opcion.place(x=3000,y=3000)
    def idioma_interfaz(self):
        self.lbl_bienvenido["text"]="Idiomas"
        self.cmbox_opcion.place(x=3000,y=3000)
        self.btn_opcion.place(x=3000,y=3000)

def main():
    mi_app = aplicacion()
    return(0)

if __name__ == '__main__':
    main()
