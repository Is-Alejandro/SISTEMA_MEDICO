import tkinter as tk
from tkinter import ttk


def construir_formulario(parent, on_calcular_callback):
    frame = ttk.LabelFrame(parent, text="Ingresar datos", padding=20)
    frame.pack(fill="x", pady=10)

    # -------------------------
    # PESO
    # -------------------------
    lbl_peso = ttk.Label(frame, text="Peso (kg):")
    lbl_peso.grid(row=0, column=0, sticky="w", pady=5)

    entry_peso = ttk.Entry(frame, width=10)
    entry_peso.grid(row=0, column=1, pady=5, padx=10)

    # -------------------------
    # TALLA
    # -------------------------
    lbl_talla = ttk.Label(frame, text="Talla (m):")
    lbl_talla.grid(row=1, column=0, sticky="w", pady=5)

    entry_talla = ttk.Entry(frame, width=10)
    entry_talla.grid(row=1, column=1, pady=5, padx=10)

    # -------------------------
    # EDAD
    # -------------------------
    lbl_edad = ttk.Label(frame, text="Edad:")
    lbl_edad.grid(row=2, column=0, sticky="w", pady=5)

    entry_edad = ttk.Entry(frame, width=10)
    entry_edad.grid(row=2, column=1, pady=5, padx=10)

    # -------------------------
    # BOTÓN CALCULAR
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

            # 🔥 Ahora enviamos los 3 valores
            on_calcular_callback(peso, talla, edad)

        except ValueError:
            ttk.Label(frame, text="⚠️ Valores inválidos.", foreground="red").grid(
                row=4, column=0, columnspan=2, pady=5
            )

    btn = ttk.Button(frame, text="Calcular IMC", command=enviar_datos)
    btn.grid(row=3, column=0, columnspan=2, pady=15)

    return frame
