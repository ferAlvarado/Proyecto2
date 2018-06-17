from tkinter import *
from tkinter import ttk
from tkinter import Image
from main3 import *




def v_principal():
    desaparecer_elementos()
    lbl_bienvenido.pack()
    cmbox_opcion.place(x=200,y=100)        
    btn_opcion.place(x=550,y=245)
    btn_opcion.config( width=30)
    lbl_opcion.place(x=20,y=100)
    lbl_relacion.place(x=20,y=150)
    chbox_etymological_origin_of.place(x=200,y=150)
    chbox_has_derived_form .place(x=200,y=180)
    chbox_is_derived_from.place(x=200,y=210)
    chbox_etymology.place(x=200,y=240)
    chbox_etymologically_related.place(x=200,y=270)
    chbox_derived.place(x=200,y=300)
    chbox_etymologically.place(x=200,y=330)
def opciones():
    opcion=[]
    if (var.get()):
        opcion += ["etymological_origin_of"]
    if (var1.get()):
        opcion += ["has_derived_form"]
    if (var2.get()):
        opcion += ["is_derived_from"]
    if (var3.get()):
        opcion += ["etymology"]
    if (var4.get()):
        opcion += ["etymologically_related"]
    if (var5.get()):
        opcion += ["derived"]
    if (var6.get()):
        opcion += ["etymologically"]
##        if (self.var7.get()):
##            opcion += ["variant:orthography"]
    x = leer("j.tsv")
    print(opcion)
    cargarPadres(opcion, x)
    #print(palabra_comun("Papa de Freyser","idioma_y",Y).data)
    #print(palabra_comun("Papa de Freyser","idioma_y",Y).data)
    
  
    if (cmbox_opcion_value.get()=="Dos palabras"):
        
        dos_palabras_interfaz()
    elif (cmbox_opcion_value.get()=="Palabra-Idioma"):
        cargar_Idiomas1(opcion, x,1)
        cargar_Idiomas1(opcion, x,2)
        palabra_Idioma_interfaz()
    else:
        cargar_Idiomas1(opcion, x,1)
        cargar_Idiomas1(opcion, x,2)
        idioma_interfaz()
def dos_palabras_interfaz():
    desaparecer_elementos()
    lbl_bienvenido["text"]="Dos palabras"
    lbl_palabras.place(x=200,y=100)
    lbl_palabras["text"]="Ingrese las palabras: "
    lbl_palabras.config( width=17)
    palabra1.place(x=370,y=100)
    palabra2.place(x=520,y=100)
    lbl_relaciones.place(x=100,y=150)
    lbl_hermanas.place(x=450,y=200)
    lbl_hija.place(x=450,y=250)
    lbl_tia.place(x=450,y=300)
    lbl_primas.place(x=450,y=350)
    lbl_grado.place(x=450,y=400)
    lbl_res_hermanas.place(x=620,y=200)
    lbl_res_hija.place(x=620,y=250)
    lbl_res_tia.place(x=620,y=300)
    lbl_res_primas.place(x=620,y=350)
    lbl_res_grado.place(x=620,y=400)
    lbl_pal2_her.place(x=280,y=200)
    lbl_pal2_hija.place(x=280,y=250)
    lbl_pal2_tia.place(x=280,y=300)
    lbl_pal2_primas.place(x=280,y=350)
    lbl_pal1_her.place(x=100,y=200)
    lbl_pal1_hija.place(x=100,y=250)
    lbl_pal1_tia.place(x=100,y=300)
    lbl_pal1_primas.place(x=100,y=350)
    btn_rel_her.place(x=700,y=195)
    btn_rel_hija.place(x=700,y=245)
    btn_rel_tia.place(x=700,y=295)
    btn_rel_prima.place(x=700,y=345)
    btn_rel_prima_grado.place(x=100,y=395)
