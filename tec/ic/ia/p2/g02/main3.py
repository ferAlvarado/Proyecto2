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


from pyDatalog import pyDatalog
import csv
from time import time
#import pandas as pd
import numpy as np
pyDatalog.create_atoms('idioma_aportando,contar_palabras,padre,\
                        hermano,tio,primo,hijo,palabra_idioma,idioma_palabra,\
                        contar_palabras_comunes,listar_palabras_comunes,\
                        ancestro,descendiente,idioma,palabra_comun,P,X,Y,A,B'
                       )
lenguajes= ['ara', 'ave', 'akk', 'aaq', 'abe', 'abs','adt', 'afr', 'aii',
    'ain', 'akz', 'ale','alq', 'amh', 'amj', 'ang', 'apw', 'arg',
    'arn', 'arq', 'arw', 'ary', 'arz', 'ase','ast', 'auc', 'ava',
    'axm', 'ayl', 'aym','aze', 'bak', 'bar', 'bdy', 'bel', 'ben',
    'bft', 'bis', 'bod', 'bre', 'bua', 'bul','byn', 'cat', 'ccc',
    'ceb', 'ces', 'cha','chc', 'che', 'chn', 'cho', 'chr', 'chu',
    'cic', 'cmn', 'cop', 'cor', 'cre', 'crh','csb', 'cym', 'dan',
    'del', 'dep', 'deu','div','dsb','dtd','dum','efi','egy','ell',
    'emn','eng','enm','enn','epo','ess','est','eus','evn','ewe',
    'fao','fas','fij','fin', 'fon','fra', 'frc', 'frk', 'frm',
    'fro', 'frp', 'fry', 'fur', 'gae', 'gez', 'gil', 'gla', 'gle',
    'glg', 'glv', 'gmh', 'gml', 'gmy', 'goh', 'got', 'grc', 'grn',
    'grv', 'gsw', 'gug', 'guj', 'gul', 'gwi', 'hak', 'hat', 'hau',
    'haw', 'hbs', 'heb', 'hif', 'hil', 'hin', 'hit', 'hop', 'hsb',
    'hun', 'hur', 'hye', 'idb', 'ido', 'ike', 'ikt', 'iku', 'ina',
    'ind', 'inz', 'ipk', 'isl', 'ita','jam', 'jav', 'jbo', 'jpn',
    'kal', 'kan', 'kat', 'kaw', 'kaz', 'kbd', 'khm', 'kin', 'kir',
    'kjh', 'kju', 'kky', 'kld', 'kmb', 'kok', 'kon', 'kor', 'kri',
    'krl', 'ksd', 'ksh', 'kum', 'kur', 'kzj', 'lad', 'lao', 'lat',
    'lav', 'lij', 'lim', 'lin', 'lit', 'liv', 'lkt', 'lld', 'lmo',
    'lng', 'lou', 'ltc', 'ltz', 'lua', 'lug', 'luo', 'lut', 'lzh',
    'mah', 'mak', 'mal', 'mar', 'mas', 'mav', 'mbc', 'mfr', 'mga',
    'mic', 'min', 'mkd', 'mlg', 'mlt', 'mnc', 'mnk', 'mod', 'moe',
    'moh', 'mon', 'mri', 'msa', 'mwl', 'mxi', 'mya', 'myv', 'nah',
    'nan', 'nap', 'naq', 'nav', 'nay', 'nci', 'ndo', 'nds', 'nep',
    'nld','nno', 'nob', 'non', 'nor', 'nov', 'nys', 'obr', 'obt',
    'oci', 'oco', 'odt', 'ofs', 'oge', 'oji', 'okm', 'ood', 'orc',
    'ori', 'orv', 'osp', 'oss', 'osx', 'ota', 'otk', 'owl', 'p_gem',
    'p_gmw', 'p_ine', 'p_sla', 'pal', 'pan', 'pap', 'pau', 'pcd',
    'pdt', 'peo', 'phn', 'pim', 'pis', 'pjt', 'pli', 'pml', 'pol',
    'por', 'pox', 'ppl', 'prg', 'pro', 'pus', 'quc', 'que', 'qwc',
    'rap', 'rhg', 'rme', 'rmf', 'rmq', 'roh', 'rom', 'ron', 'rop',
    'rue', 'ruo', 'rup', 'rus', 'ryu', 'san', 'sat', 'scn', 'sco',
    'see', 'sei', 'sga', 'shh', 'sin', 'slk', 'slv', 'sme', 'smo',
    'sms', 'sna', 'som', 'sot', 'spa', 'sqi', 'srd', 'srn', 'srs',
    'stg', 'sth', 'stq', 'sun', 'sux', 'swa', 'swe', 'syc', 'szl',
    'tah', 'tam', 'tat', 'tcs', 'tcy', 'tel', 'tet', 'tew', 'tgk',
    'tgl', 'tha', 'tir', 'tiv', 'tnq', 'ton', 'tpi', 'tpw', 'tsn',
    'tuk', 'tur', 'twf', 'twi', 'txb', 'tzm', 'uga', 'uig', 'ukr',
    'ulk', 'umb', 'umu', 'urd', 'uzb', 'vai', 'vec', 'vep', 'vie',
    'vls', 'vma', 'vol', 'wam', 'wit', 'wlm', 'wln', 'wol', 'wrh',
    'wym', 'xaa', 'xbm', 'xce', 'xcl', 'xho', 'xmb', 'xng', 'xno',
    'xnt', 'xon', 'xpr', 'xtg', 'xto', 'yid', 'yol', 'yor', 'yua',
    'yue', 'yur', 'yxg', 'zai', 'zko', 'zku', 'zsm', 'zul'
    ]
