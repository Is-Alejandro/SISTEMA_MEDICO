import tkinter as tk

class CardMenu(tk.Frame):
    def __init__(self, parent, icono, texto, comando, width=240, height=160):
        super().__init__(parent, width=width, height=height, bg="white")

        self.comando = comando
        self.icono = icono
        self.texto = texto

        # Estilo de borde simple (luego lo haremos moderno con ttkbootstrap)
        self.configure(
            highlightbackground="#C9C9C9",
            highlightthickness=1,
            cursor="hand2"
        )

        # Evita que el frame se reduzca al contenido
        self.grid_propagate(False)

        # Ícono grande
        lbl_icono = tk.Label(self, text=icono, font=("Arial", 45), bg="white")
        lbl_icono.pack(pady=(15, 0))

        # Texto debajo
        lbl_texto = tk.Label(self, text=texto, font=("Arial", 14, "bold"), bg="white")
        lbl_texto.pack(pady=(8, 0))

        # Eventos click en toda la tarjeta
        self.bind("<Button-1>", lambda e: self.comando())
        lbl_icono.bind("<Button-1>", lambda e: self.comando())
        lbl_texto.bind("<Button-1>", lambda e: self.comando())

        # Hover suave (opcional, antes de aplicar ttkbootstrap)
        self.bind("<Enter>", lambda e: self._hover(True))
        self.bind("<Leave>", lambda e: self._hover(False))
        lbl_icono.bind("<Enter>", lambda e: self._hover(True))
        lbl_icono.bind("<Leave>", lambda e: self._hover(False))
        lbl_texto.bind("<Enter>", lambda e: self._hover(True))
        lbl_texto.bind("<Leave>", lambda e: self._hover(False))

    def _hover(self, activo):
        """Efecto visual al pasar el mouse."""
        if activo:
            self.config(highlightbackground="#8E8E8E", bg="#FAFAFA")
        else:
            self.config(highlightbackground="#C9C9C9", bg="white")