def palabra_Idioma_interfaz():
    desaparecer_elementos()
    lbl_bienvenido["text"]="Palabra-Idioma"
    lbl_palabras.place(x=280,y=70)
    lbl_palabras["text"]="Ingrese palabra, idioma y elija una opción: "
    lbl_palabras.config(width=35)
    palabra1.place(x=200,y=100)
    palabra2.place(x=380,y=100)
    cmbox_idioma_pal.place(x=560,y=100)
    btn_idioma_pal.place(x=260,y=150)
    btn_idioma_pal.config( width=40)
def idioma_interfaz():
    desaparecer_elementos()
    lbl_bienvenido["text"]="Idiomas"
    lbl_palabras.place(x=280,y=70)
    lbl_palabras["text"]="Ingrese idiomas y elija una opción: "
    lbl_palabras.config(width=35)
    palabra1.place(x=200,y=100)
    palabra2.place(x=380,y=100)
    cmbox_idioma.place(x=560,y=100)
    btn_idioma.place(x=260,y=150)
    btn_idioma.config( width=40)
def desaparecer_elementos():
    chbox_etymological_origin_of.place(x=200,y=1500)
    chbox_has_derived_form .place(x=200,y=1800)
    chbox_is_derived_from.place(x=200,y=2100)
    chbox_etymology.place(x=200,y=2400)
    chbox_etymologically_related.place(x=200,y=2700)
    chbox_derived.place(x=200,y=3000)
    chbox_etymologically.place(x=200,y=3300)
    lbl_relacion.place(x=20,y=1500)
    lbl_opcion.place(x=5000,y=5000)
    chbox_etymological_origin_of.place(x=1000,y=1000)
    cmbox_idioma_pal.place(x=560,y=1000)
    btn_idioma_pal.place(x=260,y=1500)
    btn_idioma_pal.config( width=4000)
    listbox_palabras.place(x=275,y=2000)
    cmbox_idioma_pal.place(x=560,y=1000)
    btn_idioma_pal.place(x=260,y=1500)
    btn_idioma_pal.config( width=4000)
    lbl_res_hermanas.place(x=620,y=2000)
    lbl_res_hija.place(x=620,y=2500)
    lbl_res_tia.place(x=620,y=3000)
    lbl_res_primas.place(x=620,y=3500)
    lbl_res_grado.place(x=620,y=4000)
    btn_rel_her.place(x=700,y=1950)
    btn_rel_hija.place(x=700,y=2450)
    btn_rel_tia.place(x=700,y=2950)
    btn_rel_prima.place(x=700,y=3450)
    btn_rel_prima_grado.place(x=100,y=3950)
    lbl_pal2_her.place(x=280,y=2000)
    lbl_pal2_hija.place(x=280,y=2500)
    lbl_pal2_tia.place(x=280,y=3000)
    lbl_pal2_primas.place(x=280,y=3500)
    lbl_pal1_her.place(x=100,y=2000)
    lbl_pal1_hija.place(x=100,y=2500)
    lbl_pal1_tia.place(x=100,y=3000)
    lbl_pal1_primas.place(x=100,y=3500)
    lbl_hermanas.place(x=280,y=2000)
    lbl_hija.place(x=280,y=2500)
    lbl_tia.place(x=280,y=3000)
    lbl_primas.place(x=280,y=3500)
    lbl_grado.place(x=500,y=3500)
    lbl_relaciones.place(x=1000,y=200)
    palabra1.place(x=1300,y=100)
    palabra2.place(x=1500,y=100)
    lbl_palabras.place(x=1000,y=1000)
    cmbox_opcion.place(x=3000,y=3000)
    btn_opcion.place(x=3000,y=3000)
def func_relacion_hermana():
    p1=palabra1.get()
    p2=palabra2.get()
    palabra1.delete(0, END)
    palabra2.delete(0, END)
    lbl_res_hermanas["text"]=conocer_resultados(p1,p2,1) #En esta se pone el resultado de la búsqueda V/F
    
    ventana_detalles([conocer_resultados(p1,p2,1),"& padre(Y,P)  & (X!=Y)","hermano(X,Y) <= padre(X,P)","Consulta:","Padres Cargados..."])
