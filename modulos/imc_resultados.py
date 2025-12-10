import tkinter as tk
from tkinter import ttk


# -----------------------------------------------------------
#  CONSTRUIR PANEL DE RESULTADOS (VACÍO INICIALMENTE)
# -----------------------------------------------------------
def construir_panel_resultados(parent):
    frame = ttk.LabelFrame(parent, text="Resultados del IMC", padding=20)
    frame.pack(fill="x", pady=15)

    lbl_imc = ttk.Label(frame, text="IMC: --", font=("Arial", 14, "bold"))
    lbl_imc.pack(anchor="w", pady=5)

    lbl_estado = ttk.Label(frame, text="Estado: --", font=("Arial", 12))
    lbl_estado.pack(anchor="w", pady=5)

    canvas = tk.Canvas(frame, height=28, width=400, bg="#f5f5f5", bd=0, highlightthickness=0)
    canvas.pack(pady=15, fill="x")

    frame.lbl_imc = lbl_imc
    frame.lbl_estado = lbl_estado
    frame.canvas = canvas

    return frame


# -----------------------------------------------------------
#  ACTUALIZAR PANEL DE RESULTADOS
# -----------------------------------------------------------
def actualizar_resultados(panel, datos_imc):

    imc = datos_imc["imc"]
    estado = datos_imc["estado"]       # <-- CAMBIO IMPORTANTE
    color = datos_imc["color"]         # <-- SE USA PARA LA BARRA

    # -------------------------
    # Actualizar textos
    # -------------------------
    panel.lbl_imc.config(text=f"IMC: {imc:.2f}")
    panel.lbl_estado.config(text=f"Estado: {estado}")

    # -------------------------
    # Actualizar barra visual
    # -------------------------
    canvas = panel.canvas
    canvas.delete("all")

    # Fondo gris
    canvas.create_rectangle(0, 0, 400, 25, fill="#dddddd", outline="")

    # Elegir color según estado
    color_map = {
        "Bajo peso": "#4aa3df",
        "Normal": "#52c24a",
        "Sobrepeso": "#e6b800",
        "Obesidad": "#d9534f"
    }

    barra_color = color_map.get(estado, "#888")

    # Proporción IMC → 0–40
    x = min(max((imc / 40) * 400, 0), 400)

    # Rectángulo indicador
    canvas.create_rectangle(0, 0, x, 25, fill=barra_color, outline="")

    # Texto del valor
    canvas.create_text(
        x - 5 if x > 30 else x + 25,
        13,
        text=f"{imc:.1f}",
        fill="black",
        font=("Arial", 10, "bold"),
        anchor="e"
    )
