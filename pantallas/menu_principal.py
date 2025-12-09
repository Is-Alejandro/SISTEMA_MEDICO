import tkinter as tk
from tkinter import ttk, messagebox


class MenuPrincipal(tk.Frame):
    CARD_WIDTH = 240
    CARD_HEIGHT = 160

    def __init__(self, parent, app):
        super().__init__(parent, bg="white")
        self.app = app

        # --------------------------------
        # TÍTULOS
        # --------------------------------
        titulo = tk.Label(
            self,
            text="Menú Principal",
            font=("Arial", 32, "bold"),
            bg="white"
        )
        titulo.pack(pady=(20, 5))

        subtitulo = tk.Label(
            self,
            text="Seleccione una opción",
            font=("Arial", 15),
            fg="#555",
            bg="white"
        )
        subtitulo.pack(pady=(0, 20))

        # --------------------------------
        # CONTENEDOR DE TARJETAS
        # --------------------------------
        contenedor = tk.Frame(self, bg="white")
        contenedor.pack(pady=10)

        modulos = [
            ("🧮", "IMC", "imc"),
            ("🩺", "Control Médico", "control_medico"),
            ("🩻", "Diabetes", "diabetes"),

            ("🚑", "Urgencias", "urgencias"),
            ("🍽️", "Comidas", "comidas"),
            ("🤰", "Embarazo", "embarazo"),

            ("🧍‍♂️", "Registrar Usuario", "registro_usuario"),
            ("📅", "Crear Cita", "crear_cita"),
            ("📂", "Ver Citas", "ver_citas"),
        ]

        fila = 0
        columna = 0

        for icono, texto, nombre_modulo in modulos:

            card = tk.Frame(
                contenedor,
                width=self.CARD_WIDTH,
                height=self.CARD_HEIGHT,
                bg="white",
                highlightbackground="#ccc",
                highlightthickness=1
            )
            card.grid(row=fila, column=columna, padx=30, pady=25)
            card.grid_propagate(False)

            lbl_icono = tk.Label(card, text=icono, font=("Arial", 45), bg="white")
            lbl_icono.pack(pady=(10, 0))

            lbl_texto = tk.Label(card, text=texto, font=("Arial", 14, "bold"), bg="white")
            lbl_texto.pack(pady=(5, 0))

            # Eventos click
            card.bind("<Button-1>", lambda e, n=nombre_modulo: self.abrir_modulo(n))
            lbl_icono.bind("<Button-1>", lambda e, n=nombre_modulo: self.abrir_modulo(n))
            lbl_texto.bind("<Button-1>", lambda e, n=nombre_modulo: self.abrir_modulo(n))

            columna += 1
            if columna == 3:
                columna = 0
                fila += 1

        # --------------------------------
        # BOTÓN ADMIN MEJORADO Y CENTRADO
        # --------------------------------
        admin_frame = tk.Frame(self, bg="white")
        admin_frame.pack(pady=25)

        admin_btn = tk.Button(
            admin_frame,
            text="🔐 Ingresar como Administrador",
            font=("Arial", 14, "bold"),
            fg="#222",
            bg="#dcdcdc",
            relief="solid",
            bd=1,
            padx=25,
            pady=10,
            command=self.abrir_login_admin
        )
        admin_btn.pack()

    # --------------------------------
    # LOGIN ADMIN
    # --------------------------------
    def abrir_login_admin(self):
        ventana = tk.Toplevel(self)
        ventana.title("Ingreso Administrador")
        ventana.geometry("320x180")
        ventana.resizable(False, False)
        ventana.configure(bg="white")

        titulo = tk.Label(
            ventana,
            text="Ingrese clave de administrador:",
            font=("Arial", 13, "bold"),
            bg="white"
        )
        titulo.pack(pady=15)

        clave_var = tk.StringVar()

        entry = tk.Entry(ventana, textvariable=clave_var, show="•", font=("Arial", 12))
        entry.pack(pady=5)

        def validar_clave():
            if clave_var.get() == "admin123":
                ventana.destroy()
                self.ir_admin()
            else:
                messagebox.showerror("Error", "Clave incorrecta")

        btn = tk.Button(
            ventana,
            text="Ingresar",
            font=("Arial", 12, "bold"),
            bg="#4caf50",
            fg="white",
            command=validar_clave
        )
        btn.pack(pady=15)

    # --------------------------------
    # ABRIR MÓDULO
    # --------------------------------
    def abrir_modulo(self, nombre_modulo):
        self.app.mostrar_pantalla(nombre_modulo)

    # --------------------------------
    # IR A ADMIN
    # --------------------------------
    def ir_admin(self):
        from pantallas.admin import PantallaAdmin
        self.app.mostrar_pantalla("admin")
