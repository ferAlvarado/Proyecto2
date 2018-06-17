"""
=====================================
Proyecto Corto #2 ­ Unittest
=====================================
:Institucion: Instituto Tecnologico de Costa Rica
:Curso: Inteligencia Artificial
:Grupo: 2
:Semestre: I Semestre 2018
:Autores: Fernanda Alvarado Vargas,fernadaalvarado95@gmail.com
          Minor Sancho Valverde,tivin.minor10@gmail.com
          Freyser Jimenez Mena, fjimenez577@gmail.com
:Fecha: 23/05/2018

Dependencias con archivos de entrada:
- datos.csv
"""
#-----------------------------------------------------------------------
import os
import sys
import csv
import random
import pytest
import unittest
from main3 import *
os . system('ls -lah')
+ hermano("Hermano de papa de Freyser","Papa de Freyser")
+ padre("Freyser","Papa de Freyser")
+ padre("Minor","Papa de Minor")
+ padre("Fer","Papa de Fer")
+ padre("hermano de Freyser","Papa de Freyser")
+ padre("hermano de Minor","Papa de Minor")
+ padre("hermano de Fer","Papa de Fer")
+ padre("hijo de Freyser","Freyser")
+ padre("hijo de hermano de Freyser","hermano de Freyser")

+ idioma("Papa de Freyser","idioma_x")
+ idioma("Freyser","idioma_y")
+ idioma("hijo de Freyser","idioma_y")
+ idioma("Fer","idioma_x")
+ idioma("Fer","idioma_y")


