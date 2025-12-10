import tkinter as tk
from tkinter import ttk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time


# -----------------------------------------------------------
#  PANEL DE GRÁFICOS (DOS COLUMNAS)
# -----------------------------------------------------------
def construir_panel_graficos_duales(parent):
    frame = ttk.Frame(parent)
    frame.pack(fill="both", expand=True, pady=20, padx=20)

    # ---------- Figura izquierda ----------
    fig1 = Figure(figsize=(4.5, 2.5), dpi=100)
    ax1 = fig1.add_subplot(111)
    ax1.set_title("IMC")
    ax1.set_ylim(0, 40)

    canvas1 = FigureCanvasTkAgg(fig1, master=frame)
    canvas1.get_tk_widget().pack(side="left", fill="both", expand=True, padx=10)

    # ---------- Figura derecha ----------
    fig2 = Figure(figsize=(4.5, 2.5), dpi=100)
    ax2 = fig2.add_subplot(111)
    ax2.set_title("IMC actual vs ideal")
    ax2.set_ylim(0, 40)

    canvas2 = FigureCanvasTkAgg(fig2, master=frame)
    canvas2.get_tk_widget().pack(side="left", fill="both", expand=True, padx=10)

    # Guardar referencias
    frame.fig1 = fig1
    frame.ax1 = ax1
    frame.canvas1 = canvas1

    frame.fig2 = fig2
    frame.ax2 = ax2
    frame.canvas2 = canvas2

    return frame


# -----------------------------------------------------------
#  COLORES CLÍNICOS EN TONOS SUAVES
# -----------------------------------------------------------
color_map = {
    "Bajo peso":     {"strong": "#2D93AD", "soft": "#CFE8F3"},
    "Normal":        {"strong": "#88AB75", "soft": "#E4F1D5"},
    "Sobrepeso":     {"strong": "#F0A202", "soft": "#FCE8C9"},
    "Obesidad":      {"strong": "#B32C38", "soft": "#F7D4D8"},
}


# -----------------------------------------------------------
#  ANIMACIÓN SUAVE PARA GRÁFICOS
# -----------------------------------------------------------
def animar_barra(ax, canvas, valor_final, color):
    pasos = 30          # número de frames
    valor_actual = 0
    incremento = valor_final / pasos

    for _ in range(pasos):
        valor_actual += incremento
        ax.clear()
        ax.bar(["IMC"], [valor_actual], color=color)
        canvas.draw()
        canvas.get_tk_widget().update()
        time.sleep(0.015)   # velocidad suave


# -----------------------------------------------------------
#  GRÁFICO A: IMC (IZQUIERDA)
# -----------------------------------------------------------
def actualizar_grafico_principal(panel, datos):

    imc = datos["imc"]
    estado = datos["estado"]

    ax = panel.ax1
    fig = panel.fig1
    canvas = panel.canvas1

    colores = color_map.get(estado, color_map["Normal"])
    strong = colores["strong"]
    soft = colores["soft"]

    ax.clear()
    ax.set_ylim(0, max(40, imc + 5))
    ax.set_title(f"IMC: {imc:.2f} ({estado})", fontsize=12, color=strong)

    # Fondo rango normal
    ax.axhspan(18.5, 24.9, color="#E4F1D5", alpha=0.35)

    # Línea del rango
    ax.text(0.05, 22, "Rango normal (18.5–24.9)", fontsize=9, color="#555")

    # Animación de la barra
    animar_barra(ax, canvas, imc, strong)


# -----------------------------------------------------------
#  GRÁFICO B: COMPARATIVO (DERECHA)
# -----------------------------------------------------------
def actualizar_grafico_comparativo(panel, datos):

    imc_actual = datos["imc"]
    ideal_min = datos["peso_min"]
    ideal_max = datos["peso_max"]

    # Convertir rango ideal a IMC (fórmula del IMC)
    talla = datos["talla_m"]
    imc_ideal_min = ideal_min / (talla ** 2)
    imc_ideal_max = ideal_max / (talla ** 2)
    imc_ideal = (imc_ideal_min + imc_ideal_max) / 2  # Promedio → válido para comparación visual

    ax = panel.ax2
    canvas = panel.canvas2

    ax.clear()
    ax.set_ylim(0, max(40, imc_actual + 5))
    ax.set_title("IMC actual vs ideal", fontsize=12)

    # Barras comparativas
    categorias = ["Actual", "Ideal"]
    valores = [imc_actual, imc_ideal]
    colores = ["#6BAED6", "#9ECAE1"]   # tonos suaves azulados

    # Animación progresiva
    max_val = max(valores)
    pasos = 30

    for i in range(pasos + 1):
        ax.clear()
        ax.set_ylim(0, max(40, max_val + 5))
        ax.bar(categorias, [val * (i / pasos) for val in valores], color=colores)
        canvas.draw()
        canvas.get_tk_widget().update()
        time.sleep(0.015)
