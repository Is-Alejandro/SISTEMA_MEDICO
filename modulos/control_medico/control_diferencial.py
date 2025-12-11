import tkinter as tk

# ============================================================
# PANEL DE DIAGNÓSTICO DIFERENCIAL
# ============================================================

def construir_panel_diagnostico_diferencial(parent):
    """
    Construye una card independiente con explicación del
    diagnóstico diferencial basado en síntomas seleccionados.
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
    card.config(width=380, height=300)
    card.pack_propagate(False)

    lbl_titulo = tk.Label(
        card,
        text="Diagnóstico Diferencial",
        font=("Segoe UI", 16, "bold"),
        bg="white",
        fg="#1c1c1c"
    )
    lbl_titulo.pack(pady=(5, 10))

    lbl_contenido = tk.Label(
        card,
        text="(Esperando análisis...)",
        font=("Segoe UI", 12),
        bg="white",
        fg="#6c757d",
        justify="left",
        anchor="nw",
        wraplength=330
    )
    lbl_contenido.pack(fill="both", expand=True)

    return card, {
        "contenido": lbl_contenido
    }


# ============================================================
# FUNCIÓN PARA GENERAR DIAGNÓSTICO DIFERENCIAL
# ============================================================

def generar_diagnostico_diferencial(sintomas, tipo_tos, dias):
    posibles = []

    # Procesos infecciosos respiratorios
    if "Fiebre" in sintomas or "Tos" in sintomas:
        posibles.append("Infección respiratoria alta")

    # Faringitis
    if "Dolor de garganta" in sintomas:
        posibles.append("Faringitis viral")
        posibles.append("Faringitis bacteriana")

    # Bronquitis
    if tipo_tos == "con flema":
        posibles.append("Bronquitis aguda")

    # Sinusitis
    if "Congestión nasal" in sintomas and "Dolor de cabeza" in sintomas:
        posibles.append("Sinusitis")

    # Cuadro febril inespecífico
    if "Fiebre" in sintomas and dias <= 3:
        posibles.append("Cuadro febril inespecífico")

    # Cuadro respiratorio prolongado
    if dias >= 5:
        posibles.append("Cuadro respiratorio prolongado")

    if not posibles:
        posibles.append("No se identifican causas sugestivas con los datos actuales.")

    texto = "Posibles condiciones asociadas:\n"
    for p in posibles:
        texto += f"• {p}\n"

    return texto


# ============================================================
# FUNCIÓN PRINCIPAL PARA ACTUALIZAR LA CARD
# ============================================================

def actualizar_diagnostico_diferencial(refs, sintomas, tipo_tos, dias):
    texto = generar_diagnostico_diferencial(sintomas, tipo_tos, dias)
    refs["contenido"].config(text=texto, fg="#1c1c1c")