lenguajes1=['idioma_x','idioma_y','idioma_z']
################################### 1 ##################################
"""
Funcion que nos permite obtener los datos de cada linea del archivo.
"""
# -----------------------------------------------------------------------
def buscar_dos_puntos_mayor_rendimiento(
        lista):
    acum = []
    for i in lista:
        pos=i.find(':')
        acum +=[i[0:pos]]
        palabra=i[pos+1:len(i)]
        if palabra[0]==' ':
            acum +=[palabra[1:]]
        else:
            acum +=[palabra]
    return acum
"""
Definicion de clausulas de logica.
"""
hermano(X,Y) <= padre(X,P) & padre(Y,P)  & (X!=Y)
#hijo es X y padre es Y
hijo(X,Y) <= padre(X,Y)
#primero X = sobrino y segundo Y = tio
tio(X,Y) <= padre(X,P) & hermano(Y,P)
# X = primo 1 y Y = primo 2
primo(X,Y) <= padre(X,A) & tio(Y,A)
#A MAYOR Y B MENOR
descendiente(B,A) <= padre(B,A)
descendiente(B,A) <= padre(B,P) & descendiente(P,A)
#A MAYOR Y Y MENOR
ancestro(A,Y) <= descendiente(Y,A)
#X igual palabra y Y igual idioma
palabra_idioma(X,Y) <= idioma(X,Y)
palabra_idioma(X,Y) <= descendiente(X,P) & idioma(P,Y)
palabra_idioma(X,Y) <= ancestro(X,P) & idioma(P,Y)
#X palabra y Y idioma
palabra_comun(X,Y,A) <= idioma(A,Y) & padre(A,X)
#X palabra y Y resultado
idioma_palabra(X,Y) <= idioma(X,Y)
idioma_palabra(X,Y) <= descendiente(X,P) & idioma(P,Y)
idioma_palabra(X,Y) <= ancestro(X,P) & idioma(P,Y)
#X palabra y Y resultado
listar_palabras_comunes(X,Y,P) <= idioma(P,X) & idioma(P,Y)
#Contar
contar_palabras_comunes(X,Y) <= idioma(P,X) & idioma(P,Y)
(contar_palabras[X,Y] == len_(P)) <= listar_palabras_comunes(X,Y,P)
#=================idiomasAportandoaOtro=================
#X palabra y Y resultado
idioma_aportando(A,X,P)<= idioma(P,A) & padre(P,Y) & idioma(Y,X)


def obtener_Mayor_Porcentaje(
        idioma,lenguajes):
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


def obtener_Lista_Porcentajes(
        idioma,lenguajes):
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


"""
Funcion para cargar los datos del archivo.
"""
def leer(
        nombre):
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
                etymology_list += [
                    buscar_dos_puntos_mayor_rendimiento(line)
                    ]
            elif line[1] =="rel:etymological_origin_of" :
                etymological_origin_list += [
                    buscar_dos_puntos_mayor_rendimiento(line)
                    ]
            elif line[1] =="rel:has_derived_form" :
                has_derived_form_list += [
                    buscar_dos_puntos_mayor_rendimiento(line)
                    ]
            elif line[1] =="rel:is_derived_from" :
                is_derived_from_list += [
                    buscar_dos_puntos_mayor_rendimiento(line)
                    ]
            elif line[1] =="rel:etymologically_related" :
                etymologically_related_list += [
                    buscar_dos_puntos_mayor_rendimiento(line)
                    ]
            elif line[1] =="rel:derived" :
                derived_list += [
                    buscar_dos_puntos_mayor_rendimiento(line)
                    ]
            elif line[1] =="rel:variant:orthography" :
                variant_orthography_list += [
                    buscar_dos_puntos_mayor_rendimiento(line)
                    ]
            elif line[1] =="rel:etymologically" :
                etymologically_list += [
                    buscar_dos_puntos_mayor_rendimiento(line)
                    ]
            else:
                print("Opcion no encontrada")
                continue
    print("TEMINE")
    lista += [
        etymology_list, variant_orthography_list, derived_list,
        etymologically_related_list, is_derived_from_list,
        has_derived_form_list, etymological_origin_list,
        etymologically_list
        ]
    return lista


