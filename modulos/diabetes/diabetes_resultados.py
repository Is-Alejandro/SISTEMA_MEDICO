import tkinter as tk

ICONOS_RIESGO = {
    "BAJO": "🟢",
    "MODERADO": "🟡",
    "ALTO": "🔴",
}

COLORES_RIESGO = {
    "BAJO": "#16a34a",
    "MODERADO": "#eab308",
    "ALTO": "#dc2626"
}


def construir_panel_resultados_diabetes(parent):
    """
    Crea el panel vacío donde se mostrarán los resultados.
    Devuelve el frame y un diccionario con referencias para actualizar luego.
    """

    card = tk.Frame(
        parent,
        bg="white",
        relief="solid",
        borderwidth=1,
        padx=30,
        pady=25
    )
    card.pack(fill="x", padx=20, pady=20)

    # ================================
    # CABECERA DEL RESULTADO
    # ================================
    header = tk.Label(
        card,
        text="Resultado de Evaluación de Diabetes",
        font=("Segoe UI", 18, "bold"),
        bg="white",
        fg="#333"
    )
    header.pack()

    # Línea separadora
    separador = tk.Frame(card, bg="#ddd", height=1)
    separador.pack(fill="x", pady=10)

    # ================================
    # CUERPO EN DOS COLUMNAS
    # ================================
    cuerpo = tk.Frame(card, bg="white")
    cuerpo.pack(fill="x")

    col_izq = tk.Frame(cuerpo, bg="white")
    col_der = tk.Frame(cuerpo, bg="white")

    col_izq.pack(side="left", fill="both", expand=True, padx=10)
    col_der.pack(side="right", fill="both", expand=True, padx=10)

    # ================================
    # ETIQUETAS
    # ================================
    lbl_nivel = tk.Label(col_izq, text="", font=("Segoe UI", 15, "bold"), bg="white")
    lbl_nivel.pack(anchor="w", pady=(0, 10))

    lbl_desc = tk.Label(col_izq, text="", font=("Segoe UI", 12), bg="white", justify="left", wraplength=500)
    lbl_desc.pack(anchor="w", pady=5)

    lbl_recomendacion = tk.Label(col_izq, text="", font=("Segoe UI", 12, "italic"), bg="white", justify="left", wraplength=500)
    lbl_recomendacion.pack(anchor="w", pady=(10, 20))

    # FACTORES
    lbl_factores_titulo = tk.Label(col_der, text="Factores relevantes:", font=("Segoe UI", 12, "bold"), bg="white")
    lbl_factores_titulo.pack(anchor="w")

    lbl_factores = tk.Label(col_der, text="", font=("Segoe UI", 12), bg="white", justify="left", wraplength=500)
    lbl_factores.pack(anchor="w", pady=5)

    # PLAN
    lbl_plan_titulo = tk.Label(col_der, text="Plan recomendado:", font=("Segoe UI", 12, "bold"), bg="white")
    lbl_plan_titulo.pack(anchor="w", pady=(15, 0))

    lbl_plan = tk.Label(col_der, text="", font=("Segoe UI", 12), bg="white", justify="left", wraplength=500)
    lbl_plan.pack(anchor="w", pady=5)

    # Devuelve todas las referencias para poder actualizar luego
    return {
        "card": card,
        "nivel": lbl_nivel,
        "descripcion": lbl_desc,
        "recomendacion": lbl_recomendacion,
        "factores": lbl_factores,
        "plan": lbl_plan
    }


def actualizar_resultados_diabetes(componentes, resultado):
    """
    Actualiza los textos del panel con los datos calculados.
    """
    nivel = resultado["nivel_riesgo"]
    componentes["nivel"].config(
        text=f"{ICONOS_RIESGO[nivel]} Nivel de riesgo: {nivel}",
        fg=COLORES_RIESGO[nivel]
    )

    componentes["descripcion"].config(text=resultado["descripcion_general"])
    componentes["recomendacion"].config(text="Recomendación principal: \n" + resultado["recomendacion_principal"])

    # Factores listados
    factores_texto = "\n".join([f"• {f}" for f in resultado["factores_relevantes"]])
    componentes["factores"].config(text=factores_texto)

    # Plan recomendado
    componentes["plan"].config(text=resultado["plan_recomendado"])
    