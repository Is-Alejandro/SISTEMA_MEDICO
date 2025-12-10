import tkinter as tk
from tkinter import ttk


def construir_formulario(parent, on_calcular_callback):
    frame = ttk.LabelFrame(parent, text="Ingresar datos", padding=20)
    frame.pack(fill="x", pady=10)

    # =======================
    # CONFIGURACIÓN DE FUENTES
    # =======================
    label_font = ("Arial", 13)
    entry_font = ("Arial", 12)
    button_font = ("Arial", 13, "bold")

    # -------------------------
    # PESO
    # -------------------------
    lbl_peso = ttk.Label(frame, text="Peso (kg):", font=label_font)
    lbl_peso.grid(row=0, column=0, sticky="w", pady=8)

    entry_peso = ttk.Entry(frame, width=18, font=entry_font)
    entry_peso.grid(row=0, column=1, pady=8, padx=10)

    # -------------------------
    # TALLA
    # -------------------------
    lbl_talla = ttk.Label(frame, text="Talla (m):", font=label_font)
    lbl_talla.grid(row=1, column=0, sticky="w", pady=8)

    entry_talla = ttk.Entry(frame, width=18, font=entry_font)
    entry_talla.grid(row=1, column=1, pady=8, padx=10)

    # -------------------------
    # EDAD
    # -------------------------
    lbl_edad = ttk.Label(frame, text="Edad:", font=label_font)
    lbl_edad.grid(row=2, column=0, sticky="w", pady=8)

    entry_edad = ttk.Entry(frame, width=18, font=entry_font)
    entry_edad.grid(row=2, column=1, pady=8, padx=10)

    # -------------------------
    # FUNCIÓN CALCULAR
    # -------------------------
    def enviar_datos():
        peso = entry_peso.get().strip()
        talla = entry_talla.get().strip()
        edad = entry_edad.get().strip()

        if not peso or not talla or not edad:
            ttk.Label(frame, text="⚠️ Complete todos los campos.", foreground="red").grid(
                row=4, column=0, columnspan=2, pady=5
            )
            return

        try:
            peso = float(peso)
            talla = float(talla)
            edad = int(edad)

            if peso <= 0 or talla <= 0 or edad <= 0:
                raise ValueError()

            on_calcular_callback(peso, talla, edad)

        except ValueError:
            ttk.Label(frame, text="⚠️ Valores inválidos.", foreground="red").grid(
                row=4, column=0, columnspan=2, pady=5
            )

    # -------------------------
    # BOTÓN CALCULAR (MEJORADO)
    # -------------------------
    btn = ttk.Button(frame, text="Calcular IMC", command=enviar_datos)
    btn.grid(row=3, column=0, columnspan=2, pady=20, ipadx=20, ipady=8)

    # Cambiamos la fuente manualmente (ttk no acepta font directo)
    btn.configure(style="BotonIMC.TButton")

    style = ttk.Style()
    style.configure(
        "BotonIMC.TButton",
        font=button_font,
        padding=10
    )

    return frame
