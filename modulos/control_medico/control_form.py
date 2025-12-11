import tkinter as tk
from tkinter import ttk

# ============================================================
#   FORMULARIO PRINCIPAL DEL CONTROL MÉDICO
# ============================================================

def construir_formulario(parent):
    """
    Construye el formulario del módulo Control Médico:
    - Síntomas
    - Datos clínicos
    - Signos de alarma

    Retorna un contenedor (sin pack/grid aplicado)
    y un diccionario con referencias a los widgets.
    """

    # ============================================================
    # CONTENEDOR GENERAL (NO usar .pack aquí)
    # ============================================================
    contenedor = tk.Frame(parent, bg="#f4f6f9")

    widgets = {}  # donde guardaremos todas las referencias

    # ============================================================
    # 1) CARD DE SÍNTOMAS
    # ============================================================
    card_sintomas = crear_card(contenedor, width=300, height=330)
    card_sintomas.grid(row=0, column=0, padx=25)

    tk.Label(
        card_sintomas,
        text="Síntomas",
        font=("Segoe UI", 16, "bold"),
        bg="white"
    ).pack(anchor="w", pady=(5, 10))

    sintomas_lista = [
        "Fiebre", "Tos", "Dolor de garganta", "Congestión nasal",
        "Dolor de cabeza", "Dolor corporal", "Náuseas",
        "Dificultad para respirar"
    ]

    sintomas_vars = {}
    frame_chips = tk.Frame(card_sintomas, bg="white")
    frame_chips.pack()

    for sintoma in sintomas_lista:
        var = tk.BooleanVar()
        sintomas_vars[sintoma] = var

        chip = tk.Checkbutton(
            frame_chips,
            text=f" {sintoma} ",
            variable=var,
            font=("Segoe UI", 12),
            bg="white",
            relief="solid",
            borderwidth=1,
            selectcolor="#e7f1ff",
            activebackground="#e7f1ff"
        )
        chip.pack(anchor="w", pady=3)

    widgets["sintomas"] = sintomas_vars

    # ============================================================
    # 2) CARD DE DATOS CLÍNICOS
    # ============================================================
    card_datos = crear_card(contenedor, width=300, height=330)
    card_datos.grid(row=0, column=1, padx=25)

    tk.Label(
        card_datos,
        text="Datos clínicos",
        font=("Segoe UI", 16, "bold"),
        bg="white"
    ).pack(anchor="w", pady=(5, 10))

    form = tk.Frame(card_datos, bg="white")
    form.pack(pady=5)

    # Temperatura
    tk.Label(form, text="Temperatura (°C):", font=("Segoe UI", 13), bg="white")\
        .grid(row=0, column=0, sticky="w", pady=8)
    entry_temp = tk.Entry(form, font=("Segoe UI", 13), width=10)
    entry_temp.grid(row=0, column=1, padx=10)

    # Días con síntomas
    tk.Label(form, text="Días con síntomas:", font=("Segoe UI", 13), bg="white")\
        .grid(row=1, column=0, sticky="w", pady=8)
    entry_dias = tk.Entry(form, font=("Segoe UI", 13), width=10)
    entry_dias.grid(row=1, column=1, padx=10)

    # Tipo de tos
    tk.Label(form, text="Tipo de tos:", font=("Segoe UI", 13), bg="white")\
        .grid(row=2, column=0, sticky="w", pady=8)
    combo_tos = ttk.Combobox(
        form, values=["seca", "con flema"], state="readonly",
        font=("Segoe UI", 12), width=12
    )
    combo_tos.grid(row=2, column=1, padx=10)
    combo_tos.set("seca")

    widgets["temp"] = entry_temp
    widgets["dias"] = entry_dias
    widgets["tos"] = combo_tos

    # ============================================================
    # 3) SIGNOS DE ALARMA
    # ============================================================
    tk.Label(
        card_datos,
        text="Signos de alarma",
        font=("Segoe UI", 14, "bold"),
        fg="#dc3545",
        bg="white"
    ).pack(pady=(15, 5))

    var_pecho = tk.BooleanVar()
    var_conciencia = tk.BooleanVar()

    tk.Checkbutton(card_datos, text="Dolor en el pecho",
                   variable=var_pecho, bg="white",
                   font=("Segoe UI", 12)).pack(anchor="w")

    tk.Checkbutton(card_datos, text="Pérdida de conciencia",
                   variable=var_conciencia, bg="white",
                   font=("Segoe UI", 12)).pack(anchor="w")

    widgets["signos_alarma"] = {
        "pecho": var_pecho,
        "conciencia": var_conciencia
    }

    return contenedor, widgets


# ============================================================
# CARD ESTÉTICA
# ============================================================
def crear_card(parent, width, height):
    frame = tk.Frame(
        parent,
        bg="white",
        relief="solid",
        borderwidth=1,
        padx=20,
        pady=15,
        highlightthickness=1,
        highlightbackground="#e5e5e5"
    )
    frame.config(width=width, height=height)
    frame.pack_propagate(False)
    return frame
