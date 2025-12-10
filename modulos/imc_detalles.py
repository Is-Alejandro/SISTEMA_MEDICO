import tkinter as tk
from tkinter import ttk

# -------------------------------------------------------
# TARJETA GENERAL UNIFICADA
# -------------------------------------------------------
def _crear_tarjeta(parent, titulo, bg_color):
    frame = tk.Frame(parent, bg=bg_color, padx=15, pady=15)
    frame.pack(fill="both", expand=True, pady=10)

    lbl_title = tk.Label(
        frame,
        text=titulo,
        bg=bg_color,
        fg="#222",
        font=("Arial", 14, "bold"),
        anchor="w"
    )
    lbl_title.pack(anchor="w", pady=(0, 10))

    # 🔹 TODAS LAS CARDS TENDRÁN body
    frame.body = tk.Frame(frame, bg=bg_color)
    frame.body.pack(fill="both", expand=True)

    return frame


# -------------------------------------------------------
# TARJETA: ANÁLISIS CLÍNICO
# -------------------------------------------------------
def crear_tarjeta_analisis(parent):
    frame = _crear_tarjeta(parent, "Análisis clínico", "#f0f4ff")

    frame.lbl_peso = tk.Label(frame.body, text="", bg="#f0f4ff", font=("Arial", 12),
                              wraplength=250, justify="left", anchor="w")
    frame.lbl_peso.pack(anchor="w", pady=3)

    frame.lbl_pct = tk.Label(frame.body, text="", bg="#f0f4ff", font=("Arial", 12),
                             wraplength=250, justify="left", anchor="w")
    frame.lbl_pct.pack(anchor="w", pady=3)

    frame.lbl_kcal = tk.Label(frame.body, text="", bg="#f0f4ff", font=("Arial", 12),
                              wraplength=250, justify="left", anchor="w")
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
# TARJETA: RECOMENDACIONES
# -------------------------------------------------------
def crear_tarjeta_recomendaciones(parent):
    frame = _crear_tarjeta(parent, "Recomendaciones", "#eaf7ea")
    return frame


def actualizar_tarjeta_recomendaciones(frame, lista):
    # Limpiar contenido
    for w in frame.body.winfo_children():
        w.destroy()

    # Crear nuevas etiquetas
    for r in lista:
        tk.Label(
            frame.body,
            text=f"• {r}",
            bg="#eaf7ea",
            fg="#222",
            font=("Arial", 11),
            wraplength=250,
            justify="left",
            anchor="w"
        ).pack(anchor="w", pady=2)


# -------------------------------------------------------
# TARJETA: RIESGOS
# -------------------------------------------------------
def crear_tarjeta_riesgos(parent):
    frame = _crear_tarjeta(parent, "Riesgos clínicos", "#ffecec")
    return frame


def actualizar_tarjeta_riesgos(frame, lista):
    for w in frame.body.winfo_children():
        w.destroy()

    if not lista:
        tk.Label(
            frame.body,
            text="No presenta riesgos clínicos.",
            bg="#ffecec",
            fg="#444",
            font=("Arial", 11, "italic"),
            wraplength=250,
            justify="left",
            anchor="w"
        ).pack(anchor="w", pady=2)
        return

    for r in lista:
        tk.Label(
            frame.body,
            text=f"• {r}",
            bg="#ffecec",
            fg="#b30000",
            font=("Arial", 11, "bold"),
            wraplength=250,
            justify="left",
            anchor="w"
        ).pack(anchor="w", pady=2)
