from tkinter import *
from tkinter import ttk
from tkinter import Image
import os

class aplicacion(): 
    def __init__(self):
        self.ventana_principal=Tk()
        self.ventana_principal.geometry('860x500')
        self.ventana_principal["bg"]="black"
        self.componentes_interfaz()
        self.v_principal()
        self.ventana_principal.resizable(0,0)
        self.ventana_principal.title("Relaciones de Etimología")
        self.ventana_principal.mainloop()
    def componentes_interfaz(self):
        """Componentes principales"""
        self.lbl_bienvenido = Label( self.ventana_principal, text="Bienvenido", font=("Bitstream Vera Serif", 30),fg="goldenrod",bg="black")
        self.cmbox_opcion_value = StringVar()
        self.cmbox_opcion = ttk.Combobox(self.ventana_principal, textvariable=self.cmbox_opcion_value)
        self.cmbox_opcion['values'] =("Dos palabras","Palabra-Idioma","Idiomas")
        self.cmbox_opcion.current(0)
        self.btn_opcion=Button(self.ventana_principal,text="LISTO",fg="black",bg="goldenrod",font=("Bitstream Vera Serif", 10),highlightbackground ="goldenrod",highlightcolor ="goldenrod",command=self.opciones)
        self.btn_opcion.config(width=17)
        """Componentes de dos palabras"""
        self.lbl_relaciones=Label( self.ventana_principal, text="Palabras: ", font=("Helvetica", 12),fg="goldenrod",bg="black")
        self.lbl_relaciones.config( width=37)
        self.lbl_hermanas=Label( self.ventana_principal, text="Hermanas: ", font=("Helvetica", 12),fg="goldenrod",bg="black")
        self.lbl_hermanas.config( width=15)
        self.lbl_hija=Label( self.ventana_principal, text="Hija: ", font=("Helvetica", 12),fg="goldenrod",bg="black")
        self.lbl_hija.config( width=15)
        self.lbl_tia=Label( self.ventana_principal, text="Tía: ", font=("Helvetica", 12),fg="goldenrod",bg="black")
        self.lbl_tia.config( width=15)       
        self.lbl_primas=Label( self.ventana_principal, text="Primas: ", font=("Helvetica", 12),fg="goldenrod",bg="black")
        self.lbl_primas.config( width=15)
        self.lbl_grado=Label( self.ventana_principal, text="Grado: ", font=("Helvetica", 12),fg="goldenrod",bg="black")
        self.lbl_grado.config( width=15)
        self.lbl_res_hermanas=Label( self.ventana_principal,fg="goldenrod",bg="black")
        self.lbl_res_hermanas.config( width=5)
        self.lbl_res_hija=Label( self.ventana_principal,fg="goldenrod",bg="black")
        self.lbl_res_hija.config( width=5)
        self.lbl_res_tia=Label( self.ventana_principal,fg="goldenrod",bg="black")
        self.lbl_res_tia.config( width=5)
        self.lbl_res_primas=Label( self.ventana_principal,fg="goldenrod",bg="black")
        self.lbl_res_primas.config( width=5)
        self.lbl_res_grado=Label( self.ventana_principal,fg="goldenrod",bg="black")
        self.lbl_res_grado.config( width=5)
        self.lbl_pal2_her=Label( self.ventana_principal,fg="goldenrod",bg="black")
        self.lbl_pal2_her.config( width=17)
        self.lbl_pal2_hija=Label( self.ventana_principal,fg="goldenrod",bg="black")
        self.lbl_pal2_hija.config( width=17)
        self.lbl_pal2_tia=Label( self.ventana_principal,fg="goldenrod",bg="black")
        self.lbl_pal2_tia.config( width=17)
        self.lbl_pal2_primas=Label( self.ventana_principal,fg="goldenrod",bg="black")
        self.lbl_pal2_primas.config( width=17)
        self.lbl_pal1_her=Label( self.ventana_principal,fg="goldenrod",bg="black")
        self.lbl_pal1_her.config( width=17)
        self.lbl_pal1_hija=Label( self.ventana_principal,fg="goldenrod",bg="black")
        self.lbl_pal1_hija.config( width=17)
        self.lbl_pal1_tia=Label( self.ventana_principal,fg="goldenrod",bg="black")
        self.lbl_pal1_tia.config( width=17)
        self.lbl_pal1_primas=Label( self.ventana_principal,fg="goldenrod",bg="black")
        self.lbl_pal1_primas.config( width=17)
        self.btn_rel_her=Button(self.ventana_principal,text="Relación",command=self.func_relacion_hermana)
        self.btn_rel_hija=Button(self.ventana_principal,text="Relación",command=self.func_relacion_hija)
        self.btn_rel_tia=Button(self.ventana_principal,text="Relación",command=self.func_relacion_tia)
        self.btn_rel_prima=Button(self.ventana_principal,text="Relación",command=self.func_relacion_prima)
        self.btn_rel_prima_grado=Button(self.ventana_principal,text="Relación prima y grado",command=self.func_relacion_prima_grado)
        self.btn_rel_prima_grado.config( width=37)
        """componentes idioma palabra"""
        self.cmbox_idioma_pal_value = StringVar()
        self.cmbox_idioma_pal= ttk.Combobox(self.ventana_principal, textvariable=self.cmbox_idioma_pal_value)
        self.cmbox_idioma_pal['values'] =("Relacionadas","Conjunto de palabras","Idiomas relacionados")
        self.cmbox_idioma_pal.current(0)
        self.btn_idioma_pal=Button(self.ventana_principal,text="Procesar",fg="black",bg="goldenrod",font=("Bitstream Vera Serif", 10),command=self.func_palabra_idioma)
        self.lbl_res_relacionado=Label( self.ventana_principal, font=("Helvetica", 12),fg="goldenrod",bg="black")
        self.listbox_palabras = Listbox(self.ventana_principal,width=40, height=15)
        """componentes Idiomas"""
        self.cmbox_idioma_value = StringVar()
        self.cmbox_idioma= ttk.Combobox(self.ventana_principal, textvariable=self.cmbox_idioma_value)
        self.cmbox_idioma['values'] =("Contar palabras en común","Listar palabras comunes","Idioma que más aportó","Listar idiomas")
        self.cmbox_idioma.current(0)
        self.btn_idioma=Button(self.ventana_principal,text="Procesar",fg="black",bg="goldenrod",font=("Bitstream Vera Serif", 10),command=self.func_palabra_idioma)
        self.lbl_res_cantPal=Label( self.ventana_principal, font=("Helvetica", 12),fg="goldenrod",bg="black")
        self.btn_idioma=Button(self.ventana_principal,text="Procesar",fg="black",bg="goldenrod",font=("Bitstream Vera Serif", 10),command=self.func_idiomas)
        
    def v_principal(self):        
        self.lbl_bienvenido.pack()
        self.cmbox_opcion.place(y=200,x=300)        
        self.btn_opcion.place(y=240,x=305)
        self.lbl_palabras=Label( self.ventana_principal, font=("Helvetica", 12),fg="goldenrod",bg="black")
        self.palabra1 = Entry(self.ventana_principal)
        self.palabra1.config(width=17)
        self.palabra2=Entry(self.ventana_principal)
        self.palabra2.config(width=17)
    def opciones(self):
        if (self.cmbox_opcion_value.get()=="Dos palabras"):
            self.dos_palabras_interfaz()
        elif (self.cmbox_opcion_value.get()=="Palabra-Idioma"):
            self.palabra_Idioma_interfaz()
        else:
            self.idioma_interfaz()
    def dos_palabras_interfaz(self):
        self.desaparecer_elementos()
        self.lbl_bienvenido["text"]="Dos palabras"
        self.lbl_palabras.place(x=200,y=100)
        self.lbl_palabras["text"]="Ingrese las palabras: "
        self.lbl_palabras.config( width=17)
        self.palabra1.place(x=370,y=100)
        self.palabra2.place(x=520,y=100)
        self.lbl_relaciones.place(x=100,y=150)
        self.lbl_hermanas.place(x=450,y=200)
        self.lbl_hija.place(x=450,y=250)
        self.lbl_tia.place(x=450,y=300)
        self.lbl_primas.place(x=450,y=350)
        self.lbl_grado.place(x=450,y=400)
        self.lbl_res_hermanas.place(x=620,y=200)
        self.lbl_res_hija.place(x=620,y=250)
        self.lbl_res_tia.place(x=620,y=300)
        self.lbl_res_primas.place(x=620,y=350)
        self.lbl_res_grado.place(x=620,y=400)
        self.lbl_pal2_her.place(x=280,y=200)
        self.lbl_pal2_hija.place(x=280,y=250)
        self.lbl_pal2_tia.place(x=280,y=300)
        self.lbl_pal2_primas.place(x=280,y=350)
        self.lbl_pal1_her.place(x=100,y=200)
        self.lbl_pal1_hija.place(x=100,y=250)
        self.lbl_pal1_tia.place(x=100,y=300)
        self.lbl_pal1_primas.place(x=100,y=350)
        self.btn_rel_her.place(x=700,y=195)
        self.btn_rel_hija.place(x=700,y=245)
        self.btn_rel_tia.place(x=700,y=295)
        self.btn_rel_prima.place(x=700,y=345)
        self.btn_rel_prima_grado.place(x=100,y=395)
    def palabra_Idioma_interfaz(self):
        self.desaparecer_elementos()
        self.lbl_bienvenido["text"]="Palabra-Idioma"
        self.lbl_palabras.place(x=280,y=70)
        self.lbl_palabras["text"]="Ingrese palabra, idioma y elija una opción: "
        self.lbl_palabras.config(width=35)
        self.palabra1.place(x=200,y=100)
        self.palabra2.place(x=380,y=100)
        self.cmbox_idioma_pal.place(x=560,y=100)
        self.btn_idioma_pal.place(x=260,y=150)
        self.btn_idioma_pal.config( width=40)
    def idioma_interfaz(self):
        self.desaparecer_elementos()
        self.lbl_bienvenido["text"]="Idiomas"
        self.lbl_palabras.place(x=280,y=70)
        self.lbl_palabras["text"]="Ingrese idiomas y elija una opción: "
        self.lbl_palabras.config(width=35)
        self.palabra1.place(x=200,y=100)
        self.palabra2.place(x=380,y=100)
        self.cmbox_idioma.place(x=560,y=100)
        self.btn_idioma.place(x=260,y=150)
        self.btn_idioma.config( width=40)
    def desaparecer_elementos(self):
        
        self.listbox_palabras.place(x=275,y=2000)
        self.cmbox_idioma_pal.place(x=560,y=1000)
        self.btn_idioma_pal.place(x=260,y=1500)
        self.btn_idioma_pal.config( width=4000)
        self.lbl_res_hermanas.place(x=620,y=2000)
        self.lbl_res_hija.place(x=620,y=2500)
        self.lbl_res_tia.place(x=620,y=3000)
        self.lbl_res_primas.place(x=620,y=3500)
        self.lbl_res_grado.place(x=620,y=4000)
        self.btn_rel_her.place(x=700,y=1950)
        self.btn_rel_hija.place(x=700,y=2450)
        self.btn_rel_tia.place(x=700,y=2950)
        self.btn_rel_prima.place(x=700,y=3450)
        self.btn_rel_prima_grado.place(x=100,y=3950)
        self.lbl_pal2_her.place(x=280,y=2000)
        self.lbl_pal2_hija.place(x=280,y=2500)
        self.lbl_pal2_tia.place(x=280,y=3000)
        self.lbl_pal2_primas.place(x=280,y=3500)
        self.lbl_pal1_her.place(x=100,y=2000)
        self.lbl_pal1_hija.place(x=100,y=2500)
        self.lbl_pal1_tia.place(x=100,y=3000)
        self.lbl_pal1_primas.place(x=100,y=3500)
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
    def func_relacion_hermana(self):
        self.lbl_pal1_her["text"]=self.palabra1.get()
        self.lbl_pal2_her["text"]=self.palabra2.get()
        self.palabra1.delete(0, END)
        self.palabra2.delete(0, END)
        self.lbl_res_hermanas["text"]=" " #En esta se pone el resultado de la búsqueda V/F
    def func_relacion_hija(self):
        self.lbl_pal1_hija["text"]=self.palabra1.get()
        self.lbl_pal2_hija["text"]=self.palabra2.get()
        self.palabra1.delete(0, END)
        self.palabra2.delete(0, END)
        self.lbl_res_hija["text"]=" " #En esta se pone el resultado de la búsqueda V/F
    def func_relacion_tia(self):
        self.lbl_pal1_tia["text"]=self.palabra1.get()
        self.lbl_pal2_tia["text"]=self.palabra2.get()
        self.palabra1.delete(0, END)
        self.palabra2.delete(0, END)
        self.lbl_res_tia["text"]=" " #En esta se pone el resultado de la búsqueda V/F
    def func_relacion_prima(self):
        self.lbl_pal1_primas["text"]=self.palabra1.get()
        self.lbl_pal2_primas["text"]=self.palabra2.get()
        self.palabra1.delete(0, END)
        self.palabra2.delete(0, END)
        self.lbl_res_primas["text"]=" " #En esta se pone el resultado de la búsqueda V/F
    def func_relacion_prima_grado(self):
        self.lbl_pal1_primas["text"]=self.palabra1.get()
        self.lbl_pal2_primas["text"]=self.palabra2.get()
        self.palabra1.delete(0, END)
        self.palabra2.delete(0, END)
        self.lbl_res_primas["text"]=" " #En esta se pone el resultado de la búsqueda V/F
        self.lbl_res_grado["text"]=" " #Si el resultado de prima es falso, se mantieneen blanco, sino pone grado
    def func_palabra_idioma(self):
        self.lbl_res_relacionado.place(x=350,y=2500)
        self.listbox_palabras.place(x=275,y=2000)
        self.listbox_palabras.delete(0, END)
        if (self.cmbox_idioma_pal.get()=="Relacionadas"):
            self.palabra=self.palabra1.get()
            self.idioma=self.palabra2.get()
            self.lbl_res_relacionado.place(x=400,y=250)
            self.lbl_res_relacionado.config(font=("Helvetica", 30))
            self.lbl_res_relacionado["text"]=" " #Resultado SI/NO
        elif (self.cmbox_idioma_pal.get()=="Conjunto de palabras"):
            self.palabra=self.palabra1.get()
            self.idioma=self.palabra2.get()
            self.listbox_palabras.place(x=275,y=200)
        else:
            self.palabra2.delete(0, END)
            self.palabra=self.palabra1.get()
            self.listbox_palabras.place(x=275,y=200)
    def func_idiomas(self):
        self.lbl_res_cantPal.place(x=350,y=2500)
        self.listbox_palabras.place(x=275,y=2000)
        self.listbox_palabras.delete(0, END)
        if (self.cmbox_idioma.get()=="Contar palabras en común"):
            self.idioma1=self.palabra1.get()
            self.idioma2=self.palabra2.get()
            self.lbl_res_cantPal.place(x=400,y=250)
            self.lbl_res_cantPal.config(font=("Helvetica", 30))
            self.lbl_res_cantPal["text"]=" " #Cantidad
        elif (self.cmbox_idioma_pal.get()=="Listar palabras comunes"):
            self.idioma1=self.palabra1.get()
            self.idioma2=self.palabra2.get()
            self.listbox_palabras.place(x=275,y=200)
        elif (self.cmbox_idioma.get()=="Idioma que más aportó"):
            self.palabra1.delete(0, END)
            self.palabra2.delete(0, END)
            self.lbl_res_cantPal.place(x=400,y=250)
            self.lbl_res_cantPal.config(font=("Helvetica", 30))
            self.lbl_res_cantPal["text"]=" " #Idioma y porcentaje
        else:
            self.palabra1.delete(0, END)
            self.palabra2.delete(0, END)
            self.palabra=self.palabra1.get()
            self.listbox_palabras.place(x=275,y=200)
            
            

def main():
    mi_app = aplicacion()
    return(0)

if __name__ == '__main__':
    main()
