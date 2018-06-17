"""
==========================================================================

Proyecto #2 ­ Etimology relations

==========================================================================
:Institucion: Instituto Tecnologico de Costa Rica
:Curso: Inteligencia Artificial
:Grupo: 2
:Semestre: I Semestre 2018
:Autores: Fernanda Alvarado Vargas,fernadaalvarado95@gmail.com /
          Minor Sancho Valverde,tivin.minor10@gmail.com /
          Freyser Jimenez Mena, fjimenez577@gmail.com /
:Fecha: 23/05/2018
"""
# -----------------------------------------------------------------------
from pyDatalog import pyDatalog
import csv
from time import time

pyDatalog.create_atoms('idioma_aportando,contar_palabras,padre,hermano,tio,primo,hijo,palabra_idioma,idioma_palabra,contar_palabras_comunes,listar_palabras_comunes,ancestro,descendiente,idioma,palabra_comun,P,X,Y,A,B')
#tiempo_inicial = time()
# -----------------------------------------------------------------------

################################### 1 ##################################
"""
Funcion que nos permite obtener los datos de cada linea del archivo.
"""
# -----------------------------------------------------------------------
def buscar_dos_puntos_mayor_rendimiento(lista):
    acum =[]
    for i in lista:
        pos=i.find(':')
        acum +=[i[0:pos]]
        palabra=i[pos+1:len(i)]
        if palabra[0]==' ':
            acum +=[palabra[1:]]
        else:
            acum +=[palabra]
    return acum
# -----------------------------------------------------------------------

################################### 2 ##################################
"""
Definicion de clausulas de logica.
"""
# -----------------------------------------------------------------------
#=================HERMANO=================
hermano(X,Y) <= padre(X,P) & padre(Y,P)  & (X!=Y)

#=================HIJO=================
#hijo es X y padre es Y
hijo(X,Y) <= padre(X,Y)

#=================TIO=================
#primero X = sobrino y segundo Y = tio
tio(X,Y) <= padre(X,P) & hermano(Y,P)

#=================PRIMO=================
# X = primo 1 y Y = primo 2
primo(X,Y) <= padre(X,A) & tio(Y,A)

#=================Descendiente=================
#A MAYOR Y B MENOR
descendiente(B,A) <= padre(B,A)
descendiente(B,A) <= padre(B,P) & descendiente(P,A)

#=================Ancestro=================
#A MAYOR Y Y MENOR
ancestro(A,Y) <= descendiente(Y,A)

#=================PalabraIdioma=================
#X igual palabra y Y igual idioma
##+ padre("Minor","freyser")
##+ padre("freyser567","freyser")
##+ idioma("Minor","x")
##+ idioma("freyser567","n")
##+ idioma("fr","S")
palabra_idioma(X,Y) <= idioma(X,Y)
palabra_idioma(X,Y) <= descendiente(X,P) & idioma(P,Y)
palabra_idioma(X,Y) <= ancestro(X,P) & idioma(P,Y)
##print(palabra_idioma("fr","n"))
##print(pyDatalog.ask('hermano("Minor","freyser567")'))

#=================PalabraComun=================
#X palabra y Y idioma
+ padre("freyser","Papi")
+ padre("Jupa","Minor")
+ padre("Minor","freyser")
+ padre("freyser567","freyser")
+ idioma("Minor","x")
+ idioma("Minor","y")
+ idioma("PINGA","x")
+ idioma("PINGA","y")
+ idioma("Min","x")
+ idioma("Min","y")
+ idioma("freyser567","y")
+ idioma("freyser","x")
+ idioma("fr","S")
+ idioma("Jupa","SoloJupa")
+ idioma("Papi","SoloPinGarcia")
+ idioma("freyser","y")
palabra_comun(X,Y,A) <= idioma(A,Y) & padre(A,X)
#print(palabra_comun(,"n",A))
#=================idiomaPalabra=================
#X palabra y Y resultado
idioma_palabra(X,Y) <= idioma(X,Y)
idioma_palabra(X,Y) <= descendiente(X,P) & idioma(P,Y)
idioma_palabra(X,Y) <= ancestro(X,P) & idioma(P,Y)
#print(idioma_palabra("freyser",A))
#=================contarPalabrasComunes=================
#X palabra y Y resultado
#listar
listar_palabras_comunes(X,Y,P) <= idioma(P,X) & idioma(P,Y)

