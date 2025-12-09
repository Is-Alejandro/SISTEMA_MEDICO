import tkinter as tk
from tkinter import ttk, messagebox


class PantallaAdmin:

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
            text="Módulo Administrador",
            font=("Arial", 22, "bold"),
            bg="#ffffff",
            fg="#2f3640"
        ).place(x=130, y=15)

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
            text="Opciones de Administración",
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#273c75"
        ).pack(pady=(0, 20))

        # ============================
        #  GRID DE OPCIONES
        # ============================
        opciones = [
            ("👤", "Gestionar Usuarios", self.abrir_gestion_usuarios),
            ("⚙️", "Configuración del Sistema", self.abrir_configuracion_sistema),
            ("📄", "Ver Registros (Logs)", self.abrir_logs_sistema),
            ("🩺", "Gestionar Doctores (Turnos)", self.abrir_gestion_doctores)
        ]

        grid = tk.Frame(card, bg="white")
        grid.pack()

        fila = 0
        col = 0

        for icono, texto, accion in opciones:

            card_opcion = tk.Frame(
                grid,
                bg="#f0f0f0",
                relief="ridge",
                bd=2,
                width=220,
                height=120
            )
            card_opcion.grid(row=fila, column=col, padx=15, pady=15)
            card_opcion.grid_propagate(False)

            lbl_icono = tk.Label(
                card_opcion,
                text=icono,
                font=("Arial", 35),
                bg="#f0f0f0"
            )
            lbl_icono.pack(pady=(10, 0))

            lbl_texto = tk.Label(
                card_opcion,
                text=texto,
                font=("Arial", 13, "bold"),
                bg="#f0f0f0"
            )
            lbl_texto.pack(pady=(5, 0))

            card_opcion.bind("<Button-1>", lambda e, f=accion: f())
            lbl_icono.bind("<Button-1>", lambda e, f=accion: f())
            lbl_texto.bind("<Button-1>", lambda e, f=accion: f())

            col += 1
            if col == 2:
                col = 0
                fila += 1

    # =================================================
    #  ABRIR GESTIÓN DE USUARIOS
    # =================================================
    def abrir_gestion_usuarios(self):
        from pantallas.gestion_usuarios import PantallaGestionUsuarios
        self.frame.destroy()
        PantallaGestionUsuarios(self.master, self.on_back)

    # =================================================
    #  ABRIR CONFIGURACIÓN DEL SISTEMA
    # =================================================
    def abrir_configuracion_sistema(self):
        from pantallas.configuracion_sistema import PantallaConfiguracionSistema
        self.frame.destroy()
        PantallaConfiguracionSistema(self.master, self.on_back)

    # =================================================
    #  ABRIR LOGS DEL SISTEMA
    # =================================================
    def abrir_logs_sistema(self):
        from pantallas.logs_sistema import PantallaLogsSistema
        self.frame.destroy()
        PantallaLogsSistema(self.master, self.on_back)

    # =================================================
    #  ABRIR GESTIÓN DE DOCTORES
    # =================================================
    def abrir_gestion_doctores(self):
        from pantallas.gestion_doctores import PantallaGestionDoctores
        self.frame.destroy()
        PantallaGestionDoctores(self.master, self.on_back)

    # =================================================
    #  FUNCIÓN DE PLACEHOLDER
    # =================================================
    def no_implementado(self):
        messagebox.showinfo(
            "En desarrollo",
            "Esta función aún no está implementada."
        )
