import tkinter as tk

# ============================================================
# PANEL DE RESULTADOS CLÍNICOS (DIAGNÓSTICO COMPLETO)
# ============================================================

def construir_panel_resultados(parent):
    """
    Construye el panel de diagnóstico clínico con espacio
    para análisis extendido, factores y recomendaciones.
    """

    card = tk.Frame(
        parent,
        bg="white",
        relief="solid",
        borderwidth=1,
        padx=20,
        pady=15,
        highlightthickness=1,
        highlightbackground="#e5e5e5"
    )
    card.config(width=380, height=420)
    card.pack_propagate(False)

    lbl_titulo = tk.Label(
        card,
        text="Diagnóstico clínico",
        font=("Segoe UI", 16, "bold"),
        bg="white"
    )
    lbl_titulo.pack(pady=(5, 10))

    lbl_contenido = tk.Label(
        card,
        text="(Esperando evaluación...)",
        font=("Segoe UI", 12),
        bg="white",
        fg="#6c757d",
        justify="left",
        anchor="nw",
        wraplength=330
    )
    lbl_contenido.pack(fill="both", expand=True)

    return card, {
        "titulo": lbl_titulo,
        "contenido": lbl_contenido
    }


# ============================================================
# FUNCIÓN PARA GENERAR TEXTO DETALLADO DEL DIAGNÓSTICO
# ============================================================

def generar_descripcion_clinica(sintomas, dias, temp):
    texto = "Descripción del cuadro clínico:\n"
    texto += "El paciente presenta "

    # --- Resumen de síntomas ---
    if sintomas:
        texto += ", ".join(sintomas).lower()
    else:
        texto += "síntomas inespecíficos"

    texto += f" desde hace {dias} días, con una temperatura de {temp}°C.\n"

    # Interpretación general
    if temp >= 38:
        texto += "La fiebre elevada sugiere un proceso infeccioso activo. "
    if "Tos" in sintomas or "Tos productiva" in sintomas:
        texto += "La tos indica compromiso del tracto respiratorio. "
    if "Dificultad para respirar" in sintomas:
        texto += "La dificultad respiratoria es un síntoma de alarma importante. "

    texto += "\n\n"
    return texto


def generar_factores_agravantes(motivos):
    texto = "Factores que agravan la condición:\n"
    for m in motivos:
        texto += f"• {m}\n"
    texto += "\n"
    return texto


def generar_recomendaciones_detalladas(nivel):
    texto = "Recomendaciones clínicas detalladas:\n"

    texto += "• Mantener hidratación abundante.\n"
    texto += "• Evitar actividad física intensa.\n"
    texto += "• Controlar la temperatura cada 4 horas.\n"
    texto += "• Dormir en ambiente ventilado y cómodo.\n"

    if nivel == "ALTO":
        texto += "• Acudir a un centro médico inmediatamente.\n"
        texto += "• No automedicarse con antibióticos.\n"
    elif nivel == "MODERADO":
        texto += "• Considerar consulta médica en las próximas 24 horas.\n"
    else:
        texto += "• Vigilar evolución y descansar adecuadamente.\n"

    return texto + "\n"


# ============================================================
# FUNCIÓN PRINCIPAL DE ACTUALIZACIÓN
# ============================================================

def actualizar_diagnostico(refs, datos):
    nivel = datos["nivel"]
    color = datos["color"]
    motivos = datos["motivos"]
    recomendacion = datos["recomendacion"]
    sintomas = datos.get("sintomas", [])
    dias = datos.get("dias", 0)
    temp = datos.get("temp", 0)

    # --- Construcción del texto extendido ---
    texto_final = ""

    texto_final += generar_descripcion_clinica(sintomas, dias, temp)
    texto_final += generar_factores_agravantes(motivos)
    texto_final += generar_recomendaciones_detalladas(nivel)

    # --- Se mantiene recomendación final ---
    texto_final += f"Recomendación principal:\n{recomendacion}\n"

    refs["contenido"].config(
        text=texto_final,
        fg=color
    )
