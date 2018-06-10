from tkinter import *
from tkinter import ttk
import os

class aplicacion(): 
    def __init__(self):
        self.ventana_principal=Tk()
        self.ventana_principal.geometry('800x500')
        self.componentes_interfaz()
        self.v_principal()
        self.ventana_principal.resizable(0,0)
        self.ventana_principal.title("Relaciones de Etimología")
        menubar = Menu(self.ventana_principal)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.v_principal())
        filemenu.add_command(label="Open", command=self.v_principal())
        filemenu.add_command(label="Save", command=self.v_principal())
        filemenu.add_command(label="Save as...", command=self.v_principal())
        filemenu.add_command(label="Close", command=self.v_principal())
        filemenu.add_separator()
        self.ventana_principal.mainloop()
    def componentes_interfaz(self):
        """Comonentes principales"""
        self.lbl_bienvenido = Label( self.ventana_principal, text="Bienvenido", font=("Helvetica", 16),relief=RAISED)
        self.cmbox_opcion_value = StringVar()
        self.cmbox_opcion = ttk.Combobox(self.ventana_principal, textvariable=self.cmbox_opcion_value)
        self.cmbox_opcion['values'] =("Dos palabras","Palabra-Idioma","Idiomas")
        self.cmbox_opcion.current(0)
        self.btn_opcion=Button(self.ventana_principal,text="LISTO",command=self.opciones)
        """Componentes de dos palabras"""
        self.lbl_palabras=Label( self.ventana_principal, text="Ingrese las palabras: ", font=("Helvetica", 12),relief=RAISED)
        self.lbl_palabras.config( width=17)
        self.palabra1 = Entry(self.ventana_principal)
        self.palabra1.config(width=17)
        self.palabra2=Entry(self.ventana_principal)
        self.palabra2.config(width=17)
        self.lbl_relaciones=Label( self.ventana_principal, text="Relaciones: ", font=("Helvetica", 12),relief=RAISED)
        self.lbl_relaciones.config( width=17)
        self.lbl_hermanas=Label( self.ventana_principal, text="Hermanas: ", font=("Helvetica", 12),relief=RAISED)
        self.lbl_hermanas.config( width=15)
        self.lbl_hija=Label( self.ventana_principal, text="Hija: ", font=("Helvetica", 12),relief=RAISED)
        self.lbl_hija.config( width=15)
        self.lbl_tia=Label( self.ventana_principal, text="Tía: ", font=("Helvetica", 12),relief=RAISED)
        self.lbl_tia.config( width=15)       
        self.lbl_primas=Label( self.ventana_principal, text="Primas: ", font=("Helvetica", 12),relief=RAISED)
        self.lbl_primas.config( width=15)
        self.lbl_grado=Label( self.ventana_principal, text="Grado: ", font=("Helvetica", 12),relief=RAISED)
        self.lbl_grado.config( width=15)
        self.lbl_res_hermanas=Label( self.ventana_principal,bg="white")
        self.lbl_res_hermanas.config( width=5)
        self.lbl_res_hija=Label( self.ventana_principal,bg="white")
        self.lbl_res_hija.config( width=5)
        self.lbl_res_tia=Label( self.ventana_principal,bg="white")
        self.lbl_res_tia.config( width=5)
        self.lbl_res_primas=Label( self.ventana_principal,bg="white")
        self.lbl_res_primas.config( width=5)
        self.lbl_res_grado=Label( self.ventana_principal,bg="white")
        self.lbl_res_grado.config( width=5)
    def v_principal(self):        
        self.lbl_bienvenido.pack()
        self.cmbox_opcion.place(y=200,x=300)        
        self.btn_opcion.place(y=240,x=305)        
    def opciones(self):
        if (self.cmbox_opcion_value.get()=="Dos palabras"):
            self.dos_palabras_interfaz()
        elif (self.cmbox_opcion_value.get()=="Palabra-Idioma"):
            self.palabra_idioma_interfaz()
        else:
            self.idioma_interfaz()
    def dos_palabras_interfaz(self):
        self.desaparecer_elementos()
        self.lbl_bienvenido["text"]="Dos palabras"
        self.lbl_palabras.place(x=100,y=100)
        self.palabra1.place(x=280,y=100)
        self.palabra2.place(x=450,y=100)
        self.lbl_relaciones.place(x=100,y=150)
        self.lbl_hermanas.place(x=280,y=150)
        self.lbl_hija.place(x=280,y=200)
        self.lbl_tia.place(x=280,y=250)
        self.lbl_primas.place(x=280,y=300)
        self.lbl_grado.place(x=280,y=350)
        self.lbl_res_hermanas.place(x=450,y=150)
        self.lbl_res_hija.place(x=450,y=200)
        self.lbl_res_tia.place(x=450,y=250)
        self.lbl_res_primas.place(x=450,y=300)
        self.lbl_res_grado.place(x=450,y=350)
    def palabra_Idioma_interfaz(self):
        self.desaparecer_elementos()
        self.lbl_bienvenido["text"]="Palabra-Idioma"
    def idioma_interfaz(self):
        self.desaparecer_elementos()
        self.lbl_bienvenido["text"]="Idiomas"
    def desaparecer_elementos(self):
        self.lbl_hermanas.place(x=280,y=2000)
        self.lbl_hija.place(x=280,y=2500)
        self.lbl_tia.place(x=280,y=3000)
        self.lbl_primas.place(x=280,y=3500)
        self.lbl_grado.place(x=500,y=3500)
        self.lbl_relaciones.place(x=1000,y=200)
        self.palabra1.place(x=1300,y=100)
        self.palabra2.place(x=1500,y=100)
        self.lbl_palabras.place(x=1000,y=1000)
        self.cmbox_opcion.place(x=3000,y=3000)
        self.btn_opcion.place(x=3000,y=3000)

def main():
    mi_app = aplicacion()
    return(0)

if __name__ == '__main__':
    main()
