import tkinter as tk
from tkinter import ttk

from componentes_ui.scrollable_frame import ScrollableFrame


# -----------------------------------------------------------
#  CREA UN CONTENEDOR CON SCROLL VERTICAL
# -----------------------------------------------------------
def crear_scrollable_container(parent, padding=(20, 20)):
    """
    Crea un contenedor con scroll vertical reutilizable para pantallas largas.
    Retorna el frame interior donde se deben colocar los widgets.
    """

    container = ttk.Frame(parent)
    container.pack(fill="both", expand=True)

    scroll = ScrollableFrame(container)
    scroll.pack(fill="both", expand=True, padx=padding[0], pady=padding[1])

    return scroll.scrollable_frame

# -----------------------------------------------------------
#  CREA UNA SECCIÓN CON TÍTULO
# -----------------------------------------------------------
def crear_seccion(parent, titulo, padding=(0, 15)):
    """
    Crea una sección con un título grande y devuelve un frame para contenido.
    """
    lbl = ttk.Label(
        parent,
        text=titulo,
        font=("Arial", 16, "bold")
    )
    lbl.pack(anchor="w", pady=(padding[1], 5))

    frame = ttk.Frame(parent)
    frame.pack(fill="x", pady=(0, padding[1]))

    return frame


# -----------------------------------------------------------
#  CREA UNA FILA DE COLUMNAS
# -----------------------------------------------------------
def crear_columnas(parent, num_columnas=2, separacion=20):
    """
    Crea un frame con varias columnas internas.
    Retorna una lista de frames (uno por columna).
    """

    contenedor = ttk.Frame(parent)
    contenedor.pack(fill="x", pady=10)

    columnas = []

    for i in range(num_columnas):
        col = ttk.Frame(contenedor)
        col.pack(side="left", padx=(0 if i == 0 else separacion), expand=True, fill="both")
        columnas.append(col)

    return columnas


# -----------------------------------------------------------
#  AGREGA ESPACIADO ESTÁNDAR
# -----------------------------------------------------------
def agregar_padding(widget, pady=10):
    widget.pack_configure(pady=pady)
