import tkinter as tk
from PIL import Image, ImageTk
import os


class CardMenu(tk.Frame):
    def __init__(self, parent, icono=None, texto="", comando=None, image_path=None,
                 width=240, height=160):
        super().__init__(parent, bg="white")

        self.comando = comando
        self.W = width
        self.H = height

        # Tamaño real del frame
        self.configure(width=self.W, height=self.H)
        self.pack_propagate(False)

        # -------------------------------
        # SOMBRA
        # -------------------------------
        self.shadow = tk.Frame(
            self,
            width=self.W,
            height=self.H,
            bg="#E5E5E5"
        )
        self.shadow.place(x=4, y=4)
        self.shadow.lower()

        # -------------------------------
        # CARD PRINCIPAL
        # -------------------------------
        self.card = tk.Frame(
            self,
            width=self.W,
            height=self.H,
            bg="white",
            highlightthickness=1,
            highlightbackground="#D0D0D0"
        )
        self.card.place(x=0, y=0)
        self.card.lift()

        # -------------------------------
        # CONTENIDO
        # -------------------------------
        interior = tk.Frame(self.card, bg="white")
        interior.place(relx=0.5, rely=0.5, anchor="center")

        # =====================================
        # ICONO PNG
        # =====================================
        self.icon_image = None

        if image_path and os.path.exists(image_path):
            img = Image.open(image_path)
            img = img.resize((80, 80), Image.LANCZOS)
            self.icon_image = ImageTk.PhotoImage(img)

            lbl_icon = tk.Label(interior, image=self.icon_image, bg="white")
            lbl_icon.pack(pady=(0, 8))
            self._make_clickable(lbl_icon)

        else:
            lbl_icon = tk.Label(
                interior,
                text=icono if icono else "❔",
                font=("Arial", 45),
                bg="white"
            )
            lbl_icon.pack(pady=(0, 8))
            self._make_clickable(lbl_icon)

        # TEXTO
        lbl_texto = tk.Label(
            interior,
            text=texto,
            font=("Arial", 14, "bold"),
            bg="white"
        )
        lbl_texto.pack()
        self._make_clickable(lbl_texto)

        # Bind general
        self._make_clickable(self.card)
        self._make_clickable(self)

        # -----------------------------
        # EFECTOS HOVER
        # -----------------------------
        self.card.bind("<Enter>", self._hover_on)
        self.card.bind("<Leave>", self._hover_off)
        self.bind("<Enter>", self._hover_on)
        self.bind("<Leave>", self._hover_off)

    # =====================================================
    # CLICKABLE
    # =====================================================
    def _make_clickable(self, widget):
        widget.bind("<Button-1>", lambda e: self.comando() if self.comando else None)

    # =====================================================
    # HOVER
    # =====================================================
    def _hover_on(self, event):
        self.card.configure(highlightbackground="#8CCFC1", highlightthickness=2)
        self.shadow.place(x=6, y=6)
        self.shadow.lower()

    def _hover_off(self, event):
        self.card.configure(highlightbackground="#D0D0D0", highlightthickness=1)
        self.shadow.place(x=4, y=4)
        self.shadow.lower()
