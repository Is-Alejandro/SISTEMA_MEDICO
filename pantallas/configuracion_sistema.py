import tkinter as tk
from tkinter import ttk, messagebox


class PantallaConfiguracionSistema:

    def __init__(self, master, on_back):
        self.master = master
        self.on_back = on_back

        # ============================
        #  CONTENEDOR PRINCIPAL
        # ============================
        self.frame = tk.Frame(master, bg="#f5f6fa")
        self.frame.pack(fill="both", expand=True)

        # ============================
        #  BARRA SUPERIOR
        # ============================
        barra = tk.Frame(self.frame, bg="#ffffff", height=70)
        barra.pack(fill="x")

        tk.Button(
            barra,
            text="⬅ Volver",
            font=("Arial", 11, "bold"),
            bg="#dcdde1",
            relief="solid",
            bd=1,
            command=self.on_back
        ).place(x=20, y=20)

        tk.Label(
            barra,
            text="Configuración del Sistema",
            font=("Arial", 22, "bold"),
            bg="#ffffff",
            fg="#2f3640"
        ).place(x=150, y=15)

        # ============================
        #  CUADRO CENTRAL
        # ============================
        card = tk.Frame(
            self.frame,
            bg="white",
            bd=1,
            relief="solid",
            padx=40,
            pady=30
        )
        card.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            card,
            text="Ajustes Generales",
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#273c75"
        ).pack(pady=(0, 20))

        # ============================
        #  OPCIONES DE CONFIGURACIÓN
        # ============================

        # CAMBIAR CLAVE ADMIN
        btn_clave = tk.Button(
            card,
            text="🔑 Cambiar Clave de Administrador",
            font=("Arial", 13),
            bg="#dcdde1",
            relief="ridge",
            width=35,
            command=self.cambiar_clave_admin
        )
        btn_clave.pack(pady=10)

        # TEMA CLARO/OSCURO
        btn_tema = tk.Button(
            card,
            text="🎨 Cambiar Tema (Claro / Oscuro)",
            font=("Arial", 13),
            bg="#dcdde1",
            relief="ridge",
            width=35,
            command=self.no_implementado
        )
        btn_tema.pack(pady=10)

        # ACTIVAR/DESACTIVAR MÓDULOS
        btn_modulos = tk.Button(
            card,
            text="🧩 Activar / Desactivar Módulos",
            font=("Arial", 13),
            bg="#dcdde1",
            relief="ridge",
            width=35,
            command=self.no_implementado
        )
        btn_modulos.pack(pady=10)

        # INFORMACIÓN DEL SISTEMA
        btn_info = tk.Button(
            card,
            text="💻 Información del Sistema",
            font=("Arial", 13),
            bg="#dcdde1",
            relief="ridge",
            width=35,
            command=self.no_implementado
        )
        btn_info.pack(pady=10)

    # =================================================
    #   CAMBIAR CLAVE DEL ADMINISTRADOR
    # =================================================
    def cambiar_clave_admin(self):
        modal = tk.Toplevel(self.master)
        modal.title("Cambiar Clave de Administrador")
        modal.geometry("350x230")
        modal.resizable(False, False)

        tk.Label(
            modal,
            text="Cambiar Clave del Administrador",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        tk.Label(modal, text="Nueva clave:", font=("Arial", 12)).pack()
        clave_var = tk.StringVar()
        tk.Entry(modal, textvariable=clave_var, font=("Arial", 12), show="•").pack(pady=5)

        tk.Label(modal, text="Confirmar clave:", font=("Arial", 12)).pack()
        clave_confirm = tk.StringVar()
        tk.Entry(modal, textvariable=clave_confirm, font=("Arial", 12), show="•").pack(pady=5)

        def guardar():
            if not clave_var.get() or not clave_confirm.get():
                messagebox.showwarning("Error", "Todos los campos son obligatorios.")
                return

            if clave_var.get() != clave_confirm.get():
                messagebox.showwarning("Error", "Las claves no coinciden.")
                return

            # Aquí puedes guardar en archivo, BD o variable global
            messagebox.showinfo("Éxito", "Clave actualizada correctamente.")
            modal.destroy()

        tk.Button(
            modal,
            text="Guardar",
            font=("Arial", 12, "bold"),
            bg="#44bd32",
            fg="white",
            command=guardar
        ).pack(pady=15)

    # =================================================
    #   FUNCIONES NO IMPLEMENTADAS AÚN
    # =================================================
    def no_implementado(self):
        messagebox.showinfo("En desarrollo", "Esta función estará disponible pronto.")