def func_relacion_hija():
    # izquierda padre, derecha hijo
    p1=palabra1.get()
    p2=palabra2.get()
    palabra1.delete(0, END)
    palabra2.delete(0, END)
    lbl_res_hija["text"]=conocer_resultados(p1,p2,3) #En esta se pone el resultado de la búsqueda V/F
    ventana_detalles([conocer_resultados(p1,p2,3),"hijo(X,Y) <= padre(X,Y)","Consulta:","Padres Cargados..."])
def func_relacion_tia():
    p1=palabra1.get()#sobrino
    p2=palabra2.get()#tio
    palabra1.delete(0, END)
    palabra2.delete(0, END)
    lbl_res_tia["text"]=conocer_resultados(p1,p2,4) #En esta se pone el resultado de la búsqueda V/F
    ventana_detalles([conocer_resultados(p1,p2,4),"primo(X,Y) <= padre(X,A) & tio(Y,A)","Consulta:","Padres Cargados..."])
def func_relacion_prima():
    p1 = palabra1.get()#
    p2 = palabra2.get()#
    palabra1.delete(0, END)
    palabra2.delete(0, END)
    lbl_res_primas["text"]=conocer_resultados(p1,p2,2)#En esta se pone el resultado de la búsqueda V/F
    ventana_detalles([conocer_resultados(p1,p2,2),"tio(X,Y) <= padre(X,P) & hermano(Y,P)","Consulta:","Padres Cargados..."])
def func_relacion_prima_grado():
    lbl_pal1_primas["text"]=palabra1.get()
    lbl_pal2_primas["text"]=palabra2.get()
    palabra1.delete(0, END)
    palabra2.delete(0, END)
    lbl_res_primas["text"]=" " #En esta se pone el resultado de la búsqueda V/F
    lbl_res_grado["text"]=" " #Si el resultado de prima es falso, se mantieneen blanco, sino pone grado
    ventana_detalles()
    
def func_palabra_idioma():
    lbl_res_relacionado.place(x=350,y=2500)
    listbox_palabras.place(x=275,y=2000)
    listbox_palabras.delete(0, END)
    
    if (cmbox_idioma_pal.get()=="Relacionadas"):
        palabra=palabra1.get()
        idioma=palabra2.get()
        lbl_res_relacionado.place(x=400,y=250)
        lbl_res_relacionado.config(font=("Helvetica", 30))
        lbl_res_relacionado["text"]=conocer_resultados(palabra,idioma,6)#Resultado SI/NO
        ventana_detalles([conocer_resultados(palabra,idioma,6),"palabra_idioma(X,Y) <= ancestro(X,P) & idioma(P,Y)","palabra_idioma(X,Y) <= descendiente(X,P) & idioma(P,Y)","palabra_idioma(X,Y) <= idioma(X,Y)","Consulta:","Idiomas Cargados","Padres Cargados.."])

    elif (cmbox_idioma_pal.get()=="Conjunto de palabras"):
        print("aqui")
        palabra=palabra1.get()
        idioma=palabra2.get()
        idiomas = conocer_resultados(palabra,idioma,5)
        listbox_palabras.insert(0, idiomas)
        listbox_palabras.place(x=275,y=200)
        ventana_detalles([conocer_resultados(palabra,idioma,5),"palabra_comun(X,Y,A) <= idioma(A,Y) & padre(A,X)","Consulta:","Idiomas Cargados","Padres Cargados.."])
        
    else: 
        palabra=palabra1.get()
        idioma=palabra2.get()
        idiomas = conocer_resultados(palabra,idioma,7)
        palabra2.delete(0, END)
        listbox_palabras.insert(0, idiomas)
        listbox_palabras.place(x=275,y=200)
        ventana_detalles([conocer_resultados(palabra,idioma,7),"palabra_idioma(X,Y) <= ancestro(X,P) & idioma(P,Y)","palabra_idioma(X,Y) <= descendiente(X,P) & idioma(P,Y)","palabra_idioma(X,Y) <= idioma(X,Y)","Consulta:","Idiomas Cargados","Padres Cargados.."])

        
