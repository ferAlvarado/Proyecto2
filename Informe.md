# Instituto Tecnológico de Costa Rica.
## Ingeniería en computación
## Escuela de Computación - Sede Cartago.
## Inteligencia Artificial.
## II Semestre 2018.
## Proyecto 2: Relaciones etimológicas.
## Profesor: Juan Esquivel.
## Estudiantes: 
                 Fernanda Alvarado.
                 Freyser Jímenez.
                 Minor Sancho.

# Sección 1. Introducción.
La derivación lógica es un algoritmo utilizado en Inteligencia Artificial para obtener la solución más óptima de un problema,el propósito de este proyecto es procesar un conjunto de datos por medio de derivación lógica. 
Los datos que se van a procesar son relaciones etimológicas entre palabras de diferentes idiomas; estos datos se extraen de la base de la base de datos "Etymological Wordnet", la cual se basa en  basada en en.wiktionary.org que recopila relaciones entre palabras en múltiples idiomas (aunque iniciando desde inglés). Tomando estos datos, se puede construir un sistema que, basado en proposiciones lógicas, nos permita responder preguntas relacionadas con orígen común de palabras, similitud entre lenguajes, etc. El proyecto se va a desarrollar con la biblioteca pyDatalog, la cual es una adaptación de un lenguaje lógico en alto nivel y actualmente es muy utilizado en esta rama para realizar multiples proyecto, esto se debe a que es fácil de aprender y se adapta a las necesidades de los desarrolladores.
# Sección 2. Descripción de instalación.
Para instalar este proyecto:
1. Descargas la base de datos .tsv: http://www1.icsi.berkeley.edu/~demelo/etymwn
2. Descargar el proyecto https://github.com/ferAlvarado/Proyecto2.
3. Una vez descargado el proyecto se debe descomprimir en el directorio que desee.
4. Para que el proyecto funcione correctamente, la base de datos ddescargada se debe copiar en la carpeta donde se ejecuta el proyecto; en este caso: /tec/ia/p2/g02.
5. Ejecutar el archivo: 
# Sección 3. Manual de usuario.
Manual de usuario:https://github.com/ferAlvarado/Proyecto2/blob/master/Manual%20de%20instalaci%C3%B3n.md
# Sección 4. Resultados.
# Sección 5. Detalles de implementación.
## Manejo de datos.
Los datos que utiliza el código desarrollado son los de la base de datos "Etymological Wordnet", este es un archivo .tsv; para trabajar primero se lee el archivo; una vez realizada esta tarea, se almacenan en una lista que los separa según la relación; esto permite que la búsqueda sea ms eficiente ya que cada relación es la "llave primaria" de cada sublista. 
Para leer el archivo se utiliza la siguiente función:
```sh
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
    lista += [etymology_list, variant_orthography_list, derived_list, etymologically_related_list,
              is_derived_from_list, has_derived_form_list, etymological_origin_list,etymologically_list]
    return lista
```
La lista que almacena los datos leídos es la siguiente:
```sh
lista += [etymology_list, variant_orthography_list, derived_list, etymologically_related_list,
          is_derived_from_list, has_derived_form_list, etymological_origin_list,etymologically_list]
```
## Estructuras de control.
Para construir las estructura utilizadas en el proecto se utilizó la biblioteca pyDatalog; y se hace de la siguiente manera:
```sh
from pyDatalog import pyDatalog
import csv
from time import time

pyDatalog.create_atoms('idioma_aportando,contar_palabras,
                       padre,hermano,tio,primo,hijo,palabra_idioma,idioma_palabra,
                       contar_palabras_comunes,listar_palabras_comunes,ancestro,
                       descendiente,idioma,palabra_comun,P,X,Y,A,B')
```                      

# Distribución de trabajo.
     -------------------------------------------------------
     -           Nombre          -     % Aporte            -
     -------------------------------------------------------
     -     Fernanda Alvarado     -                         -
     -------------------------------------------------------
     -      Freyser Jímenez      -                         -
     -------------------------------------------------------
     -       Minor Sancho        -                         -
     -------------------------------------------------------
