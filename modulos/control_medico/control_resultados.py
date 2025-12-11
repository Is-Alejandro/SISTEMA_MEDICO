import tkinter as tk

# ============================================================
# PANEL PROFESIONAL DE DIAGNÓSTICO CLÍNICO
# ============================================================

ICONOS_RIESGO = {
    "BAJO": "🟢🩺",
    "MODERADO": "🟡⚠️",
    "ALTO": "🔴🚨",
    "ERROR": "❗"
}

COLORES_RIESGO = {
    "BAJO": "#198754",      # verde
    "MODERADO": "#ffc107",  # amarillo
    "ALTO": "#dc3545",      # rojo
    "ERROR": "#dc3545",
}


def construir_panel_resultados(parent):
    """
    Crea un panel de diagnóstico profesional,
    con fondo dinámico según el nivel de riesgo.
    """

    card = tk.Frame(
        parent,
        bg="#ffffff",
        relief="solid",
        borderwidth=1,
        padx=0,
        pady=0,
        highlightthickness=1,
        highlightbackground="#e5e5e5"
    )

    # Dejamos que el alto sea automático y adaptable
    card.config(width=380)
    card.pack_propagate(True)

    # --- CONTENEDOR INTERNO QUE CAMBIARÁ DE COLOR ---
    fondo = tk.Frame(card, bg="#ffffff")
    fondo.pack(fill="both", expand=True)

    # Título de riesgo
    lbl_titulo = tk.Label(
        fondo,
        text="Diagnóstico clínico",
        font=("Segoe UI", 18, "bold"),
        bg="#ffffff",
        fg="#1c1c1c"
    )
    lbl_titulo.pack(pady=(15, 5))

    # Icono
    lbl_icono = tk.Label(
        fondo,
        text="🩺",
        font=("Segoe UI Emoji", 40),
        bg="#ffffff"
    )
    lbl_icono.pack(pady=(0, 10))

    # Contenido de texto
    lbl_contenido = tk.Label(
        fondo,
        text="(Esperando evaluación...)",
        font=("Segoe UI", 12),
        bg="#ffffff",
        fg="#ffffff",
        justify="left",
        anchor="nw",
        wraplength=360  # más ancho para texto más fluido
    )
    lbl_contenido.pack(fill="both", expand=True, padx=20, pady=(5, 15))

    return card, {
        "fondo": fondo,
        "titulo": lbl_titulo,
        "icono": lbl_icono,
        "contenido": lbl_contenido
    }


# ============================================================
# GENERADORES DE TEXTO DETALLADO
# ============================================================

def generar_descripcion(sintomas, dias, temp):
    txt = "📋 *Descripción clínica general*\n\n"
    txt += "• El paciente presenta "

    if sintomas:
        txt += ", ".join(s.lower() for s in sintomas)
    else:
        txt += "síntomas inespecíficos"

    txt += f".\n• Duración: {dias} días.\n• Temperatura: {temp}°C.\n\n"
    return txt


def generar_lista_motivos(motivos):
    if not motivos:
        return ""

    txt = "🧩 *Factores relevantes detectados*\n\n"
    for m in motivos:
        txt += f"• {m}\n"
    return txt + "\n"


def generar_plan(nivel):
    """
    Caja interna con sugerencias clínicas según el nivel de riesgo.
    """
    txt = "💊 *Plan recomendado*\n\n"

    txt += "• Mantener hidratación.\n"
    txt += "• Controlar temperatura cada 4 horas.\n"
    txt += "• Evitar esfuerzos físicos.\n"

    if nivel == "ALTO":
        txt += "• Acudir a emergencias inmediatamente.\n"
    elif nivel == "MODERADO":
        txt += "• Buscar consulta médica en 24-48 horas.\n"
    else:
        txt += "• Reposo y observación de síntomas.\n"

    return txt + "\n"


# ============================================================
# ACTUALIZACIÓN PRINCIPAL DEL PANEL
# ============================================================

def actualizar_diagnostico(refs, datos):
    nivel = datos["nivel"]
    motivos = datos["motivos"]
    recomendacion = datos["recomendacion"]
    sintomas = datos.get("sintomas", [])
    dias = datos.get("dias", 0)
    temp = datos.get("temp", 0)

    # Cambiar color de fondo según riesgo
    color = COLORES_RIESGO.get(nivel, "#6c757d")
    refs["fondo"].config(bg=color)

    # Cambiar colores de textos
    refs["titulo"].config(bg=color, fg="white", text=f"{nivel} - Evaluación clínica")
    refs["icono"].config(bg=color, text=ICONOS_RIESGO.get(nivel, "❗"))
    refs["contenido"].config(bg=color, fg="white")

    # Construcción del mensaje final
    texto = ""

    texto += generar_descripcion(sintomas, dias, temp)
    texto += generar_lista_motivos(motivos)
    texto += generar_plan(nivel)

    texto += "🔎 *Recomendación principal*\n"
    texto += recomendacion + "\n"

    refs["contenido"].config(text=texto)