def func_idiomas():
    lbl_res_cantPal.place(x=350,y=2500)
    listbox_palabras.place(x=275,y=2000)
    listbox_palabras.delete(0, END)

    if (cmbox_idioma.get()=="Contar palabras en común"):
        print("aqui")
        idioma1=palabra1.get()
        idioma2=palabra2.get()
        idiomas = conocer_resultados(idioma1,idioma2,8)
        lbl_res_cantPal.place(x=400,y=250)
        lbl_res_cantPal.config(font=("Helvetica", 30))
        lbl_res_cantPal["text"]=idiomas #Cantidad
        ventana_detalles([conocer_resultados(idioma1,idioma2,8),"(contar_palabras[X,Y] == len_(P)) <= listar_palabras_comunes(X,Y,P)","contar_palabras_comunes(X,Y) <= idioma(P,X) & idioma(P,Y)","Consulta:","Idiomas Cargados","Padres Cargados.."])
    elif (cmbox_idioma_pal.get()=="Listar palabras comunes"):
        idioma1=palabra1.get()
        idioma2=palabra2.get()
        idiomas = conocer_resultados(idioma1,idioma2,9)
        listbox_palabras.insert(0, idiomas)
        listbox_palabras.place(x=275,y=200)
        ventana_detalles([conocer_resultados(idioma1,idioma2,9),"(contar_palabras[X,Y] == len_(P)) <= listar_palabras_comunes(X,Y,P)","contar_palabras_comunes(X,Y) <= idioma(P,X) & idioma(P,Y)","Consulta:","Idiomas Cargados","Padres Cargados.."])
        
    elif (cmbox_idioma.get()=="Idioma que más aportó"):
        pala1=palabra1.get()
        pala2=palabra1.get()
        palabra1.delete(0, END)
        palabra2.delete(0, END)
        idiomas = conocer_resultados(pala1,pala2,10)
        lbl_res_cantPal.place(x=400,y=250)
        lbl_res_cantPal.config(font=("Helvetica", 30))
        lbl_res_cantPal["text"]=idiomas#Idioma y porcentaje
        ventana_detalles(["& padre(P,Y) & idioma(Y,X)","idioma_aportando(A,X,P)<= idioma(P,A) ","Consulta:","Idiomas Cargados","Padres Cargados.."])
    else:
        palabra=palabra1.get()
        acum = obtener_Lista_Porcentajes(palabra,lenguajes)
        print(acum)
        for k in acum[:-1]:
            agregar = str(k[0])+" "+str(((k[1]/acum[-1])*100))
            listbox_palabras.insert(0, agregar)
        palabra1.delete(0, END)
        palabra2.delete(0, END)
        listbox_palabras.place(x=275,y=200)
        ventana_detalles(["& padre(P,Y) & idioma(Y,X)","idioma_aportando(A,X,P)<= idioma(P,A) ","Consulta:","Idiomas Cargados","Padres Cargados.."])
        


def ventana_detalles(lista):
    detalles = Toplevel()
    detalles.geometry("400x300")
    detalles.resizable(width=False, height=False)
    detalles.title("Detalles")
    detalles["bg"]="black"
    listbox_detalles = Listbox(detalles,width=55, height=15)
    for i  in lista:
        listbox_detalles.insert(0, i)
    listbox_detalles.place(x=50,y=30)
    

ventana_principal=Tk()
ventana_principal.geometry('860x500')
ventana_principal["bg"]="black"
ventana_principal.resizable(0,0)
ventana_principal.title("Relaciones de Etimología")
    

