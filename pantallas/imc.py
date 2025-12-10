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
        # DIVIDIR EN 3 COLUMNAS (izquierda / centro / derecha)
        # ---------------------------------------------------
        col_izq, col_centro, col_der = crear_columnas(
            contenedor,
            num_columnas=3,
            separacion=40
        )

        # ---------------------------------------------------
        # COLUMNA IZQUIERDA → FORMULARIO
        # ---------------------------------------------------
        construir_formulario(col_izq, self.on_calcular)

        # ---------------------------------------------------
        # COLUMNA CENTRAL → CARD con RESULTADOS + BARRA IMC
        # ---------------------------------------------------
        card_centro = tk.Frame(
            col_centro,
            bg="white",
            highlightthickness=1,
            highlightbackground="#D0D0D0",
            padx=15,
            pady=15
        )
        card_centro.pack(fill="both", expand=True)

        # Sombra (opcional)
        sombra = tk.Frame(col_centro, bg="#E5E5E5")
        sombra.place(relx=0, rely=0, relwidth=1, relheight=1)
        card_centro.lift()

        # PANEL RESULTADOS (dentro del CARD)
        self.panel_resultados = construir_panel_resultados(card_centro)

        # ---------------------------------------------------
        # COLUMNA DERECHA → 3 CARDS HORIZONTALES
        # ---------------------------------------------------
        contenedor_cards = ttk.Frame(col_der)
        contenedor_cards.pack(fill="x", pady=10)

        # Crear 3 columnas internas para las cards
        col_a = ttk.Frame(contenedor_cards)
        col_b = ttk.Frame(contenedor_cards)
        col_c = ttk.Frame(contenedor_cards)

        col_a.pack(side="left", expand=True, fill="both", padx=5)
        col_b.pack(side="left", expand=True, fill="both", padx=5)
        col_c.pack(side="left", expand=True, fill="both", padx=5)

        # Función genérica para crear cards visuales
        def crear_card(parent, titulo):
            card = tk.Frame(
                parent,
                bg="white",
                highlightthickness=1,
                highlightbackground="#D0D0D0",
                padx=12,
                pady=12
            )
            card.pack(fill="both", expand=True)

            lbl = ttk.Label(
                card,
                text=titulo,
                font=("Segoe UI", 14, "bold"),
                foreground="#0ea5e9",
                background="white"
            )
            lbl.pack(anchor="w", pady=(0, 8))

            return card

        # CARD 1: ANÁLISIS CLÍNICO
        card_analisis = crear_card(col_a, "Análisis clínico")
        self.tarjeta_analisis = crear_tarjeta_analisis(card_analisis)

        # CARD 2: RECOMENDACIONES
        card_recomendaciones = crear_card(col_b, "Recomendaciones")
        self.tarjeta_recomendaciones = crear_tarjeta_recomendaciones(card_recomendaciones)

        # CARD 3: RIESGOS CLÍNICOS
        card_riesgos = crear_card(col_c, "Riesgos clínicos")
        self.tarjeta_riesgos = crear_tarjeta_riesgos(card_riesgos)

        # ---------------------------------------------------
        # GRÁFICO IMC (DEBAJO DE TODO)
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