class TestUM(
        unittest.TestCase):
   
    def setUp(
            self):
        pass

    
    """
    Funcion que nos testea como obtener los datos de cada linea del archivo.
    """
    def test_buscar_dos_puntos_mayor_rendimiento(
                self):
            print("__________________________________________________________________\n")
            print("Test : buscar_dos_puntos_mayor_rendimiento(Lista)")
            entrada = [
                "aaq: Pawanobskewi",
                "rel:etymological_origin_of",
                "eng: Penobscot"
                ]
            resultado = [
                "aaq","Pawanobskewi",
                "rel","etymological_origin_of",
                "eng","Penobscot"
                ]
            self.assertEqual(
                buscar_dos_puntos_mayor_rendimiento(entrada),
                resultado
                )

            
    """
    Funcion que nos teste la funcion logica de padre.
    """
    def test_padre(
            self):
        print("__________________________________________________________________\n")
        print("Test : padre(X,Y)")
        entrada = 'padre("Freyser",Y)'
        resultado = {('Papa de Freyser',)}
        self.assertEqual(
            pyDatalog.ask(entrada),
            resultado
            )

        
    """
    Funcion que nos teste la funcion logica de hermano.
    """
    def test_hermano(
            self):
        print("__________________________________________________________________\n")
        print("Test : hermano(X,Y)")
        entrada = 'hermano("Freyser",Y)'
        resultado = {('hermano de Freyser',)}
        self.assertEqual(
            pyDatalog.ask(entrada),resultado
            )

        
    """
    Funcion que nos teste la funcion logica de hijo.
    """
    def test_hijo(
            self):
        print("__________________________________________________________________\n")
        print("Test : hijo(X,Y)")
        entrada = 'hijo(X,"Papa de Freyser")'
        resultado = {('Freyser',), ('hermano de Freyser',)}
        self.assertEqual(
            pyDatalog.ask(entrada),
            resultado
            )

        
    """
    Funcion que nos teste la funcion logica de tio.
    """
    def test_tio(
            self):
        print("__________________________________________________________________\n")
        print("Test : tio(X,Y)")
        entrada = 'tio("Freyser",Y)'
        resultado = {('Hermano de papa de Freyser',)}
        self.assertEqual(
            pyDatalog.ask(entrada),
            resultado
            )

        
    """
    Funcion que nos teste la funcion logica de primo.
    """
    def test_primo(self):
        print("__________________________________________________________________\n")
        print("Test : primo(X,Y)")
        entrada = 'primo("hijo de Freyser",Y)'
        resultado = {('hijo de hermano de Freyser',)}
        self.assertEqual(
            pyDatalog.ask(entrada),
            resultado
            )

        
    """
    Funcion que nos teste la funcion logica de descendientes.
    """
    def test_descendiente(
            self):
        print("__________________________________________________________________\n")
        print("Test : descendiente(X,Y)")
        entrada = 'descendiente("hijo de Freyser",Y)'
        resultado = {('Freyser',), ('Papa de Freyser',)}
        self.assertEqual(
            pyDatalog.ask(entrada),
            resultado
            )

        
    """
    Funcion que nos teste la funcion logica de ancestros.
    """
    def test_ancestro(
            self):
        print("__________________________________________________________________\n")
        print("Test : ancestro(X,Y)")
        entrada = 'ancestro("Papa de Freyser",Y)'
        resultado = {('hijo de hermano de Freyser',),
                     ('hijo de Freyser',), ('hermano de Freyser',),
                     ('Freyser',)}
        self.assertEqual(
            pyDatalog.ask(entrada),
            resultado
            )

        
    """
    Funcion que nos teste la funcion logica de palabra_idioma que nos permite
    conocer los idiomas relacionados a una palabra.
    """
    def test_palabra_idioma(
            self):
        print("__________________________________________________________________\n")
        print("Test : palabra_idioma(X,Y)")
        entrada = 'palabra_idioma("Papa de Freyser",Y)'
        resultado = {('idioma_x',), ('idioma_y',)}
        self.assertEqual(
            pyDatalog.ask(entrada),
            resultado
            )

        
    """
    Funcion que nos teste la funcion logica de palabra_comun que nos permite
    Obtener el conjunto de todas las palabras en un idioma originadas por
    una palabra específica.
    """
    def test_palabra_comun(
            self):
        print("__________________________________________________________________\n")
        print("Test : palabra_comun(X,Y,A).")
        entrada = 'palabra_comun("Papa de Freyser","idioma_y",Y)'
        resultado = {('Freyser',)}
        self.assertEqual(
            pyDatalog.ask(entrada),
            resultado
            )

        
    """
    Test de la funcion logica de  idioma_palabra(X,Y) que nos permite
    determinar si una palabra está relacionada con un idioma (Si / No).
    """
    def test_idioma_palabra(
            self):
        print("__________________________________________________________________\n")
        print("Test : idioma_palabra(X,Y) .")
        entrada = 'idioma_palabra("Papa de Freyser",Y)'
        resultado = {('idioma_y',), ('idioma_x',)}
        self.assertEqual(
            pyDatalog.ask(entrada),resultado
            )

        
    """
    Test de la funcion logica de  listar_palabras_comunes(X,Y,P) que nos permite
    Listar todas las palabras comunes entre dos idiomas.
    """
    def test_listar_palabras_comunes(
            self):
        print("__________________________________________________________________\n")
        print("Test : listar_palabras_comunes(X,Y,P) .")
        entrada = 'listar_palabras_comunes("idioma_x", "idioma_y",P)'
        resultado = {('Fer',)}
        self.assertEqual(
            pyDatalog.ask(entrada),
            resultado
            )

        
    """
    Test de la funcion logica de  contar_palabras[X,Y] == len_(P) que nos permite
    Contar todas las palabras comunes entre dos idiomas  .
    """
    def test_contar_palabras(
            self):
        print("__________________________________________________________________\n")
        print("Test : contar_palabras[X,Y] .")
        entrada = 'contar_palabras["idioma_x", "idioma_y"] == P'
        resultado = {(1,)}
        self.assertEqual(
            pyDatalog.ask(entrada),
            resultado
            )

        
    """
    Test de la funcion logica de  obtener_Lista_Porcentajes(idioma,lenguajes) que nos permite
    Contar todas las palabras comunes entre dos idiomas  .
    """
    def test_obtener_Lista_Porcentajes(
            self):
        print("__________________________________________________________________\n")
        print("Test : obtener_Lista_Porcentajes(idioma,lenguajes) .")
        entrada = "idioma_y"
        resultado = ['idioma_x', 1]
        self.assertEqual(
            obtener_Lista_Porcentajes(entrada,lenguajes1)[0],
            resultado
            )

        
    """
    Test de la funcion logica de  obtener_Mayor_Porcentaje(idioma,lenguajes) que nos permite
    Contar todas las palabras comunes entre dos idiomas  .
    """
    # -----------------------------------------------------------------------
    def test_obtener_Mayor_Porcentaje(
            self):
        print("__________________________________________________________________\n")
        print("Test : obtener_Mayor_Porcentaje(idioma,lenguajes) .")
        entrada = "idioma_y"
        resultado = "idioma_x 100.0"
        self.assertEqual(
            obtener_Mayor_Porcentaje(entrada,lenguajes1),
            resultado
            )

        
    """
    Test de la funcion leer(nombre) que nos permite leer el archivo y obtener
    los datos en una lista.
    """
    def test_leer(
            self):
        print("__________________________________________________________________\n")
        print("Test : leer(nombre) .")
        entrada = "prueba.tsv"
        resultado = [
            [['aaq', 'senabe', 'rel', 'etymology', 'eng', 'sannup']],
            [['abs', 'beta', 'rel', 'variant:orthography', 'zsm', 'beta']],
            [], [], [['abe', 'waniigan', 'rel', 'is_derived_from', 'eng', 'wannigan']],
            [['abe', 'waniigan', 'rel', 'has_derived_form', 'eng', 'wangan']],
            [['aaq', 'Pawanobskewi', 'rel', 'etymological_origin_of', 'eng', 'Penobscot']],
            []
            ]
        self.assertEqual(
            leer(entrada),resultado
            )

        
    """
    Test de la funcion cargarPadres(relaciones, datos) que nos permite obtener
    los padres correspondientes para cada palabra, tomando en cuenta le lista
    de relaciones que se le ingrese.
    """
    # -----------------------------------------------------------------------
    def test_cargarPadres(
            self):
        print("__________________________________________________________________\n")
        print("Test : cargarPadres(relaciones, datos) .")
        entrada1 = leer("prueba.tsv")
        entrada2 = ["etymological_origin_of",
                    "variant:orthography"]
        cargarPadres(entrada2, entrada1)
        print(pyDatalog.ask('padre(X,Y)'))
        resultado = {('hermano de Freyser', 'Papa de Freyser'),
                     ('hermano de Minor', 'Papa de Minor'),
                     ('Fer', 'Papa de Fer'), ('Minor', 'Papa de Minor'),
                     ('Freyser', 'Papa de Freyser'),
                     ('Penobscot', 'Pawanobskewi'),
                     ('hijo de hermano de Freyser', 'hermano de Freyser'),
                     ('hijo de Freyser', 'Freyser'),
                     ('hermano de Fer', 'Papa de Fer'),
                     ('beta', 'beta')
                     }
        self.assertEqual(
            pyDatalog.ask('padre(X,Y)'),
            resultado
            )

        
    """
    Test de la funcion cargar_Idiomas1(relaciones, datos, valor) que nos permite obtener
    los idiomas correspondientes para cada palabra, tomando en cuenta le lista
    de relaciones que se le ingrese.
    """
    def test_cargar_Idiomas1(
            self):
        print("__________________________________________________________________\n")
        print("Test : cargar_Idiomas1(relaciones, datos,valor) .")
        entrada1 = leer("prueba.tsv")
        entrada2 = ["etymological_origin_of",
                    "variant:orthography"
                    ]
        cargar_Idiomas1(entrada2, entrada1,2)
        resultado = {('hijo de Freyser', 'idioma_y'),
                     ('Penobscot', 'eng'), ('beta', 'zsm'),
                     ('Fer', 'idioma_x'), ('Papa de Freyser', 'idioma_x'),
                     ('Fer', 'idioma_y'), ('Freyser', 'idioma_y')
                     }
        self.assertEqual(
            pyDatalog.ask('idioma(X,Y)'),
            resultado
            )

        
    """
    Test de la funcion conocer_resultados(palabra1,palabra2,opcion) que nos permite
    conocer datos finales, de opcion conocida.
    """
    def test_conocer_resultados(
            self):
        print("__________________________________________________________________\n")
        print("Test : conocer_resultados(palabra1,palabra2,opcion) .")
        entrada1 = "Hermano de papa de Freyser"
        entrada2 = "Papa de Freyser"
        resultado = "SI"
        self.assertEqual(
            conocer_resultados(entrada1,entrada2,1),
            resultado)

        
if __name__ == '__main__':
    unittest.main()
