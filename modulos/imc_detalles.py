import tkinter as tk
from tkinter import ttk


# -------------------------------------------------------
# TARJETA GENERAL CON ESTILO MODERNO
# -------------------------------------------------------
def _crear_tarjeta(parent, titulo, bg_color):
    frame = tk.Frame(parent, bg=bg_color, padx=15, pady=15)
    frame.pack(fill="x", pady=10)

    lbl_title = tk.Label(
        frame,
        text=titulo,
        bg=bg_color,
        fg="#222",
        font=("Arial", 14, "bold")
    )
    lbl_title.pack(anchor="w", pady=(0, 10))

    return frame


# -------------------------------------------------------
# TARJETA: ANÁLISIS CLÍNICO (peso ideal, kcal, % ideal)
# -------------------------------------------------------
def crear_tarjeta_analisis(parent):
    frame = _crear_tarjeta(parent, "Análisis clínico", "#f0f4ff")  # azul muy suave

    frame.lbl_peso = tk.Label(frame, text="", bg="#f0f4ff", font=("Arial", 12))
    frame.lbl_peso.pack(anchor="w", pady=3)

    frame.lbl_pct = tk.Label(frame, text="", bg="#f0f4ff", font=("Arial", 12))
    frame.lbl_pct.pack(anchor="w", pady=3)

    frame.lbl_kcal = tk.Label(frame, text="", bg="#f0f4ff", font=("Arial", 12))
    frame.lbl_kcal.pack(anchor="w", pady=3)

    return frame


def actualizar_tarjeta_analisis(frame, datos):
    frame.lbl_peso.config(
        text=f"Peso recomendado: {datos['peso_min']} kg – {datos['peso_max']} kg"
    )
    frame.lbl_pct.config(
        text=f"Porcentaje respecto al ideal: {datos['pct_ideal']}%"
    )
    frame.lbl_kcal.config(
        text=f"Calorías recomendadas: {datos['kcal']} kcal"
    )


# -------------------------------------------------------
# TARJETA RECOMENDACIONES (verde suave)
# -------------------------------------------------------
def crear_tarjeta_recomendaciones(parent):
    frame = _crear_tarjeta(parent, "Recomendaciones", "#eaf7ea")  # verde suave
    frame.contenido = tk.Frame(frame, bg="#eaf7ea")
    frame.contenido.pack(anchor="w")
    return frame


def actualizar_tarjeta_recomendaciones(frame, lista):
    for w in frame.contenido.winfo_children():
        w.destroy()

    for r in lista:
        tk.Label(
            frame.contenido,
            text=f"• {r}",
            bg="#eaf7ea",
            fg="#222",
            font=("Arial", 11)
        ).pack(anchor="w")


# -------------------------------------------------------
# TARJETA RIESGOS (rojo suave)
# -------------------------------------------------------
def crear_tarjeta_riesgos(parent):
    frame = _crear_tarjeta(parent, "Riesgos clínicos", "#ffecec")  # rojo suave
    frame.contenido = tk.Frame(frame, bg="#ffecec")
    frame.contenido.pack(anchor="w")
    return frame


def actualizar_tarjeta_riesgos(frame, lista):
    for w in frame.contenido.winfo_children():
        w.destroy()

    if not lista:
        tk.Label(
            frame.contenido,
            text="No presenta riesgos clínicos.",
            bg="#ffecec",
            fg="#444",
            font=("Arial", 11, "italic")
        ).pack(anchor="w")
        return

    for r in lista:
        tk.Label(
            frame.contenido,
            text=f"• {r}",
            bg="#ffecec",
            fg="#b30000",
            font=("Arial", 11, "bold")
        ).pack(anchor="w")
