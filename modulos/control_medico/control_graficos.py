import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ============================================================
# PANEL PROFESIONAL DE GRÁFICAS CLÍNICAS (VERSIÓN VERTICAL)
# ============================================================

def construir_panel_graficos(parent):
    """
    Construye un panel con dos gráficos colocados en vertical:
    [ Gráfico 1 ]
    [ Gráfico 2 ]
    Usamos EXCLUSIVAMENTE grid() para evitar errores.
    """

    # CARD GENERAL (sin pack → el padre usará grid para colocarlo)
    card = tk.Frame(
        parent,
        bg="white",
        relief="solid",
        borderwidth=1,
        padx=25,
        pady=20,
        highlightthickness=1,
        highlightbackground="#e5e5e5"
    )

    # Título del panel
    titulo = tk.Label(
        card,
        text="Indicadores Clínicos",
        font=("Segoe UI", 18, "bold"),
        bg="white",
        fg="#1c1c1c"
    )
    titulo.grid(row=0, column=0, sticky="w", pady=(0, 15))

    # CONTENEDOR VERTICAL PARA GRÁFICOS
    contenedor = tk.Frame(card, bg="white")
    contenedor.grid(row=1, column=0)

    refs = {}

    # ============================================================
    # GRÁFICO 1 — TEMPERATURA
    # ============================================================
    fig1 = Figure(figsize=(5.5, 2.6), dpi=100)
    ax1 = fig1.add_subplot(111)
    ax1.set_title("Evolución de la temperatura corporal (°C)", fontsize=12)
    ax1.set_ylim(35, 41)
    ax1.set_ylabel("°C")
    ax1.grid(alpha=0.3)

    canvas1 = FigureCanvasTkAgg(fig1, master=contenedor)
    canvas1_widget = canvas1.get_tk_widget()
    canvas1_widget.grid(row=0, column=0, pady=10)

    refs["ax_temp"] = ax1
    refs["canvas_temp"] = canvas1

    # ============================================================
    # GRÁFICO 2 — SEVERIDAD DE SÍNTOMAS
    # ============================================================
    fig2 = Figure(figsize=(5.5, 2.6), dpi=100)
    ax2 = fig2.add_subplot(111)
    ax2.set_title("Severidad de los síntomas reportados", fontsize=12)
    ax2.set_ylim(0, 10)
    ax2.set_ylabel("Intensidad")
    ax2.grid(alpha=0.3)

    canvas2 = FigureCanvasTkAgg(fig2, master=contenedor)
    canvas2_widget = canvas2.get_tk_widget()
    canvas2_widget.grid(row=1, column=0, pady=10)

    refs["ax_sintomas"] = ax2
    refs["canvas_sintomas"] = canvas2

    return card, refs


# ============================================================
# FUNCIÓN PARA ACTUALIZAR GRÁFICOS
# ============================================================

def actualizar_graficos(refs, datos_temp, datos_sintomas):

    # --- TEMP ---
    ax1 = refs["ax_temp"]
    ax1.clear()
    ax1.set_title("Evolución de la temperatura corporal (°C)", fontsize=12)
    ax1.set_ylim(35, 41)
    ax1.set_ylabel("°C")
    ax1.plot(datos_temp, marker="o", color="#0d6efd")
    ax1.grid(alpha=0.3)
    refs["canvas_temp"].draw()

    # --- SÍNTOMAS ---
    ax2 = refs["ax_sintomas"]
    ax2.clear()
    ax2.set_title("Severidad de los síntomas reportados", fontsize=12)
    ax2.set_ylim(0, 10)
    ax2.set_ylabel("Intensidad")
    ax2.bar(["Actual"], [datos_sintomas], color="#dc3545")
    ax2.grid(alpha=0.3)
    refs["canvas_sintomas"].draw()
