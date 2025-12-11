import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ============================================================
# GRÁFICOS DEL CONTROL MÉDICO
# ============================================================

def construir_panel_graficos(parent):
    """
    Construye un panel de dos gráficos profesionales:
    - Evolución de temperatura
    - Severidad de síntomas

    Retorna:
    - frame contenedor
    - diccionario con referencias a ejes y canvas
    """

    contenedor = tk.Frame(parent, bg="#f4f6f9")
    contenedor.pack(pady=25)

    refs = {}

    # ============================================================
    # GRÁFICO 1: EVOLUCIÓN DE TEMPERATURA
    # ============================================================
    fig1 = Figure(figsize=(4.5, 2.4), dpi=100)
    ax1 = fig1.add_subplot(111)
    ax1.set_title("Evolución de temperatura", fontsize=12)
    ax1.set_ylim(35, 41)
    ax1.grid(alpha=0.3)

    canvas1 = FigureCanvasTkAgg(fig1, master=contenedor)
    canvas1.get_tk_widget().pack(side="left", padx=20)

    refs["ax_temp"] = ax1
    refs["canvas_temp"] = canvas1

    # ============================================================
    # GRÁFICO 2: SEVERIDAD DE SÍNTOMAS (BARRAS)
    # ============================================================
    fig2 = Figure(figsize=(4.5, 2.4), dpi=100)
    ax2 = fig2.add_subplot(111)
    ax2.set_title("Severidad de síntomas", fontsize=12)
    ax2.set_ylim(0, 10)
    ax2.grid(alpha=0.3)

    canvas2 = FigureCanvasTkAgg(fig2, master=contenedor)
    canvas2.get_tk_widget().pack(side="left", padx=20)

    refs["ax_sintomas"] = ax2
    refs["canvas_sintomas"] = canvas2

    return contenedor, refs


# ============================================================
# FUNCIÓN PARA ACTUALIZAR GRÁFICOS
# ============================================================
def actualizar_graficos(refs, datos_temp, datos_sintomas):
    """
    Actualiza los gráficos del módulo:
    
    - datos_temp: lista de temperaturas registradas
    - datos_sintomas: número de síntomas seleccionados

    Permite en el futuro graficar tendencias reales.
    """

    # --- Gráfico de temperatura ---
    refs["ax_temp"].clear()
    refs["ax_temp"].set_title("Evolución de temperatura", fontsize=12)
    refs["ax_temp"].set_ylim(35, 41)
    refs["ax_temp"].plot(datos_temp, marker="o", color="#0d6efd")
    refs["ax_temp"].grid(alpha=0.3)
    refs["canvas_temp"].draw()

    # --- Gráfico de severidad ---
    refs["ax_sintomas"].clear()
    refs["ax_sintomas"].set_title("Severidad de síntomas", fontsize=12)
    refs["ax_sintomas"].set_ylim(0, 10)
    refs["ax_sintomas"].bar(["Actual"], [datos_sintomas], color="#dc3545")
    refs["ax_sintomas"].grid(alpha=0.3)
    refs["canvas_sintomas"].draw()
