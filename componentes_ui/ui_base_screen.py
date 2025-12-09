import tkinter as tk
from tkinter import ttk


class UIBaseScreen(ttk.Frame):
    """
    Pantalla base profesional para módulos internos.
    Incluye:
     - Botón Volver
     - Título grande
     - Subtítulo
     - Contenedor principal (card)
    """

    def __init__(self, parent, controller, titulo="", subtitulo="", icono=None):
        super().__init__(parent)
        self.controller = controller
        self.configure(style="Base.TFrame")

        # =====================================
        # CONFIGURAR ESTILOS
        # =====================================
        self._configurar_estilos()

        # =====================================
        # HEADER (Botón + Títulos)
        # =====================================
        header = ttk.Frame(self, style="Base.TFrame")
        header.pack(fill="x", pady=(10, 5), padx=20)

        # Botón Volver
        btn_volver = ttk.Button(
            header,
            text="⬅ Volver al menú",
            style="Volver.TButton",
            command=self.controller.volver_menu
        )
        btn_volver.pack(side="left")

        # Sección de textos
        textos_frame = ttk.Frame(self, style="Base.TFrame")
        textos_frame.pack(pady=(5, 20))

        # Icono opcional
        if icono:
            lbl_icono = tk.Label(textos_frame, image=icono, bg="white")
            lbl_icono.pack()

        # Título
        lbl_titulo = ttk.Label(
            textos_frame,
            text=titulo,
            style="Titulo.TLabel"
        )
        lbl_titulo.pack(pady=(5, 0))

        # Subtítulo
        lbl_subtitulo = ttk.Label(
            textos_frame,
            text=subtitulo,
            style="Subtitulo.TLabel"
        )
        lbl_subtitulo.pack()

        # =====================================
        # CONTENEDOR PRINCIPAL (CARD)
        # =====================================
        self.card = tk.Frame(
            self,
            bg="white",
            highlightthickness=1,
            highlightbackground="#DADADA"
        )
        self.card.pack(padx=40, pady=10)

        # Sombra suave
        self.shadow = tk.Frame(
            self,
            bg="#ECECEC",
            width=1,
            height=1
        )
        self.shadow.lower()
        self.card.bind("<Configure>", self._actualizar_sombra)

    # =====================================================
    # SOMBRA REALISTA
    # =====================================================
    def _actualizar_sombra(self, event):
        self.shadow.place(
            x=self.card.winfo_x() + 3,
            y=self.card.winfo_y() + 3,
            width=self.card.winfo_width(),
            height=self.card.winfo_height()
        )

    # =====================================================
    # ESTILOS PROFESIONALES
    # =====================================================
    def _configurar_estilos(self):
        style = ttk.Style()

        style.configure("Base.TFrame", background="white")

        style.configure(
            "Titulo.TLabel",
            font=("Arial", 26, "bold"),
            foreground="#333",
            background="white"
        )

        style.configure(
            "Subtitulo.TLabel",
            font=("Arial", 12),
            foreground="#777",
            background="white"
        )

        style.configure(
            "Volver.TButton",
            font=("Arial", 11),
            padding=6
        )

    # =====================================================
    # MÉTODO PARA OBTENER EL CONTENEDOR PRINCIPAL
    # =====================================================
    def get_card(self):
        return self.card
