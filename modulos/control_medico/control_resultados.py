import tkinter as tk

# ============================================================
# ICONOS Y COLORES DEL NIVEL DE RIESGO
# ============================================================

ICONOS_RIESGO = {
    "BAJO": "🟢🩺",
    "MODERADO": "🟡⚠️",
    "ALTO": "🔴🚨",
    "ERROR": "❗"
}

COLORES_RIESGO = {
    "BAJO": "#198754",
    "MODERADO": "#ffc107",
    "ALTO": "#dc3545",
    "ERROR": "#dc3545",
}

# ============================================================
# PANEL DE RESULTADOS PRINCIPAL (AMPLIO)
# ============================================================

def construir_panel_resultados(parent):
    """
    Construye un panel ancho (horizontal) donde se mostrará el diagnóstico clínico
    en dos columnas, sin ventana emergente.
    """

    # CARD ANCHA
    card = tk.Frame(
        parent,
        bg="white",
        relief="solid",
        borderwidth=1,
        padx=25,
        pady=20,
        highlightbackground="#e5e5e5"
    )

    card.config(width=900)     # ANCHO grande
    card.grid_propagate(True)  # PERMITE crecer verticalmente

    # ---------------------------------
    # TÍTULO ENCABEZADO
    # ---------------------------------
    lbl_titulo = tk.Label(
        card,
        text="Diagnóstico clínico",
        font=("Segoe UI", 22, "bold"),
        bg="white",
        fg="#1c1c1c"
    )
    lbl_titulo.pack(anchor="center", pady=(0, 15))

    # ---------------------------------
    # CONTENEDOR INTERNO (2 COLUMNAS)
    # ---------------------------------
    cont = tk.Frame(card, bg="white")
    cont.pack(fill="x", expand=True)

    cont.grid_columnconfigure(0, weight=1, minsize=430)
    cont.grid_columnconfigure(1, weight=1, minsize=430)

    # ================================
    # COLUMNA IZQUIERDA
    # ================================
    col_izq = tk.Frame(cont, bg="white")
    col_izq.grid(row=0, column=0, sticky="nw")

    # DESCRIPCIÓN
    lbl_desc = tk.Label(
        col_izq,
        text="📋 *Descripción general*",
        font=("Segoe UI", 14, "bold"),
        bg="white",
        fg="#444"
    )
    lbl_desc.pack(anchor="w", pady=(0, 5))

    txt_desc = tk.Label(
        col_izq,
        text="(sin datos)",
        font=("Segoe UI", 12),
        justify="left",
        bg="white",
        fg="#333",
        wraplength=430
    )
    txt_desc.pack(anchor="w", pady=(0, 15))

    # ⭐ NUEVO: RECOMENDACIÓN PRINCIPAL AQUÍ MISMO
    lbl_rec = tk.Label(
        col_izq,
        text="🔎 Recomendación principal:",
        font=("Segoe UI", 14, "bold"),
        bg="white",
        fg="#1c1c1c"
    )
    lbl_rec.pack(anchor="w", pady=(10, 0))

    txt_rec = tk.Label(
        col_izq,
        text="(sin datos)",
        font=("Segoe UI", 12),
        bg="white",
        fg="#333",
        justify="left",
        wraplength=430
    )
    txt_rec.pack(anchor="w", pady=(5, 20))

    # ================================
    # COLUMNA DERECHA
    # ================================
    col_der = tk.Frame(cont, bg="white")
    col_der.grid(row=0, column=1, sticky="nw")

    # FACTORES RELEVANTES
    lbl_fact = tk.Label(
        col_der,
        text="🧩 *Factores relevantes*",
        font=("Segoe UI", 14, "bold"),
        bg="white",
        fg="#444"
    )
    lbl_fact.pack(anchor="w", pady=(0, 5))

    txt_fact = tk.Label(
        col_der,
        text="(sin datos)",
        font=("Segoe UI", 12),
        justify="left",
        bg="white",
        fg="#333",
        wraplength=430
    )
    txt_fact.pack(anchor="w", pady=(0, 15))

    # PLAN RECOMENDADO
    lbl_plan = tk.Label(
        col_der,
        text="💊 *Plan recomendado*",
        font=("Segoe UI", 14, "bold"),
        bg="white",
        fg="#444"
    )
    lbl_plan.pack(anchor="w", pady=(0, 5))

    txt_plan = tk.Label(
        col_der,
        text="(sin datos)",
        font=("Segoe UI", 12),
        justify="left",
        bg="white",
        fg="#333",
        wraplength=430
    )
    txt_plan.pack(anchor="w", pady=(0, 15))

    # ---------------------------------
    # RETORNAMOS REFERENCIAS
    # ---------------------------------
    return card, {
        "titulo": lbl_titulo,
        "descripcion": txt_desc,
        "recomendacion": txt_rec,
        "factores": txt_fact,
        "plan": txt_plan
    }


# ============================================================
# GENERACIÓN DE TEXTO
# ============================================================

def generar_descripcion(sintomas, dias, temp):
    txt = ""
    txt += "• El paciente presenta "

    if sintomas:
        txt += ", ".join(s.lower() for s in sintomas)
    else:
        txt += "síntomas inespecíficos"

    txt += f".\n• Duración: {dias} días.\n• Temp: {temp}°C."
    return txt


def generar_lista_motivos(motivos):
    if not motivos:
        return "• Sin factores relevantes."
    return "\n".join(f"• {m}" for m in motivos)


def generar_plan(nivel):
    if nivel == "ALTO":
        return (
            "• Hidratación.\n"
            "• Control de fiebre.\n"
            "• Evitar esfuerzo.\n"
            "• Atención de emergencias inmediata."
        )
    elif nivel == "MODERADO":
        return (
            "• Hidratación.\n"
            "• Control sintomático.\n"
            "• Revisión médica en 24–48 horas."
        )
    else:
        return (
            "• Reposo.\n"
            "• Hidratación.\n"
            "• Monitorización de síntomas."
        )


# ============================================================
# ACTUALIZAR CARD — SIN VENTANA EMERGENTE
# ============================================================

def actualizar_diagnostico(refs, datos):
    nivel = datos["nivel"]
    sintomas = datos["sintomas"]
    motivos = datos["motivos"]
    recomendacion = datos["recomendacion"]
    temp = datos["temp"]
    dias = datos["dias"]

    # TÍTULO
    refs["titulo"].config(text=f"{nivel} – Diagnóstico clínico")

    # DESCRIPCIÓN
    refs["descripcion"].config(
        text=generar_descripcion(sintomas, dias, temp)
    )

    # RECOMENDACIÓN PRINCIPAL
    refs["recomendacion"].config(text=recomendacion)

    # FACTORES
    refs["factores"].config(
        text=generar_lista_motivos(motivos)
    )

    # PLAN
    refs["plan"].config(
        text=generar_plan(nivel)
    )
