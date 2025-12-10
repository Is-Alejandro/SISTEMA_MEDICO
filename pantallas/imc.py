import tkinter as tk
from tkinter import ttk

from componentes_ui.ui_base_screen import UIBaseScreen
from componentes_ui.layout_utils import crear_columnas

from modulos.imc_form import construir_formulario
from modulos.imc_resultados import construir_panel_resultados, actualizar_resultados
from modulos.imc_graficos import construir_panel_graficos, actualizar_grafico
from modulos.imc_core import calcular_imc_completo

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
        # CONTENEDOR PRINCIPAL
        # ---------------------------------------------------
        contenedor = tk.Frame(self, bg="white")
        contenedor.pack(fill="both", expand=True, padx=20, pady=20)

        # ---------------------------------------------------
        # 5 COLUMNAS (la solución correcta)
        # ---------------------------------------------------
        col_form, col_result, col_ana, col_reco, col_ries = crear_columnas(
            contenedor,
            num_columnas=5,
            separacion=20
        )

        # ---------------------------------------------------
        # COLUMNA 1 → FORMULARIO
        # ---------------------------------------------------
        construir_formulario(col_form, self.on_calcular)

        # ---------------------------------------------------
        # COLUMNA 2 → RESULTADOS IMC
        # ---------------------------------------------------
        card_resultados = self._crear_card(col_result, "Resultados del IMC")
        self.panel_resultados = construir_panel_resultados(card_resultados)

        # ---------------------------------------------------
        # COLUMNA 3 → ANÁLISIS CLÍNICO
        # ---------------------------------------------------
        card_analisis = self._crear_card(col_ana, "Análisis clínico")
        self.tarjeta_analisis = crear_tarjeta_analisis(card_analisis)

        # ---------------------------------------------------
        # COLUMNA 4 → RECOMENDACIONES
        # ---------------------------------------------------
        card_recomendaciones = self._crear_card(col_reco, "Recomendaciones")
        self.tarjeta_recomendaciones = crear_tarjeta_recomendaciones(card_recomendaciones)

        # ---------------------------------------------------
        # COLUMNA 5 → RIESGOS CLÍNICOS
        # ---------------------------------------------------
        card_riesgos = self._crear_card(col_ries, "Riesgos clínicos")
        self.tarjeta_riesgos = crear_tarjeta_riesgos(card_riesgos)

        # ---------------------------------------------------
        # GRÁFICO INFERIOR
        # ---------------------------------------------------
        self.panel_graficos = construir_panel_graficos(self)

    # ---------------------------------------------------
    # FUNCIÓN PARA CREAR UNA CARD REUTILIZABLE
    # ---------------------------------------------------
    def _crear_card(self, parent, titulo):
        card = tk.Frame(
            parent,
            bg="white",
            highlightthickness=1,
            highlightbackground="#D0D0D0",
            padx=15,
            pady=15
        )
        card.pack(fill="both", expand=True)

        lbl = ttk.Label(
            card,
            text=titulo,
            font=("Segoe UI", 14, "bold"),
            foreground="#0ea5e9",
            background="white"
        )
        lbl.pack(anchor="w", pady=(0, 10))

        return card

    # ---------------------------------------------------
    # CALLBACK DE CÁLCULO
    # ---------------------------------------------------
    def on_calcular(self, peso, talla, edad):
        datos = calcular_imc_completo(peso, talla, edad)

        actualizar_resultados(self.panel_resultados, datos)
        actualizar_tarjeta_analisis(self.tarjeta_analisis, datos)
        actualizar_tarjeta_recomendaciones(self.tarjeta_recomendaciones, datos["recomendaciones"])
        actualizar_tarjeta_riesgos(self.tarjeta_riesgos, datos["riesgos"])
        actualizar_grafico(self.panel_graficos, datos)