#print(contar_palabras['x','y'] == P) # X is John
contar_palabras_comunes(X,Y) <= idioma(P,X) & idioma(P,Y)
(contar_palabras[X,Y] == len_(P)) <= listar_palabras_comunes(X,Y,P)        
#contar_palabras_comunes(X,Y,A,True) <= idioma(P,X) & idioma(P,Y)
#contar_palabras_comunes(X,Y,0,False) <= ~(idioma(P,X) & idioma(P,Y))
#contar_palabras_comunes(X,Y,B) <= idioma(P,X) & idioma(P,Y) & contar_palabras_comunes(X,Y,B+1)
#(contador[X]==sum_(Y, key=A)) <= contar_palabras_comunes(X,Y)
#print(contador[X]==Y)
#listar_palabras_comunes(X,Y,P)
#print(factorial["x","y",0]==N)
#print(listar_palabras_comunes(X,Y,P))
#=================idiomasAportandoaOtro=================
#X palabra y Y resultado
lenguajes= ['ara', 'ave', 'akk', 'aaq', 'abe', 'abs', 'adt', 'afr', 'aii', 'ain', 'akz', 'ale', 'alq', 'amh', 'amj', 'ang', 'apw', 'arg', 'arn', 'arq', 'arw', 'ary', 'arz', 'ase', 'ast', 'auc', 'ava', 'axm', 'ayl', 'aym', 'aze', 'bak', 'bar', 'bdy', 'bel', 'ben', 'bft', 'bis', 'bod', 'bre', 'bua', 'bul', 'byn', 'cat', 'ccc', 'ceb', 'ces', 'cha', 'chc', 'che', 'chn', 'cho', 'chr', 'chu', 'cic', 'cmn', 'cop', 'cor', 'cre', 'crh', 'csb', 'cym', 'dan', 'del', 'dep', 'deu','div','dsb','dtd','dum','efi','egy','ell','emn','eng','enm','enn','epo','ess','est','eus','evn','ewe','fao','fas','fij','fin','fon','fra', 'frc', 'frk', 'frm', 'fro', 'frp', 'fry', 'fur', 'gae', 'gez', 'gil', 'gla', 'gle', 'glg', 'glv', 'gmh', 'gml', 'gmy', 'goh', 'got', 'grc', 'grn', 'grv', 'gsw', 'gug', 'guj', 'gul', 'gwi', 'hak', 'hat', 'hau', 'haw', 'hbs', 'heb', 'hif', 'hil', 'hin', 'hit', 'hop', 'hsb', 'hun', 'hur', 'hye', 'idb', 'ido', 'ike', 'ikt', 'iku', 'ina', 'ind', 'inz', 'ipk', 'isl', 'ita','jam', 'jav', 'jbo', 'jpn', 'kal', 'kan', 'kat', 'kaw', 'kaz', 'kbd', 'khm', 'kin', 'kir', 'kjh', 'kju', 'kky', 'kld', 'kmb', 'kok', 'kon', 'kor', 'kri', 'krl', 'ksd', 'ksh', 'kum', 'kur', 'kzj', 'lad', 'lao', 'lat', 'lav', 'lij', 'lim', 'lin', 'lit', 'liv', 'lkt', 'lld', 'lmo', 'lng', 'lou', 'ltc', 'ltz', 'lua', 'lug', 'luo', 'lut', 'lzh', 'mah', 'mak', 'mal', 'mar', 'mas', 'mav', 'mbc', 'mfr', 'mga', 'mic', 'min', 'mkd', 'mlg', 'mlt', 'mnc', 'mnk', 'mod', 'moe', 'moh', 'mon', 'mri', 'msa', 'mwl', 'mxi', 'mya', 'myv', 'nah', 'nan', 'nap', 'naq', 'nav', 'nay', 'nci', 'ndo', 'nds', 'nep', 'nld','nno', 'nob', 'non', 'nor', 'nov', 'nys', 'obr', 'obt', 'oci', 'oco', 'odt', 'ofs', 'oge', 'oji', 'okm', 'ood', 'orc', 'ori', 'orv', 'osp', 'oss', 'osx', 'ota', 'otk', 'owl', 'p_gem', 'p_gmw', 'p_ine', 'p_sla', 'pal', 'pan', 'pap', 'pau', 'pcd', 'pdt', 'peo', 'phn', 'pim', 'pis', 'pjt', 'pli', 'pml', 'pol', 'por', 'pox', 'ppl', 'prg', 'pro', 'pus', 'quc', 'que', 'qwc', 'rap', 'rhg', 'rme', 'rmf', 'rmq', 'roh', 'rom', 'ron', 'rop', 'rue', 'ruo', 'rup', 'rus', 'ryu', 'san', 'sat', 'scn', 'sco', 'see', 'sei', 'sga', 'shh', 'sin', 'slk', 'slv', 'sme', 'smo', 'sms', 'sna', 'som', 'sot', 'spa', 'sqi', 'srd', 'srn', 'srs', 'stg', 'sth', 'stq', 'sun', 'sux', 'swa', 'swe', 'syc', 'szl', 'tah', 'tam', 'tat', 'tcs', 'tcy', 'tel', 'tet', 'tew', 'tgk', 'tgl', 'tha', 'tir', 'tiv', 'tnq', 'ton', 'tpi', 'tpw', 'tsn', 'tuk', 'tur', 'twf', 'twi', 'txb', 'tzm', 'uga', 'uig', 'ukr', 'ulk', 'umb', 'umu', 'urd', 'uzb', 'vai', 'vec', 'vep', 'vie', 'vls', 'vma', 'vol', 'wam', 'wit', 'wlm', 'wln', 'wol', 'wrh', 'wym', 'xaa', 'xbm', 'xce', 'xcl', 'xho', 'xmb', 'xng', 'xno', 'xnt', 'xon', 'xpr', 'xtg', 'xto', 'yid', 'yol', 'yor', 'yua', 'yue', 'yur', 'yxg', 'zai', 'zko', 'zku', 'zsm', 'zul']
idioma_aportando(A,X,P)<= idioma(P,A) & padre(P,Y) & idioma(Y,X)
#Mayor procentaje
def obtener_Mayor_Porcentaje(idioma,lenguajes):
    acum = []
    total= 0
    maximo = ["",0]
    for i in lenguajes:
        if idioma != i:
            num=len(idioma_aportando(idioma,i,P))
            acum+=[[i,num]]
    for j in acum:
        total+=j[1]
        if maximo[1] <= j[1]:
            maximo=[j[0],j[1]]
        else:
            maximo=maximo
    return str(maximo[0])+" "+str(((maximo[1]/total)*100))

