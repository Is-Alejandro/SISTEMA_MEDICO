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
    # CONTENEDOR GENERAL
    # ============================================================
    contenedor = tk.Frame(parent, bg="#f4f6f9")
    widgets = {}

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

    # --- Estilo moderno tipo chip ---
    for sintoma in sintomas_lista:
        var = tk.BooleanVar()
        sintomas_vars[sintoma] = var

        chip = tk.Checkbutton(
            frame_chips,
            text=sintoma,
            variable=var,
            font=("Segoe UI", 12),
            bg="white",
            fg="#333",
            activebackground="white",
            selectcolor="white",
            anchor="w",
            padx=4,
            pady=2
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
    form.pack(pady=5, fill="x")

    # 🔹 Usamos un ancho estándar profesional para inputs
    input_width = 14

    # --- Temperatura ---
    tk.Label(
        form,
        text="Temperatura (°C):",
        font=("Segoe UI", 13),
        bg="white"
    ).grid(row=0, column=0, sticky="w", pady=6)

    entry_temp = tk.Entry(
        form,
        font=("Segoe UI", 13),
        width=input_width,
        relief="solid",
        borderwidth=1
    )
    entry_temp.grid(row=0, column=1, padx=10, pady=6, sticky="w")

    # --- Días con síntomas ---
    tk.Label(
        form,
        text="Días con síntomas:",
        font=("Segoe UI", 13),
        bg="white"
    ).grid(row=1, column=0, sticky="w", pady=6)

    entry_dias = tk.Entry(
        form,
        font=("Segoe UI", 13),
        width=input_width,
        relief="solid",
        borderwidth=1
    )
    entry_dias.grid(row=1, column=1, padx=10, pady=6, sticky="w")

    # --- Tipo de tos ---
    tk.Label(
        form,
        text="Tipo de tos:",
        font=("Segoe UI", 13),
        bg="white"
    ).grid(row=2, column=0, sticky="w", pady=6)

    combo_tos = ttk.Combobox(
        form,
        values=["seca", "con flema"],
        state="readonly",
        font=("Segoe UI", 12),
        width=input_width
    )
    combo_tos.grid(row=2, column=1, padx=10, pady=6, sticky="w")
    combo_tos.set("seca")
    combo_tos.configure(foreground="#333")

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
    ).pack(anchor="w", pady=(15, 5))

    var_pecho = tk.BooleanVar()
    var_conciencia = tk.BooleanVar()

    tk.Checkbutton(
        card_datos,
        text="Dolor en el pecho",
        variable=var_pecho,
        bg="white",
        font=("Segoe UI", 12),
        anchor="w",
        pady=2
    ).pack(anchor="w")

    tk.Checkbutton(
        card_datos,
        text="Pérdida de conciencia",
        variable=var_conciencia,
        bg="white",
        font=("Segoe UI", 12),
        anchor="w",
        pady=2
    ).pack(anchor="w")

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

    # --- ALTURA AUTOMÁTICA (FIX) ---
    frame.config(width=width)
    frame.pack_propagate(True)

    return frame