"""Componentes principales"""
lbl_bienvenido = Label( ventana_principal, text="Bienvenido", font=("Bitstream Vera Serif", 30),fg="goldenrod",bg="black")
cmbox_opcion_value = StringVar()
cmbox_opcion = ttk.Combobox(ventana_principal, textvariable=cmbox_opcion_value, font=("Helvetica", 12))
cmbox_opcion['values'] =("Dos palabras","Palabra-Idioma","Idiomas")
cmbox_opcion.current(0)
btn_opcion=Button(ventana_principal,text="LISTO",fg="black",bg="goldenrod",font=("Bitstream Vera Serif", 10),highlightbackground ="goldenrod",highlightcolor ="goldenrod",command=opciones)
btn_opcion.config(width=17)
lbl_opcion=Label( ventana_principal, text="Elija operación: ", font=("Helvetica", 12),fg="goldenrod",bg="black")
lbl_opcion.config( width=15)
lbl_relacion=Label( ventana_principal, text="Elija relación: ", font=("Helvetica", 12),fg="goldenrod",bg="black")
lbl_relacion.config( width=15)
var = IntVar()
chbox_etymological_origin_of = Checkbutton(ventana_principal, text="etymological_origin_of", variable=var, font=("Helvetica", 12),fg="goldenrod",bg="black",anchor=SW)
chbox_etymological_origin_of.config( width=25)
var1 = IntVar()
chbox_has_derived_form = Checkbutton(ventana_principal, text="has_derived_form", variable=var1, font=("Helvetica", 12),fg="goldenrod",bg="black",anchor=SW)
chbox_has_derived_form.config( width=25)
var2 = IntVar()
chbox_is_derived_from = Checkbutton(ventana_principal, text=" is_derived_from", variable=var2, font=("Helvetica", 12),fg="goldenrod",bg="black",anchor=SW)
chbox_is_derived_from.config( width=25)
var3 = IntVar()
chbox_etymology = Checkbutton(ventana_principal, text=" etymology", variable=var3, font=("Helvetica", 12),fg="goldenrod",bg="black",anchor=SW)
chbox_etymology.config( width=25)
var4 = IntVar()
chbox_etymologically_related = Checkbutton(ventana_principal, text="etymologically_related", variable=var4, font=("Helvetica", 12),fg="goldenrod",bg="black",anchor=SW)
chbox_etymologically_related.config( width=25)
var5 = IntVar()
chbox_derived = Checkbutton(ventana_principal, text="derived", variable=var5, font=("Helvetica", 12),fg="goldenrod",bg="black",anchor=SW)
chbox_derived.config( width=25)
var6 = IntVar()
chbox_etymologically = Checkbutton(ventana_principal, text=" etymologically", variable=var6, font=("Helvetica", 12),fg="goldenrod",bg="black",anchor=SW)
chbox_etymologically.config( width=25)
barramenu = Menu(ventana_principal)
ventana_principal['menu'] = barramenu
menu1 = Menu(barramenu)
barramenu.add_cascade(menu=menu1, label='Inicio')
menu1.add_command(label='Página principal', 
                  command=v_principal, 
                  underline=0, accelerator="Ctrl+c",compound=LEFT)
