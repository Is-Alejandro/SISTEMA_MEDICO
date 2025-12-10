import tkinter as tk
from tkinter import ttk

from componentes_ui.scrollable_frame import ScrollableFrame


# -----------------------------------------------------------
#  CREA UN CONTENEDOR CON SCROLL VERTICAL
# -----------------------------------------------------------
def crear_scrollable_container(parent, padding=(20, 20)):
    container = ttk.Frame(parent)
    container.pack(fill="both", expand=True)

    scroll = ScrollableFrame(container)
    scroll.pack(fill="both", expand=True, padx=padding[0], pady=padding[1])

    return scroll.scrollable_frame


# -----------------------------------------------------------
#  CREA UNA SECCIÓN CON TÍTULO
# -----------------------------------------------------------
def crear_seccion(parent, titulo, padding=(0, 15)):
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
#  CREA UNA FILA DE COLUMNAS PERFECTAMENTE DISTRIBUIDAS
# -----------------------------------------------------------
def crear_columnas(parent, num_columnas=2, separacion=20):
    contenedor = ttk.Frame(parent)
    contenedor.pack(fill="x", pady=10, expand=True)

    columnas = []

    # Asegurar que cada columna tiene el mismo tamaño exacto
    for i in range(num_columnas):
        contenedor.grid_columnconfigure(i, weight=1, uniform="columnas")

        col = ttk.Frame(contenedor)
        col.grid(row=0, column=i, padx=(0 if i == 0 else separacion), sticky="nsew")

        columnas.append(col)

    return columnas


# -----------------------------------------------------------
#  PADDING ESTÁNDAR
# -----------------------------------------------------------
def agregar_padding(widget, pady=10):
    widget.pack_configure(pady=pady)
