import tkinter as tk
from tkinter import ttk


def construir_formulario(parent, on_calcular_callback):

    # CARD BASE
    frame = tk.Frame(
        parent,
        bg="white",
        padx=15,
        pady=15,
        highlightthickness=1,
        highlightbackground="#D0D0D0"
    )
    frame.pack(fill="both", expand=True, pady=10)

    # -------------------------
    # TÍTULO
    # -------------------------
    lbl_title = tk.Label(
        frame,
        text="Ingresar datos",
        bg="white",
        fg="#0ea5e9",
        font=("Segoe UI", 14, "bold"),
        anchor="w"
    )
    lbl_title.grid(row=0, column=0, columnspan=2, pady=(0, 15), sticky="w")

    # =======================
    # CONFIGURACIÓN DE FUENTES
    # =======================
    label_font = ("Arial", 12)
    entry_font = ("Arial", 12)
    button_font = ("Arial", 13, "bold")

    # -------------------------
    # PESO
    # -------------------------
    lbl_peso = tk.Label(frame, text="Peso (kg):", font=label_font, bg="white")
    lbl_peso.grid(row=1, column=0, sticky="w", pady=6)
    entry_peso = ttk.Entry(frame, width=18, font=entry_font)
    entry_peso.grid(row=1, column=1, pady=6, padx=10, sticky="w")

    # -------------------------
    # TALLA
    # -------------------------
    lbl_talla = tk.Label(frame, text="Talla (m):", font=label_font, bg="white")
    lbl_talla.grid(row=2, column=0, sticky="w", pady=6)
    entry_talla = ttk.Entry(frame, width=18, font=entry_font)
    entry_talla.grid(row=2, column=1, pady=6, padx=10, sticky="w")

    # -------------------------
    # EDAD
    # -------------------------
    lbl_edad = tk.Label(frame, text="Edad:", font=label_font, bg="white")
    lbl_edad.grid(row=3, column=0, sticky="w", pady=6)
    entry_edad = ttk.Entry(frame, width=18, font=entry_font)
    entry_edad.grid(row=3, column=1, pady=6, padx=10, sticky="w")

    # --------------------------------------------
    # LABEL DE ERROR (una sola vez)
    # --------------------------------------------
    error_label = tk.Label(
        frame,
        text="",
        fg="red",
        bg="white",
        font=("Arial", 10, "italic")
    )
    error_label.grid(row=6, column=0, columnspan=2, pady=(5, 0), sticky="w")

    # -------------------------
    # FUNCIÓN CALCULAR
    # -------------------------
    def enviar_datos():
        peso = entry_peso.get().strip()
        talla = entry_talla.get().strip()
        edad = entry_edad.get().strip()

        # Validación de campos vacíos
        if not peso or not talla or not edad:
            error_label.config(text="⚠ Complete todos los campos.")
            return

        try:
            peso = float(peso)
            talla = float(talla)
            edad = int(edad)

            if peso <= 0 or talla <= 0 or edad <= 0:
                raise ValueError()

            # 🚀 SI ESTÁ TODO BIEN → BORRAR EL ERROR
            error_label.config(text="")

            # Ejecutar cálculo
            on_calcular_callback(peso, talla, edad)

        except ValueError:
            error_label.config(text="⚠ Valores inválidos.")

    # -------------------------
    # BOTÓN CALCULAR
    # -------------------------
    btn = ttk.Button(frame, text="Calcular IMC", command=enviar_datos)
    btn.grid(row=5, column=0, columnspan=2, pady=20, ipadx=20, ipady=8)

    style = ttk.Style()
    style.configure(
        "BotonIMC.TButton",
        font=button_font,
        padding=10
    )
    btn.configure(style="BotonIMC.TButton")

    return frame