#Todos los procentajes
def obtener_Lista_Porcentajes(idioma,lenguajes):
    acum = []
    total= 0
    maximo = ["",0]
    for i in lenguajes:
        if idioma != i:
            num=len(idioma_aportando(idioma,i,P))
            if num != 0:
                acum+=[[i,num]]
    for j in acum:
        total+=j[1]
        maximo+=[[j[0],j[1]]]
    acum+=[total]
    return acum
# -----------------------------------------------------------------------

################################### 3 ##################################
"""
Funcion para cargar los datos del archivo.
"""
# -----------------------------------------------------------------------
def leer():
    lista = []
    etymology_list=[]
    etymological_origin_list=[]
    has_derived_form_list=[]
    is_derived_from_list=[]
    etymologically_related_list=[]
    derived_list=[]
    variant_orthography_list=[]
    etymologically_list=[]
    with open('etymwn.tsv', "r",encoding= 'utf-8') as f:
        f = csv.reader(f,delimiter="\t")
        for line in f:            
            if line[1] == "rel:etymology" :
                etymology_list += [line]
            elif line[1] =="rel:etymological_origin_of" :
                etymological_origin_list += [line]
            elif line[1] =="rel:has_derived_form" :
                has_derived_form_list += [line]
            elif line[1] =="rel:is_derived_from" :
                is_derived_from_list += [line]
            elif line[1] =="rel:etymologically_related" :
                etymologically_related_list += [line]
            elif line[1] =="rel:derived" :
                derived_list += [buscar_dos_puntos_mayor_rendimiento(line)]
            elif line[1] =="rel:variant:orthography" :
                variant_orthography_list += [line]
            elif line[1] =="rel:etymologically" :
                etymologically_list += [buscar_dos_puntos_mayor_rendimiento(line)]
            else:
                print("Opcion no encontrada")
                continue
    print("TEMINE")
    lista += [etymology_list,variant_orthography_list,derived_list,etymologically_related_list,is_derived_from_list,has_derived_form_list,etymological_origin_list,etymologically_list]
    return lista

