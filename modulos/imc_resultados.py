import tkinter as tk
from tkinter import ttk


# ============================================================
#  PALETA DE COLORES MÉDICA (Coolors adaptado)
# ============================================================
COLOR_BAJO_PESO   = "#2D93AD"   # Celeste clínico
COLOR_NORMAL      = "#88AB75"   # Verde clínico
COLOR_SOBREPESO   = "#F0A202"   # Amarillo advertencia
COLOR_OBESIDAD    = "#B32C38"   # Rojo alerta

COLOR_BARRA_FONDO = "#D9D9D9"   # Gris claro
COLOR_TEXTO       = "#202C59"   # Azul profundo profesional


# Mapa de colores por estado
COLOR_MAP = {
    "Bajo peso": COLOR_BAJO_PESO,
    "Normal": COLOR_NORMAL,
    "Sobrepeso": COLOR_SOBREPESO,
    "Obesidad": COLOR_OBESIDAD,
}


# ============================================================
#  CONSTRUIR PANEL DE RESULTADOS
# ============================================================
def construir_panel_resultados(parent):
    
    # Creamos un frame limpio sin LabelFrame
    frame = tk.Frame(parent, bg=parent.cget("bg"))
    frame.pack(fill="x", pady=10)

    # Título IMC
    lbl_titulo = ttk.Label(
        frame,
        text="Resultados del IMC",
        font=("Segoe UI", 16, "bold"),
        foreground=COLOR_TEXTO,
        background=parent.cget("bg"),
    )
    lbl_titulo.pack(anchor="w", pady=(0, 5))

    # IMC
    lbl_imc = ttk.Label(
        frame,
        text="IMC: --",
        font=("Segoe UI", 14, "bold"),
        foreground=COLOR_TEXTO,
        background=parent.cget("bg"),
    )
    lbl_imc.pack(anchor="w", pady=3)

    # Estado clínico
    lbl_estado = ttk.Label(
        frame,
        text="Estado: --",
        font=("Segoe UI", 12),
        foreground=COLOR_TEXTO,
        background=parent.cget("bg"),
    )
    lbl_estado.pack(anchor="w", pady=3)

    # Barra IMC moderna
    canvas = tk.Canvas(
        frame,
        height=32,
        bg=parent.cget("bg"),
        highlightthickness=0,
        bd=0
    )
    canvas.pack(fill="x", pady=12)

    frame.lbl_titulo = lbl_titulo
    frame.lbl_imc = lbl_imc
    frame.lbl_estado = lbl_estado
    frame.canvas = canvas

    return frame


# ============================================================
#  ACTUALIZAR PANEL DE RESULTADOS
# ============================================================
def actualizar_resultados(panel, datos):

    imc = datos["imc"]
    estado = datos["estado"]

    # ----------------------------------
    # Actualizar etiquetas
    # ----------------------------------
    panel.lbl_imc.config(text=f"IMC: {imc:.2f}")
    panel.lbl_estado.config(text=f"Estado: {estado}")

    # ----------------------------------
    # Determinar color clínico
    # ----------------------------------
    color = COLOR_MAP.get(estado, "#888")

    # ----------------------------------
    # Redibujar nueva barra IMC moderna
    # ----------------------------------
    canvas = panel.canvas
    canvas.delete("all")

    width = canvas.winfo_width() or 400
    height = 28
    radius = 14  # bordes redondeados

    # Fondo gris con bordes redondeados
    _rounded_rect(canvas, 0, 0, width, height, radius, fill=COLOR_BARRA_FONDO)

    # Largo según IMC (máx 40)
    porcentaje = min(max(imc / 40, 0), 1)
    barra_width = width * porcentaje

    # Barra coloreada con bordes redondeados
    _rounded_rect(canvas, 0, 0, barra_width, height, radius, fill=color)

    # ----------------------------------
    # Etiqueta IMC (valor flotante)
    # ----------------------------------
    x_value = min(barra_width - 10, width - 40)
    if x_value < 40:
        x_value = 40

    canvas.create_text(
        x_value,
        height / 2,
        text=f"{imc:.1f}",
        fill="white" if porcentaje > 0.15 else "#202C59",
        font=("Segoe UI", 12, "bold")
    )


# ============================================================
#  FUNCIONES DE DIBUJO (Bordes redondeados)
# ============================================================
def _rounded_rect(canvas, x1, y1, x2, y2, r, **kwargs):
    """
    Dibuja un rectángulo redondeado en un canvas.
    """
    points = [
        x1+r, y1,
        x2-r, y1,
        x2,   y1,
        x2,   y1+r,
        x2,   y2-r,
        x2,   y2,
        x2-r, y2,
        x1+r, y2,
        x1,   y2,
        x1,   y2-r,
        x1,   y1+r,
        x1,   y1,
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)
