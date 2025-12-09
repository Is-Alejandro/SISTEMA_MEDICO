import tkinter as tk
from ttkbootstrap import Style
from componentes_ui.card_menu import CardMenu


class MenuPrincipal(tk.Frame):
    CARD_WIDTH = 240
    CARD_HEIGHT = 160

    def __init__(self, parent, app):
        super().__init__(parent, bg="white")
        self.app = app

        # Bootstrap theme
        Style(theme="minty")

        # Título
        tk.Label(
            self,
            text="Menú Principal",
            font=("Arial", 32, "bold"),
            bg="white"
        ).pack(pady=(20, 5))

        tk.Label(
            self,
            text="Seleccione una opción",
            font=("Arial", 15),
            fg="#555",
            bg="white"
        ).pack(pady=(0, 20))

        # Contenedor
        contenedor = tk.Frame(self, bg="white")
        contenedor.pack(pady=10)

        MODULOS = [
            ("IMC", "imc", "assets/icons/imc.png"),
            ("Control Médico", "control_medico", "assets/icons/control_medico.png"),
            ("Diabetes", "diabetes", "assets/icons/diabetes.png"),
            ("Urgencias", "urgencias", "assets/icons/urgencia.png"),
            ("Comidas", "comidas", "assets/icons/comidas.png"),
            ("Embarazo", "embarazo", "assets/icons/embarazo.png"),
            ("Registrar Usuario", "registro_usuario", "assets/icons/registrar_usuario.png"),
            ("Crear Cita", "crear_cita", "assets/icons/crear_cita.png"),
            ("Ver Citas", "ver_citas", "assets/icons/ver_citas.png"),
        ]

        fila = 0
        columna = 0

        for texto, modulo, img in MODULOS:
            card = CardMenu(
                contenedor,
                texto=texto,
                comando=lambda m=modulo: self.abrir_modulo(m),
                image_path=img,
                width=self.CARD_WIDTH,
                height=self.CARD_HEIGHT
            )
            card.grid(row=fila, column=columna, padx=40, pady=30)

            columna += 1
            if columna == 3:
                columna = 0
                fila += 1

        # Botón admin
        tk.Button(
            self,
            text="🔐 Ingresar como Administrador",
            font=("Arial", 14, "bold"),
            fg="#222",
            bg="#96d6c6",
            padx=25,
            pady=12,
            relief="flat",
            command=self.abrir_login_admin
        ).pack(pady=25)

    def abrir_login_admin(self):
        ventana = tk.Toplevel(self)
        ventana.title("Ingreso Administrador")
        ventana.geometry("330x180")
        ventana.resizable(False, False)
        ventana.configure(bg="white")

        tk.Label(
            ventana,
            text="Ingrese clave de administrador:",
            font=("Arial", 13, "bold"),
            bg="white"
        ).pack(pady=15)

        clave_var = tk.StringVar()
        tk.Entry(ventana, textvariable=clave_var, show="•", font=("Arial", 12)).pack(pady=5)

        def validar():
            if clave_var.get() == "admin123":
                ventana.destroy()
                self.ir_admin()
            else:
                from tkinter import messagebox
                messagebox.showerror("Error", "Clave incorrecta")

        tk.Button(
            ventana,
            text="Ingresar",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            command=validar
        ).pack(pady=15)

    def abrir_modulo(self, nombre):
        self.app.mostrar_pantalla(nombre)

    def ir_admin(self):
        self.app.mostrar_pantalla("admin")
