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

        # Estado visual
        self.normal_bg = "white"
        self.hover_bg = "#F8FFFB"        # fondo suave en hover
        self.normal_border = "#D0D0D0"
        self.hover_border = "#4CAF50"

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
            bg="#E5E5E5"  # gris suave
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
            bg=self.normal_bg,
            highlightthickness=1,
            highlightbackground=self.normal_border
        )
        self.card.place(x=0, y=0)
        self.card.lift()

        # -------------------------------
        # CONTENIDO
        # -------------------------------
        interior = tk.Frame(self.card, bg=self.normal_bg)
        interior.place(relx=0.5, rely=0.5, anchor="center")

        # =====================================
        # ICONO PNG
        # =====================================
        self.icon_image = None

        if image_path and os.path.exists(image_path):
            img = Image.open(image_path)
            img = img.resize((80, 80), Image.LANCZOS)
            self.icon_image = ImageTk.PhotoImage(img)

            lbl_icon = tk.Label(interior, image=self.icon_image, bg=self.normal_bg)
        else:
            lbl_icon = tk.Label(
                interior,
                text=icono if icono else "❔",
                font=("Arial", 45),
                bg=self.normal_bg
            )

        lbl_icon.pack(pady=(0, 8))
        self._make_clickable(lbl_icon)

        # TEXTO
        lbl_texto = tk.Label(
            interior,
            text=texto,
            font=("Arial", 14, "bold"),
            bg=self.normal_bg
        )
        lbl_texto.pack()
        self._make_clickable(lbl_texto)

        # Binds generales (hover + click)
        self._apply_hover_events(self)
        self._apply_hover_events(self.card)
        self._apply_hover_events(interior)
        self._apply_hover_events(lbl_icon)
        self._apply_hover_events(lbl_texto)

    # =====================================================
    # CLICKABLE
    # =====================================================
    def _make_clickable(self, widget):
        widget.bind("<Button-1>", lambda e: self._click_effect())

    def _click_effect(self):
        # Efecto de clic comprimido
        self.card.place(x=1, y=1)
        self.shadow.place(x=5, y=5)
        self.after(120, lambda: self._reset_click())

        if self.comando:
            self.after(150, self.comando)

    def _reset_click(self):
        self.card.place(x=0, y=0)
        self.shadow.place(x=6, y=6)

    # =====================================================
    # HOVER
    # =====================================================
    def _apply_hover_events(self, widget):
        widget.bind("<Enter>", self._hover_on)
        widget.bind("<Leave>", self._hover_off)

    def _hover_on(self, event):
        self.card.configure(
            highlightbackground=self.hover_border,
            highlightthickness=2,
            bg=self.hover_bg
        )
        self.shadow.place(x=6, y=6)

    def _hover_off(self, event):
        self.card.configure(
            highlightbackground=self.normal_border,
            highlightthickness=1,
            bg=self.normal_bg
        )
        self.shadow.place(x=4, y=4)
