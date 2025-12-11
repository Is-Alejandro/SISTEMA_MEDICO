import tkinter as tk
from PIL import Image, ImageTk, ImageFilter


class PantallaInicio(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="white")
        self.app = app

        # ==================================
        #   CARGAR FONDO
        # ==================================
        try:
            bg_image = Image.open("assets/fondo_medico.png")
            bg_image = bg_image.resize((1700, 1200), Image.Resampling.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(bg_image)

            fondo = tk.Label(self, image=self.bg_photo, bg="white")
            fondo.place(relx=0, rely=0, relwidth=1, relheight=1)
        except Exception as e:
            print("No se pudo cargar la imagen de fondo:", e)

        # ==================================
        #   GENERAR SOMBRA DIFUSA REAL
        # ==================================
        shadow = Image.new("RGBA", (600, 380), (0, 0, 0, 0))
        shadow_layer = Image.new("RGBA", (550, 330), (0, 0, 0, 80))  # sombra tenue
        shadow.paste(shadow_layer, (25, 25))

        shadow = shadow.filter(ImageFilter.GaussianBlur(20))
        self.shadow_tk = ImageTk.PhotoImage(shadow)

        sombra_label = tk.Label(self, image=self.shadow_tk, bg="white", borderwidth=0)
        sombra_label.place(relx=0.5, rely=0.45, anchor="center")

        # ==================================
        #   CARD CENTRAL (INVISIBLE)
        # ==================================
        card = tk.Frame(
            self,
            bg="white",
            bd=0,
            highlightthickness=0
        )
        card.place(relx=0.5, rely=0.45, anchor="center")

        # ==================================
        #   ICONO GRANDE
        # ==================================
        try:
            icono_img = Image.open("assets/icons/icono_medico.png")
            icono_img = icono_img.resize((160, 160), Image.Resampling.LANCZOS)
            self.icono_render = ImageTk.PhotoImage(icono_img)

            icono = tk.Label(card, image=self.icono_render, bg="white")
            icono.pack(pady=(10, 10))

        except:
            icono = tk.Label(card, text="🩺", font=("Segoe UI", 90), bg="white")
            icono.pack(pady=(10, 10))

        # ==================================
        #   TÍTULOS
        # ==================================
        titulo = tk.Label(
            card,
            text="Sistema Experto de Control Médico",
            font=("Segoe UI", 30, "bold"),
            fg="#2c3e50",
            bg="white"
        )
        titulo.pack(pady=(5, 5))

        subtitulo = tk.Label(
            card,
            text="Asistente médico virtual con análisis inteligente",
            font=("Segoe UI", 15),
            fg="#555",
            bg="white"
        )
        subtitulo.pack(pady=(0, 20))

        # ==================================
        #   BOTÓN INICIAR (MODERNO)
        # ==================================
        btn_iniciar = tk.Label(
            card,
            text="INICIAR",
            font=("Segoe UI", 17, "bold"),
            bg="#14b8a6",
            fg="white",
            padx=40,
            pady=14,
            cursor="hand2"
        )
        btn_iniciar.pack(pady=(5, 20))

        btn_iniciar.bind("<Button-1>", lambda e: self.pasar_al_menu())
        btn_iniciar.bind("<Enter>", lambda e: btn_iniciar.configure(bg="#0d9488"))
        btn_iniciar.bind("<Leave>", lambda e: btn_iniciar.configure(bg="#14b8a6"))

        # ==================================
        #   FOOTER
        # ==================================
        texto_inferior = tk.Label(
            card,
            text="Versión 1.0 — Optimizado por IA médica",
            font=("Segoe UI", 10),
            fg="#777",
            bg="white"
        )
        texto_inferior.pack(pady=(0, 10))

        # ==================================
        #   EFECTO FADE-IN (APLICADO A LA VENTANA)
        # ==================================
        try:
            self.app.attributes("-alpha", 0)
            self.fade_in()
        except:
            pass

    # ==================================
    #   FUNCIÓN DE ANIMACIÓN FADE-IN
    # ==================================
    def fade_in(self):
        try:
            alpha = self.app.attributes("-alpha")
            if alpha < 1:
                alpha += 0.05
                self.app.attributes("-alpha", alpha)
                self.after(30, self.fade_in)
        except:
            pass

    def pasar_al_menu(self):
        self.app.mostrar_pantalla("menu")