def cargar_Datos(nombre,opcion):
    for palabra in opcion:
        if palabra =="rel:etymological_origin_of" or palabra =="rel:has_derived_form" or palabra =="rel:etymologically" :
            + padre(palabra2,palabra1)
            print("Termine")
        else:
            + padre(palabra1,palabra2)
            print("Termine")

def cargarPadres(opciones, datos):
    for palabra in opciones:
        if palabra =="etymological_origin_of":
            for i in datos[6]:
                + padre(i[5],i[1])
        if palabra =="has_derived_form" :
            for i in datos[5]:
                + padre(i[5],i[1])
        if palabra =="etymologically":
            for i in datos[7]:
                + padre(i[5],i[1])
        if palabra == "etymology":
            for i in datos[0]:
                + padre(i[1],i[5])
        if palabra == "variant:orthography":
            for i in datos[1]:
                + padre(i[1],i[5])
        if palabra == "derived":
            for i in datos[2]:
                + padre(i[1],i[5])
        if palabra == "etymologically_related":
            for i in datos[3]:
                + padre(i[1],i[5])
                
        if palabra == "is_derived_from":
            for i in datos[4]:
                + padre(i[1],i[5])
    print("Padres Cargados...")
    return

def cargar_Idiomas1(opciones, datos):
    for palabra in opciones:
        if palabra =="etymological_origin_of":
            for i in datos[6]:
                + idioma(i[1],i[0])
        if palabra =="has_derived_form" :
            for i in datos[5]:
                + idioma(i[1],i[0])
        if palabra =="etymologically":
            for i in datos[7]:
                + idioma(i[1],i[0])
        if palabra == "etymology":
            for i in datos[0]:
                + idioma(i[1],i[0])
        if palabra == "variant:orthography":
            for i in datos[1]:
                + idioma(i[1],i[0])
        if palabra == "derived":
            for i in datos[2]:
                + idioma(i[1],i[0])
        if palabra == "etymologically_related":
            for i in datos[3]:
                + idioma(i[1],i[0])
        if palabra == "is_derived_from":
            for i in datos[4]:
                + idioma(i[1],i[0])
    print("Idiomas Cargados...")
    return

def cargar_Idiomas2(opciones, datos):
    for palabra in opciones:
        if palabra =="etymological_origin_of":
            for i in datos[6]:
                + idioma(i[5],i[4])
        if palabra =="has_derived_form" :
            for i in datos[5]:
                + idioma(i[5],i[4])
        if palabra =="etymologically":
            for i in datos[7]:
                + idioma(i[5],i[4])
        if palabra == "etymology":
            for i in datos[0]:
                + idioma(i[5],i[4])
        if palabra == "variant:orthography":
            for i in datos[1]:
                + idioma(i[5],i[4])
        if palabra == "derived":
            for i in datos[2]:
                + idioma(i[5],i[4])
        if palabra == "etymologically_related":
            for i in datos[3]:
                + idioma(i[5],i[4])
        if palabra == "is_derived_from":
            for i in datos[4]:
                + idioma(i[5],i[4])
    print("Idiomas2 Cargados...")
    return
        