palabra1 = Entry(ventana_principal)
palabra1.config(width=17)
palabra2=Entry(ventana_principal)
palabra2.config(width=17)
"""Componentes de dos palabras"""
lbl_relaciones=Label( ventana_principal, text="Palabras: ", font=("Helvetica", 12),fg="goldenrod",bg="black")
lbl_relaciones.config( width=37)
lbl_palabras=Label( ventana_principal, font=("Helvetica", 12),fg="goldenrod",bg="black")
lbl_hermanas=Label( ventana_principal, text="Hermanas: ", font=("Helvetica", 12),fg="goldenrod",bg="black")
lbl_hermanas.config( width=15)
lbl_hija=Label( ventana_principal, text="Hija: ", font=("Helvetica", 12),fg="goldenrod",bg="black")
lbl_hija.config( width=15)
lbl_tia=Label( ventana_principal, text="Tía: ", font=("Helvetica", 12),fg="goldenrod",bg="black")
lbl_tia.config( width=15)       
lbl_primas=Label( ventana_principal, text="Primas: ", font=("Helvetica", 12),fg="goldenrod",bg="black")
lbl_primas.config( width=15)
lbl_grado=Label( ventana_principal, text="Grado: ", font=("Helvetica", 12),fg="goldenrod",bg="black")
lbl_grado.config( width=15)
lbl_res_hermanas=Label( ventana_principal,fg="goldenrod",bg="black")
lbl_res_hermanas.config( width=5)
lbl_res_hija=Label( ventana_principal,fg="goldenrod",bg="black")
lbl_res_hija.config( width=5)
lbl_res_tia=Label( ventana_principal,fg="goldenrod",bg="black")
lbl_res_tia.config( width=5)
lbl_res_primas=Label( ventana_principal,fg="goldenrod",bg="black")
lbl_res_primas.config( width=5)
lbl_res_grado=Label( ventana_principal,fg="goldenrod",bg="black")
lbl_res_grado.config( width=5)
lbl_pal2_her=Label( ventana_principal,fg="goldenrod",bg="black")
lbl_pal2_her.config( width=17)
lbl_pal2_hija=Label( ventana_principal,fg="goldenrod",bg="black")
lbl_pal2_hija.config( width=17)
lbl_pal2_tia=Label( ventana_principal,fg="goldenrod",bg="black")
lbl_pal2_tia.config( width=17)
lbl_pal2_primas=Label( ventana_principal,fg="goldenrod",bg="black")
lbl_pal2_primas.config( width=17)
lbl_pal1_her=Label( ventana_principal,fg="goldenrod",bg="black")
lbl_pal1_her.config( width=17)
lbl_pal1_hija=Label( ventana_principal,fg="goldenrod",bg="black")
lbl_pal1_hija.config( width=17)
lbl_pal1_tia=Label( ventana_principal,fg="goldenrod",bg="black")
lbl_pal1_tia.config( width=17)
lbl_pal1_primas=Label( ventana_principal,fg="goldenrod",bg="black")
lbl_pal1_primas.config( width=17)
btn_rel_her=Button(ventana_principal,text="Relación",fg="black",bg="goldenrod",font=("Bitstream Vera Serif", 10),command=func_relacion_hermana)
btn_rel_hija=Button(ventana_principal,text="Relación",fg="black",bg="goldenrod",font=("Bitstream Vera Serif", 10),command=func_relacion_hija)
btn_rel_tia=Button(ventana_principal,text="Relación",fg="black",bg="goldenrod",font=("Bitstream Vera Serif", 10),command=func_relacion_tia)
btn_rel_prima=Button(ventana_principal,text="Relación",fg="black",bg="goldenrod",font=("Bitstream Vera Serif", 10),command=func_relacion_prima)
btn_rel_prima_grado=Button(ventana_principal,text="Relación prima y grado",fg="black",bg="goldenrod",font=("Bitstream Vera Serif", 10),command=func_relacion_prima_grado)
btn_rel_prima_grado.config( width=37)
"""componentes idioma palabra"""
cmbox_idioma_pal_value = StringVar()
cmbox_idioma_pal= ttk.Combobox(ventana_principal, textvariable=cmbox_idioma_pal_value)
cmbox_idioma_pal['values'] =("Relacionadas","Conjunto de palabras","Idiomas relacionados")
cmbox_idioma_pal.current(0)
btn_idioma_pal=Button(ventana_principal,text="Procesar",fg="black",bg="goldenrod",font=("Bitstream Vera Serif", 10),command=func_palabra_idioma)
lbl_res_relacionado=Label( ventana_principal, font=("Helvetica", 12),fg="goldenrod",bg="black")
listbox_palabras = Listbox(ventana_principal,width=40, height=15)
"""componentes Idiomas"""
cmbox_idioma_value = StringVar()
cmbox_idioma= ttk.Combobox(ventana_principal, textvariable=cmbox_idioma_value)
cmbox_idioma['values'] =("Contar palabras en común","Listar palabras comunes","Idioma que más aportó","Listar idiomas")
cmbox_idioma.current(0)
btn_idioma=Button(ventana_principal,text="Procesar",fg="black",bg="goldenrod",font=("Bitstream Vera Serif", 10),command=func_palabra_idioma)
lbl_res_cantPal=Label( ventana_principal, font=("Helvetica", 12),fg="goldenrod",bg="black")
btn_idioma=Button(ventana_principal,text="Procesar",fg="black",bg="goldenrod",font=("Bitstream Vera Serif", 10),command=func_idiomas)


#componentes_interfaz()
v_principal()
ventana_principal.mainloop()
