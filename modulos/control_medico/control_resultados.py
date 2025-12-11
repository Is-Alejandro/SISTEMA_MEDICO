import tkinter as tk

# ============================================================
# PANEL DE RESULTADOS CLÍNICOS (DIAGNÓSTICO)
# ============================================================

def construir_panel_resultados(parent):
    """
    Construye el panel de diagnóstico clínico dentro de la interfaz.

    Retorna:
    - frame contenedor
    - diccionario con referencias a los labels para actualizarlos
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
    card.config(width=320, height=330)
    card.pack_propagate(False)

    # --- Título ---
    lbl_titulo = tk.Label(
        card,
        text="Diagnóstico clínico",
        font=("Segoe UI", 16, "bold"),
        bg="white"
    )
    lbl_titulo.pack(pady=(10, 5))

    # --- Contenido ---
    lbl_contenido = tk.Label(
        card,
        text="(Esperando evaluación...)",
        font=("Segoe UI", 13),
        bg="white",
        fg="#6c757d",
        justify="left",
        wraplength=260
    )
    lbl_contenido.pack()

    return card, {
        "titulo": lbl_titulo,
        "contenido": lbl_contenido
    }


# ============================================================
# FUNCIÓN PARA MOSTRAR EL RESULTADO CLÍNICO
# ============================================================
def actualizar_diagnostico(refs, datos):
    """
    Actualiza el diagnóstico clínico.
    
    Parámetros:
    - refs: diccionario con referencias a labels (titulo, contenido)
    - datos: dict proveniente de control_core.evaluar_control_medico()

    datos = {
        "nivel": str,
        "color": "#HEX",
        "motivos": [...],
        "recomendacion": str
    }
    """

    nivel = datos["nivel"]
    color = datos["color"]
    motivos = datos["motivos"]
    recomendacion = datos["recomendacion"]

    texto_final = f"Nivel de riesgo: {nivel}\n\nMotivos:\n"
    for m in motivos:
        texto_final += f"• {m}\n"

    texto_final += f"\nRecomendación:\n{recomendacion}"

    refs["contenido"].config(text=texto_final, fg=color)


# ============================================================
# FUNCIÓN PARA LIMPIAR EL PANEL
# ============================================================
def limpiar_diagnostico(refs):
    refs["contenido"].config(
        text="(Esperando evaluación...)",
        fg="#6c757d"
    )
