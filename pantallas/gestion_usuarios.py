import tkinter as tk
from tkinter import ttk, messagebox


class PantallaGestionUsuarios:

    def __init__(self, master, on_back):
        self.master = master
        self.on_back = on_back

        # LISTA TEMPORAL (más adelante la conectamos a BD si deseas)
        self.usuarios = [
            {"id": 1, "nombre": "Administrador", "rol": "admin"},
            {"id": 2, "nombre": "Invitado", "rol": "usuario"},
        ]

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
            text="Gestión de Usuarios",
            font=("Arial", 22, "bold"),
            bg="#ffffff",
            fg="#2f3640"
        ).place(x=150, y=15)

        # ============================
        #  BOTÓN AGREGAR USUARIO
        # ============================
        tk.Button(
            self.frame,
            text="➕ Agregar Usuario",
            font=("Arial", 12, "bold"),
            bg="#4cd137",
            fg="white",
            relief="flat",
            command=self.agregar_usuario
        ).pack(pady=20)

        # ============================
        #  TABLA DE USUARIOS
        # ============================
        tabla_frame = tk.Frame(self.frame, bg="#f5f6fa")
        tabla_frame.pack()

        columnas = ("ID", "Nombre", "Rol")

        self.tabla = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings",
            height=10
        )

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Rol", text="Rol")

        self.tabla.column("ID", width=80, anchor="center")
        self.tabla.column("Nombre", width=200)
        self.tabla.column("Rol", width=150, anchor="center")

        self.tabla.pack()

        # Botones debajo de tabla
        botones = tk.Frame(self.frame, bg="#f5f6fa")
        botones.pack(pady=15)

        tk.Button(
            botones,
            text="✏ Editar",
            font=("Arial", 11),
            bg="#fbc531",
            command=self.editar_usuario
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            botones,
            text="🗑 Eliminar",
            font=("Arial", 11),
            bg="#e84118",
            fg="white",
            command=self.eliminar_usuario
        ).grid(row=0, column=1, padx=10)

        self.cargar_usuarios()

    # ============================================================
    #  Cargar datos a la tabla
    # ============================================================
    def cargar_usuarios(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        for usuario in self.usuarios:
            self.tabla.insert("", "end", values=(usuario["id"], usuario["nombre"], usuario["rol"]))

    # ============================================================
    #  Agregar usuario
    # ============================================================
    def agregar_usuario(self):
        self.abrir_modal_usuario("Agregar Usuario")

    # ============================================================
    #  Editar usuario seleccionado
    # ============================================================
    def editar_usuario(self):
        item = self.tabla.selection()
        if not item:
            messagebox.showwarning("Aviso", "Seleccione un usuario para editar.")
            return

        datos = self.tabla.item(item)["values"]
        self.abrir_modal_usuario("Editar Usuario", datos)

    # ============================================================
    #  Eliminar usuario
    # ============================================================
    def eliminar_usuario(self):
        item = self.tabla.selection()
        if not item:
            messagebox.showwarning("Aviso", "Seleccione un usuario para eliminar.")
            return

        datos = self.tabla.item(item)["values"]

        confirm = messagebox.askyesno("Confirmar", f"¿Eliminar usuario '{datos[1]}'?")
        if confirm:
            self.usuarios = [u for u in self.usuarios if u["id"] != datos[0]]
            self.cargar_usuarios()

    # ============================================================
    #  Modal para agregar/editar usuario
    # ============================================================
    def abrir_modal_usuario(self, titulo, datos=None):
        modal = tk.Toplevel(self.master)
        modal.title(titulo)
        modal.geometry("350x250")
        modal.resizable(False, False)

        tk.Label(modal, text=titulo, font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(modal, text="Nombre:", font=("Arial", 12)).pack()
        nombre_var = tk.StringVar()
        tk.Entry(modal, textvariable=nombre_var, font=("Arial", 12)).pack(pady=5)

        tk.Label(modal, text="Rol:", font=("Arial", 12)).pack()
        rol_var = tk.StringVar()
        tk.Entry(modal, textvariable=rol_var, font=("Arial", 12)).pack(pady=5)

        if datos:
            nombre_var.set(datos[1])
            rol_var.set(datos[2])

        def guardar():
            nombre = nombre_var.get()
            rol = rol_var.get()

            if not nombre or not rol:
                messagebox.showwarning("Error", "Todos los campos son obligatorios.")
                return

            if datos:
                # Editar
                for u in self.usuarios:
                    if u["id"] == datos[0]:
                        u["nombre"] = nombre
                        u["rol"] = rol
            else:
                # Agregar
                nuevo_id = max([u["id"] for u in self.usuarios]) + 1 if self.usuarios else 1
                self.usuarios.append({"id": nuevo_id, "nombre": nombre, "rol": rol})

            self.cargar_usuarios()
            modal.destroy()

        tk.Button(
            modal,
            text="Guardar",
            font=("Arial", 12, "bold"),
            bg="#44bd32",
            fg="white",
            command=guardar
        ).pack(pady=15)