"""
Funcion para cargar los padres dependiendo la relacion en el archivo.
"""
# -----------------------------------------------------------------------
def cargarPadres(
        opciones, datos):
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
    return


"""
Funcion para emparejar los idiomas dependiendo la relacion en el archivo.
"""
def cargar_Idiomas1(
        opciones, datos, valor):
    for palabra in opciones:
        if palabra =="etymological_origin_of":
            for i in datos[6]:
                if valor==1:
                    + idioma(i[1],i[0])
                else:
                    + idioma(i[5],i[4])
        if palabra =="has_derived_form" :
            for i in datos[5]:
                if valor==1:
                    + idioma(i[1],i[0])
                else:
                    + idioma(i[5],i[4])
        if palabra =="etymologically":
            for i in datos[7]:
                if valor==1:
                    + idioma(i[1],i[0])
                else:
                    + idioma(i[5],i[4])
        if palabra == "etymology":
            for i in datos[0]:
                if valor==1:
                    + idioma(i[1],i[0])
                else:
                    + idioma(i[5],i[4])
        if palabra == "variant:orthography":
            for i in datos[1]:
                if valor==1:
                    + idioma(i[1],i[0])
                else:
                    + idioma(i[5],i[4])
        if palabra == "derived":
            for i in datos[2]:
                if valor==1:
                    + idioma(i[1],i[0])
                else:
                    + idioma(i[5],i[4])
        if palabra == "etymologically_related":
            for i in datos[3]:
                if valor==1:
                    + idioma(i[1],i[0])
                else:
                    + idioma(i[5],i[4])
        if palabra == "is_derived_from":
            for i in datos[4]:
                if valor==1:
                    + idioma(i[1],i[0])
                else:
                    + idioma(i[5],i[4])
    print("Idiomas Cargados...")
    return
"""
Funcion para conocer datos finales, de opcion conocida.
"""
def conocer_resultados(
        palabra1,palabra2,opcion):
    if opcion==1:
        result = hermano(
            palabra1,palabra2
            )
        if len(result) > 0:
            return "SI"
        else:
            return "NO"
    elif opcion==2:
        result = primo(
            palabra1,palabra2
            )
        if len(result) > 0:
            return "SI"
        else:
            return "NO"
    elif opcion==3:
        result = hijo(
            palabra1,palabra2
            )
        if len(result) > 0:
            return "SI "
        else:
            return "NO"
    elif opcion==4:
        result = tio(
            palabra1,palabra2
            )
        if len(result) > 0:
            return "SI"
        else:
            return "NO"
    elif opcion==5:
        print("Entre en 5")
        result = palabra_comun(
            palabra1,palabra2,A
            )
        if len(result) > 0:
            string = 'palabra_comun('+palabra1+','+palabra2+',A)'
            x = pyDatalog.ask(string)
            return x
        else:
            return "No existen palabras en "+ palabra2 +" \
                    que desciendan de "+palabra1
    elif opcion==6:
        result = palabra_idioma(
            palabra1,palabra2
            )
        if len(result) > 0:
            return "SI"
        else:
            return "NO"
    elif opcion==7:
        string = 'idioma_palabra('+palabra1+',A)'
        idiomas = pyDatalog.ask(string)
        print(idiomas)
        return idiomas
    elif opcion==8:
        string = 'contar_palabras['+palabra1+','+palabra2+']==P'
        idiomas = pyDatalog.ask(string)
        print(idiomas)
        return idiomas
        return "Palabras relacionadas son: \n\
                "+contar_palabras[palabra1,palabra2]==P
    elif opcion==9:#listar palabras Comunenes entre Idiomas
        string = 'listar_palabras_comunes('+palabra1+','+palabra2+',P)'
        idiomas = pyDatalog.ask(string)
        return idiomas
    elif opcion==10:#Idioma que mas aporta a otro
        result = obtener_Mayor_Porcentaje(palabra1,lenguajes)
        print("I   |   V \n" + "---------\n",
              obtener_Mayor_Porcentaje(
                  palabra1,lenguajes)
              )
        return result 
    elif opcion==11:#Idioma que mas aporta a otro
        acum = obtener_Lista_Porcentajes(
            palabra1,lenguajes
            )
        for k in acum[:-1]:
            print(str(k[0])+" "+str(((k[1]/acum[-1])*100)))
    else:
        print("No se encontro la opcion")
