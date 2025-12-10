import tkinter as tk
from tkinter import ttk

# Matplotlib para gráficos embebidos
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# -----------------------------------------------------------
#  PANEL DE GRÁFICOS
# -----------------------------------------------------------
def construir_panel_graficos(parent):
    frame = ttk.LabelFrame(parent, text="Gráfico del IMC", padding=20)
    frame.pack(fill="both", expand=True, pady=15)

    fig = Figure(figsize=(4, 2.5), dpi=90)
    ax = fig.add_subplot(111)
    ax.set_title("IMC")
    ax.set_xlabel("Categorías")
    ax.set_ylabel("Valor")

    ax.bar(["IMC"], [0], color="#888")

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill="both", expand=True)

    frame.fig = fig
    frame.ax = ax
    frame.canvas = canvas

    return frame


# -----------------------------------------------------------
#  ACTUALIZAR GRÁFICO
# -----------------------------------------------------------
def actualizar_grafico(panel, datos_imc):
    imc = datos_imc["imc"]
    estado = datos_imc["estado"]        # <--- CORREGIDO

    ax = panel.ax
    fig = panel.fig

    ax.clear()

    ax.bar(["IMC"], [imc], color="#4a90e2")

    ax.set_title(f"IMC: {imc:.2f}  ({estado})")   # <--- CORREGIDO
    ax.set_ylim(0, max(40, imc + 5))
    ax.set_ylabel("Valor")

    panel.canvas.draw()
