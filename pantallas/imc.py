import tkinter as tk
from tkinter import ttk

from componentes_ui.ui_base_screen import UIBaseScreen
from componentes_ui.layout_utils import crear_scrollable_container, crear_columnas

# Módulos IMC
from modulos.imc_form import construir_formulario
from modulos.imc_resultados import construir_panel_resultados, actualizar_resultados
from modulos.imc_graficos import construir_panel_graficos, actualizar_grafico
from modulos.imc_core import calcular_imc_completo

# Nuevas tarjetas clínicas
from modulos.imc_detalles import (
    crear_tarjeta_analisis,
    actualizar_tarjeta_analisis,
    crear_tarjeta_recomendaciones,
    actualizar_tarjeta_recomendaciones,
    crear_tarjeta_riesgos,
    actualizar_tarjeta_riesgos,
)


class PantallaIMC(UIBaseScreen):
    def __init__(self, parent, controller):
        super().__init__(
            parent,
            controller,
            titulo="Cálculo de IMC",
            subtitulo="Evaluación del estado nutricional"
        )

        # ---------------------------------------------------
        # CONTENEDOR SCROLLEABLE (zona izquierda)
        # ---------------------------------------------------
        contenedor = crear_scrollable_container(self)

        # ---------------------------------------------------
        # DIVIDIR EN 2 COLUMNAS (izquierda / derecha)
        # ---------------------------------------------------
        col_izq, col_der = crear_columnas(contenedor, num_columnas=2, separacion=40)

        # ---------------------------------------------------
        # FORMULARIO EN LA COLUMNA IZQUIERDA
        # ---------------------------------------------------
        construir_formulario(col_izq, self.on_calcular)

        # ---------------------------------------------------
        # PANEL DE RESULTADOS EN COLUMNA IZQUIERDA
        # ---------------------------------------------------
        self.panel_resultados = construir_panel_resultados(col_izq)

        # ---------------------------------------------------
        # TARJETAS CLÍNICAS EN COLUMNA DERECHA
        # ---------------------------------------------------
        self.tarjeta_analisis = crear_tarjeta_analisis(col_der)
        self.tarjeta_recomendaciones = crear_tarjeta_recomendaciones(col_der)
        self.tarjeta_riesgos = crear_tarjeta_riesgos(col_der)

        # ---------------------------------------------------
        # GRÁFICO IMC (DEBAJO)
        # ---------------------------------------------------
        self.panel_graficos = construir_panel_graficos(self)


    # ============================================================
    # CALLBACK: CALCULAR IMC
    # ============================================================
    def on_calcular(self, peso, talla, edad):
        datos = calcular_imc_completo(peso, talla, edad)

        # Resultado básico (IMC + estado)
        actualizar_resultados(self.panel_resultados, datos)

        # Análisis clínico (peso ideal, kcal, % ideal)
        actualizar_tarjeta_analisis(self.tarjeta_analisis, datos)

        # Recomendaciones
        actualizar_tarjeta_recomendaciones(self.tarjeta_recomendaciones, datos["recomendaciones"])

        # Riesgos
        actualizar_tarjeta_riesgos(self.tarjeta_riesgos, datos["riesgos"])

        # Gráfico IMC
        actualizar_grafico(self.panel_graficos, datos)
