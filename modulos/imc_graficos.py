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

    # Crear figura
    fig = Figure(figsize=(5, 2.8), dpi=90)
    ax = fig.add_subplot(111)

    # Configuración inicial
    ax.set_title("IMC")
    ax.set_ylabel("Valor")
    ax.set_ylim(0, 40)

    # Barra inicial
    ax.bar(["IMC"], [0], color="#888")

    # Canvas
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill="both", expand=True)

    frame.fig = fig
    frame.ax = ax
    frame.canvas = canvas

    return frame


# -----------------------------------------------------------
#  ACTUALIZAR GRÁFICO CON LÍNEA Y COLORES CLÍNICOS
# -----------------------------------------------------------
def actualizar_grafico(panel, datos_imc):
    imc = datos_imc["imc"]
    estado = datos_imc["estado"]

    ax = panel.ax
    fig = panel.fig

    # Limpia el gráfico
    ax.clear()

    # -----------------------------------------------------------
    # Colores según estado (paleta Coolors)
    # -----------------------------------------------------------
    color_map = {
        "Bajo peso": "#2D93AD",   # Celeste
        "Normal": "#88AB75",      # Verde suave
        "Sobrepeso": "#F0A202",   # Amarillo
        "Obesidad": "#B32C38"     # Rojo fuerte
    }

    color = color_map.get(estado, "#888")

    # -----------------------------------------------------------
    # DIBUJAR BARRA PRINCIPAL
    # -----------------------------------------------------------
    ax.bar(["IMC"], [imc], color=color)

    # -----------------------------------------------------------
    # LÍNEA VERTICAL QUE MARCA TU IMC EXACTO
    # -----------------------------------------------------------
    ax.axhline(imc, color=color, linestyle="--", linewidth=1.8, alpha=0.8)

    # -----------------------------------------------------------
    # ZONA NORMAL (18.5 – 24.9)
    # -----------------------------------------------------------
    ax.axhspan(18.5, 24.9, color="#88AB75", alpha=0.15)

    # Texto del rango normal
    ax.text(
        0.05, 22,
        "Rango normal (18.5 – 24.9)",
        color="#4a4a4a",
        fontsize=9,
        alpha=0.9
    )

    # -----------------------------------------------------------
    # TÍTULOS Y ESTILO
    # -----------------------------------------------------------
    ax.set_title(f"IMC: {imc:.2f}  ({estado})", fontsize=12, color=color)
    ax.set_ylabel("Valor")
    ax.set_xlabel("")

    # Ajustar límites
    ax.set_ylim(0, max(40, imc + 5))

    # Redibujar
    panel.canvas.draw()
