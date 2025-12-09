import tkinter as tk
from tkinter import ttk, messagebox

from componentes_ui.card_menu import CardMenu
from datos.modulos_menu import MODULOS_MENU


class MenuPrincipal(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="white")
        self.app = app

        # ----------------------
        # TÍTULOS
        # ----------------------
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

        # ----------------------
        # GRID DE TARJETAS
        # ----------------------
        contenedor = tk.Frame(self, bg="white")
        contenedor.pack(pady=10)

        fila = 0
        columna = 0

        for icono, texto, modulo in MODULOS_MENU:

            card = CardMenu(
                contenedor,
                icono=icono,
                texto=texto,
                comando=lambda m=modulo: self.abrir_modulo(m)
            )
            card.grid(row=fila, column=columna, padx=30, pady=25)

            columna += 1
            if columna == 3:   # 3 columnas por fila
                columna = 0
                fila += 1

        # ----------------------
        # BOTÓN ADMIN
        # ----------------------
        tk.Button(
            self,
            text="🔐 Ingresar como Administrador",
            font=("Arial", 14, "bold"),
            fg="#222",
            bg="#dcdcdc",
            relief="solid",
            bd=1,
            padx=25,
            pady=10,
            command=self.abrir_login_admin
        ).pack(pady=25)

    # ----------------------
    # ABRIR MÓDULO
    # ----------------------
    def abrir_modulo(self, nombre_modulo):
        self.app.mostrar_pantalla(nombre_modulo)

    # ----------------------
    # LOGIN ADMIN
    # ----------------------
    def abrir_login_admin(self):
        ventana = tk.Toplevel(self)
        ventana.title("Ingreso Administrador")
        ventana.geometry("320x180")
        ventana.resizable(False, False)
        ventana.configure(bg="white")

        tk.Label(
            ventana,
            text="Ingrese clave de administrador:",
            font=("Arial", 13, "bold"),
            bg="white"
        ).pack(pady=15)

        clave_var = tk.StringVar()

        tk.Entry(
            ventana,
            textvariable=clave_var,
            show="•",
            font=("Arial", 12)
        ).pack(pady=5)

        def validar_clave():
            if clave_var.get() == "admin123":
                ventana.destroy()
                self.ir_admin()
            else:
                messagebox.showerror("Error", "Clave incorrecta")

        tk.Button(
            ventana,
            text="Ingresar",
            font=("Arial", 12, "bold"),
            bg="#4caf50",
            fg="white",
            command=validar_clave
        ).pack(pady=15)

    # ----------------------
    # IR A ADMIN
    # ----------------------
    def ir_admin(self):
        from pantallas.admin import PantallaAdmin
        self.app.mostrar_pantalla("admin")
