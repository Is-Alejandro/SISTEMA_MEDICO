import tkinter as tk
from tkinter import ttk

def construir_formulario_diabetes(parent):
    """
    Construye un formulario moderno para evaluación de diabetes,
    utilizando listas desplegables (Combobox) y mejor organización visual.
    """

    contenedor = tk.Frame(parent, bg="white")
    contenedor.pack(fill="both", expand=True, pady=10)

    # ================================
    #   TÍTULO
    # ================================
    titulo = tk.Label(
        contenedor,
        text="Evaluación de Diabetes",
        font=("Segoe UI", 18, "bold"),
        bg="white",
        fg="#333"
    )
    titulo.pack(pady=(0, 20))

    # ================================
    #   CUERPO DEL FORMULARIO
    # ================================
    cuerpo = tk.Frame(contenedor, bg="white")
    cuerpo.pack()

    # ============================================
    #   LISTAS DE OPCIONES
    # ============================================

    opciones_ayunas = ["70", "80", "90", "95", "100", "105", "110", "120", "126", "130", "140"]
    opciones_post = ["90", "110", "130", "140", "150", "160", "180", "200", "220"]
    opciones_peso = [str(i) for i in range(40, 151)]  # 40kg – 150kg
    opciones_estatura = ["1.40", "1.45", "1.50", "1.55", "1.60", "1.65", "1.70", "1.75", "1.80", "1.85", "1.90", "1.95", "2.00"]

    # ============================================
    #   CAMPOS CON COMBOBOX
    # ============================================

    def crear_fila(lbl_texto, fila, opciones):
        lbl = tk.Label(
            cuerpo,
            text=lbl_texto,
            font=("Segoe UI", 12),
            bg="white"
        )
        lbl.grid(row=fila, column=0, sticky="w", pady=6)

        combo = ttk.Combobox(
            cuerpo,
            values=opciones,
            font=("Segoe UI", 12),
            width=12,
            state="readonly"
        )
        combo.grid(row=fila, column=1, padx=10, pady=6)

        return combo

    entrada_ayunas = crear_fila("Glucosa en ayunas (mg/dL):", 0, opciones_ayunas)
    entrada_post   = crear_fila("Glucosa postprandial (mg/dL):", 1, opciones_post)
    entrada_peso   = crear_fila("Peso (kg):", 2, opciones_peso)
    entrada_estatura = crear_fila("Estatura (m):", 3, opciones_estatura)

    # ================================
    #   SÍNTOMAS
    # ================================
    sintomas_lbl = tk.Label(
        cuerpo,
        text="Síntomas:",
        font=("Segoe UI", 12, "bold"),
        bg="white"
    )
    sintomas_lbl.grid(row=4, column=0, sticky="w", pady=(15, 5))

    sed_var = tk.BooleanVar()
    miccion_var = tk.BooleanVar()
    fatiga_var = tk.BooleanVar()

    chk_sed = tk.Checkbutton(cuerpo, text="Sed excesiva", variable=sed_var, bg="white", font=("Segoe UI", 11))
    chk_miccion = tk.Checkbutton(cuerpo, text="Micción frecuente", variable=miccion_var, bg="white", font=("Segoe UI", 11))
    chk_fatiga = tk.Checkbutton(cuerpo, text="Fatiga", variable=fatiga_var, bg="white", font=("Segoe UI", 11))

    chk_sed.grid(row=5, column=0, sticky="w", pady=2)
    chk_miccion.grid(row=6, column=0, sticky="w", pady=2)
    chk_fatiga.grid(row=7, column=0, sticky="w", pady=2)

    # ================================
    #   ANTECEDENTES
    # ================================
    antecedentes_lbl = tk.Label(
        cuerpo,
        text="Antecedentes:",
        font=("Segoe UI", 12, "bold"),
        bg="white"
    )
    antecedentes_lbl.grid(row=8, column=0, sticky="w", pady=(15, 5))

    antecedente_var = tk.BooleanVar()
    chk_ant = tk.Checkbutton(
        cuerpo,
        text="Antecedentes familiares de diabetes",
        variable=antecedente_var,
        bg="white",
        font=("Segoe UI", 11)
    )
    chk_ant.grid(row=9, column=0, sticky="w", pady=2)

    return {
        "ayunas": entrada_ayunas,
        "post": entrada_post,
        "peso": entrada_peso,
        "estatura": entrada_estatura,
        "sed": sed_var,
        "miccion": miccion_var,
        "fatiga": fatiga_var,
        "antecedentes": antecedente_var
    }
