import tkinter as tk

# ============================================================
# CARD DE NOTAS DEL PACIENTE
# ============================================================

def construir_panel_notas(parent):
    """
    Construye una card grande para registrar notas,
    observaciones u otros síntomas no listados.
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
    card.config(width=760, height=200)
    card.pack_propagate(False)

    lbl_titulo = tk.Label(
        card,
        text="Notas del paciente / Observaciones",
        font=("Segoe UI", 16, "bold"),
        bg="white",
        fg="#1c1c1c"
    )
    lbl_titulo.pack(anchor="w", pady=(0, 8))

    txt_nota = tk.Text(
        card,
        font=("Segoe UI", 12),
        height=6,
        width=80,
        wrap="word",
        bd=1,
        relief="solid"
    )
    txt_nota.pack(fill="both", expand=True)

    return card, {
        "nota": txt_nota
    }


# ============================================================
# Función para obtener la nota escrita por el usuario
# ============================================================

def obtener_nota(refs):
    return refs["nota"].get("1.0", tk.END).strip()