#cargar_Datos('etymwn.tsv',["rel:etymologically","rel:derived","rel:variant:orthography","rel:etymological_origin_of","rel:etymology","rel:etymologically_related","is_derived_from","rel:has_derived_form"])
#cargar_Datos('etymwn.tsv',["rel:has_derived_form"])

def leer(nombre):
    lista = []
    etymology_list=[]
    etymological_origin_list=[]
    has_derived_form_list=[]
    is_derived_from_list=[]
    etymologically_related_list=[]
    derived_list=[]
    variant_orthography_list=[]
    etymologically_list=[]
    with open(nombre,"r",encoding= 'utf-8') as f:
        f = csv.reader(f,delimiter="\t")
        for line in f:
            if line[1] == "rel:etymology" :
                etymology_list += [buscar_dos_puntos_mayor_rendimiento(line)]
            elif line[1] =="rel:etymological_origin_of" :
                etymological_origin_list += [buscar_dos_puntos_mayor_rendimiento(line)]
            elif line[1] =="rel:has_derived_form" :
                has_derived_form_list += [buscar_dos_puntos_mayor_rendimiento(line)]
            elif line[1] =="rel:is_derived_from" :
                is_derived_from_list += [buscar_dos_puntos_mayor_rendimiento(line)]
            elif line[1] =="rel:etymologically_related" :
                etymologically_related_list += [buscar_dos_puntos_mayor_rendimiento(line)]
            elif line[1] =="rel:derived" :
                derived_list += [buscar_dos_puntos_mayor_rendimiento(line)]
            elif line[1] =="rel:variant:orthography" :
                variant_orthography_list += [buscar_dos_puntos_mayor_rendimiento(line)]
            elif line[1] =="rel:etymologically" :
                etymologically_list += [buscar_dos_puntos_mayor_rendimiento(line)]
            else:
                print("Opcion no encontrada")
                continue
    print("TEMINE")
    lista += [etymology_list, variant_orthography_list, derived_list, etymologically_related_list, is_derived_from_list, has_derived_form_list, etymological_origin_list,etymologically_list]
    return lista

#leer()        

# -----------------------------------------------------------------------

################################### 4 ##################################
"""
Funcion para conocer datos finales.
"""
# -----------------------------------------------------------------------
def conocer_resultados(palabra1,palabra2,opcion):
    if opcion==1:#Hermano
        result = hermano(palabra1,palabra2)
        if len(result) > 0:
            return "SI"
        else:
            return "NO"
    elif opcion==2:#Primo
        result = primo(palabra1,palabra2)
        if len(result) > 0:
            return "SI"
        else:
            return "NO"
    elif opcion==3:#Hijo
        
        result = hijo(palabra1,palabra2)
        if len(result) > 0:
           
            return "SI "
        else:
            return "NO"
    elif opcion==4:#Tio
        result = tio(palabra1,palabra2)
        if len(result) > 0:
            return "SI"
        else:
            return "NO"
    elif opcion==5:#palabraComun
        print("Entre en 5")
        result = palabra_comun(palabra1,palabra2,A)
        if len(result) > 0:
            string = 'palabra_comun('+palabra1+','+palabra2+',A)'
            x = pyDatalog.ask(string)
            return x
        else:
            return "No existen palabras en "+ palabra2 +" que desciendan de "+palabra1
    elif opcion==6:#palabraIdioma
        result = palabra_idioma(palabra1,palabra2)
        if len(result) > 0:
            return "SI"
        else:
            return "NO"
    elif opcion==7:#listar idiomas relacionados a una Palabra
        
        string = 'idioma_palabra('+palabra1+',A)'
        idiomas = pyDatalog.ask(string)
        print(idiomas)
        return idiomas
    
    elif opcion==8:#cantidad de palabras Comunenes entre Idiomas

        string = 'contar_palabras['+palabra1+','+palabra2+']==P'
        idiomas = pyDatalog.ask(string)
        print(idiomas)
        return idiomas
        
        return "Palabras relacionadas son: \n"+contar_palabras[palabra1,palabra2]==P
    
    elif opcion==9:#listar palabras Comunenes entre Idiomas
        string = 'listar_palabras_comunes('+palabra1+','+palabra2+',P)'
        idiomas = pyDatalog.ask(string)
        return idiomas
        
    elif opcion==10:#Idioma que mas aporta a otro
        result = obtener_Mayor_Porcentaje(palabra1,lenguajes)
        print("I   |   V \n" + "---------\n",obtener_Mayor_Porcentaje(palabra1,lenguajes))
        return result 
    
    elif opcion==11:#Idioma que mas aporta a otro
        acum = obtener_Lista_Porcentajes(palabra1,lenguajes)
        for k in acum[:-1]:
            print(str(k[0])+" "+str(((k[1]/acum[-1])*100)))
    else:
        print("No se encontro la opcion")

