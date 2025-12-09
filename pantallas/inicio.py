import tkinter as tk


class PantallaInicio(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="white")
        self.app = app

        # ----------------------------
        # CONTENIDO PRINCIPAL
        # ----------------------------

        # Icono (emoji temporal)
        icono = tk.Label(
            self,
            text="🩺",
            font=("Arial", 80),
            bg="white"
        )
        icono.pack(pady=20)

        # Título
        titulo = tk.Label(
            self,
            text="Sistema Experto de Control Médico",
            font=("Arial", 28, "bold"),
            bg="white"
        )
        titulo.pack(pady=10)

        # Subtítulo
        subtitulo = tk.Label(
            self,
            text="Bienvenido al asistente médico virtual",
            font=("Arial", 16),
            fg="#555",
            bg="white"
        )
        subtitulo.pack(pady=5)

        # Botón iniciar
        btn_iniciar = tk.Button(
            self,
            text="INICIAR",
            font=("Arial", 16, "bold"),
            bg="#0d9488",
            fg="white",
            padx=20,
            pady=10,
            command=self.pasar_al_menu
        )
        btn_iniciar.pack(pady=40)

    def pasar_al_menu(self):
        self.app.mostrar_pantalla("menu")