# -----------------------------------------------------------------------

################################### 5 ##################################
"""
Pruebas.
"""
# -----------------------------------------------------------------------

#x = leer()
def menu():
    n="S"
    K="S"
    opcion=[]
    x=leer("j.tsv")
    while True:
        while n=="S": 
            i=input("Ingrese relacion/es: ")
            opcion+=[i]
            print(opcion)
            n=input("S/N: ")
        tiempo_inicial = time()
        cargarPadres(opcion, x)
        print(padre(X,Y))
        while K=="S": 
            i=int(input("Ingrese opcion de relacion: "))
            if i==1 or i==2 or i ==3 or i==4:
                p1=input("Palabra 1: ")
                p2=input("Palabra 2: ")
                conocer_resultados(p1,p2,i)
            elif i==7:
                cargar_Idiomas1(opcion, x)
                cargar_Idiomas2(opcion, x)
                p1=input("Palabra 1: ")
                conocer_resultados(p1,p1,i)
            elif i==8 or i==9:
                cargar_Idiomas1(opcion, x)
                cargar_Idiomas2(opcion, x)
                p1=input("Idioma 1: ")
                p2=input("Idioma 2: ")
                conocer_resultados(p1,p2,i)
            elif i==10 or i==11:
                cargar_Idiomas1(opcion, x)
                cargar_Idiomas2(opcion, x)
                p1=input("Idioma 1: ")
                conocer_resultados(p1,p1,i)
            else:
                cargar_Idiomas1(opcion, x)
                cargar_Idiomas2(opcion, x)
                p1=input("Palabra 1: ")
                p2=input("Palabra 2: ")
                conocer_resultados(p1,p2,i)
            K=input("S/N: ")
        tiempo_final = time()
        print("Tiempo de ejecucion: ",(tiempo_final-tiempo_inicial)/60)
        return
    
#menu()
#tiempo_final = time()
#print("Tiempo de ejecucion: ",(tiempo_final-tiempo_inicial)/60)
#cargar_Datos2()
#conocer_resultados("pancakelike","pancake",3)
#tiempo_final = time()
#tiempo_ejecucion = tiempo_final - tiempo_inicial
#print ("El tiempo de ejecucion fue:",tiempo_ejecucion) #En segundos
#conocer_resultados("Damianist","Damian",3)# etimology
#conocer_resultados("africâner","Afrikaner",3)# "etymological_origin_of"
#conocer_resultados("pan","pancake",1)
#conocer_resultados("Aprilmaande","April",3)#afr: April	rel:has_derived_form	afr: Aprilmaande
#conocer_resultados("Aprilmaande","April",3)#afr: Aprilmaande	rel:is_derived_form	afr: April
#conocer_resultados("blut","pancake",1)#"etymologically_related"
#conocer_resultados("cerebellum","cerebrum",3)#"derived"
#conocer_resultados("Elphame","Elfhame",3)#""
#relacion_idioma("yuru","eng") Bank e,o,of Blutung
#palabras_relacionadas("pancake","spa",["is_derived_from"])



########################################################################################################################3














from tkinter import *
from tkinter import ttk
from tkinter import Image





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
        cargar_Idiomas1(opcion, x)
        cargar_Idiomas2(opcion, x)
        palabra_Idioma_interfaz()
    else:
        cargar_Idiomas1(opcion, x)
        cargar_Idiomas2(opcion, x)
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
    ventana_detalles()
def func_relacion_hija():
    # izquierda padre, derecha hijo
    p1=palabra1.get()
    p2=palabra2.get()
    palabra1.delete(0, END)
    palabra2.delete(0, END)
    lbl_res_hija["text"]=conocer_resultados(p1,p2,3) #En esta se pone el resultado de la búsqueda V/F
    ventana_detalles()
def func_relacion_tia():
    p1=palabra1.get()#sobrino
    p2=palabra2.get()#tio
    palabra1.delete(0, END)
    palabra2.delete(0, END)
    lbl_res_tia["text"]=conocer_resultados(p1,p2,4) #En esta se pone el resultado de la búsqueda V/F
    ventana_detalles()
def func_relacion_prima():
    p1 = palabra1.get()#
    p2 = palabra2.get()#
    palabra1.delete(0, END)
    palabra2.delete(0, END)
    lbl_res_primas["text"]=conocer_resultados(p1,p2,2)#En esta se pone el resultado de la búsqueda V/F
    ventana_detalles()
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
    ventana_detalles()
    if (cmbox_idioma_pal.get()=="Relacionadas"):
        palabra=palabra1.get()
        idioma=palabra2.get()
        lbl_res_relacionado.place(x=400,y=250)
        lbl_res_relacionado.config(font=("Helvetica", 30))
        lbl_res_relacionado["text"]=conocer_resultados(palabra,idioma,6)#Resultado SI/NO
        
    elif (cmbox_idioma_pal.get()=="Conjunto de palabras"):
        print("aqui")
        palabra=palabra1.get()
        idioma=palabra2.get()
        idiomas = conocer_resultados(palabra,idioma,5)
        listbox_palabras.insert(0, idiomas)
        listbox_palabras.place(x=275,y=200)
        
    else: 
        palabra=palabra1.get()
        idioma=palabra2.get()
        idiomas = conocer_resultados(palabra,idioma,7)
        palabra2.delete(0, END)
        listbox_palabras.insert(0, idiomas)
        listbox_palabras.place(x=275,y=200)
        

        
def func_idiomas():
    lbl_res_cantPal.place(x=350,y=2500)
    listbox_palabras.place(x=275,y=2000)
    listbox_palabras.delete(0, END)
    ventana_detalles()
    if (cmbox_idioma.get()=="Contar palabras en común"):
        print("aqui")
        idioma1=palabra1.get()
        idioma2=palabra2.get()
        idiomas = conocer_resultados(idioma1,idioma2,8)
        lbl_res_cantPal.place(x=400,y=250)
        lbl_res_cantPal.config(font=("Helvetica", 30))
        lbl_res_cantPal["text"]=idiomas #Cantidad
        
    elif (cmbox_idioma_pal.get()=="Listar palabras comunes"):
        idioma1=palabra1.get()
        idioma2=palabra2.get()
        idiomas = conocer_resultados(idioma1,idioma2,9)
        listbox_palabras.insert(0, idiomas)
        listbox_palabras.place(x=275,y=200)
        
    elif (cmbox_idioma.get()=="Idioma que más aportó"):
        pala1=palabra1.get()
        pala2=palabra1.get()
        palabra1.delete(0, END)
        palabra2.delete(0, END)
        idiomas = conocer_resultados(pala1,pala2,10)
        lbl_res_cantPal.place(x=400,y=250)
        lbl_res_cantPal.config(font=("Helvetica", 30))
        
        print("Soy idiomas",idiomas)
        lbl_res_cantPal["text"]=idiomas#Idioma y porcentaje
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


def ventana_detalles():
    detalles = Toplevel()
    detalles.geometry("400x300")
    detalles.resizable(width=False, height=False)
    detalles.title("Detalles")
    detalles["bg"]="black"
    listbox_detalles = Listbox(detalles,width=40, height=15)
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
