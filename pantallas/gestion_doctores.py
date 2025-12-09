import tkinter as tk
from tkinter import ttk, messagebox


class PantallaGestionDoctores:

    def __init__(self, master, on_back):
        self.master = master
        self.on_back = on_back

        # =======================================
        #   LISTA TEMPORAL DE DOCTORES
        # =======================================
        self.doctores = [
            {"id": 1, "nombre": "Dr. Carlos Pérez", "especialidad": "General", "turno": "Mañana"},
            {"id": 2, "nombre": "Dra. Ana Torres", "especialidad": "Pediatría", "turno": "Tarde"},
        ]

        # =======================================
        #   CONTENEDOR PRINCIPAL
        # =======================================
        self.frame = tk.Frame(master, bg="#f5f6fa")
        self.frame.pack(fill="both", expand=True)

        # =======================================
        #   BARRA SUPERIOR
        # =======================================
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
            text="Gestión de Doctores (Turnos)",
            font=("Arial", 22, "bold"),
            bg="#ffffff",
            fg="#2f3640"
        ).place(x=150, y=15)

        # =======================================
        #   BOTÓN AGREGAR DOCTOR
        # =======================================
        tk.Button(
            self.frame,
            text="➕ Agregar Doctor",
            font=("Arial", 12, "bold"),
            bg="#4cd137",
            fg="white",
            relief="flat",
            command=self.agregar_doctor
        ).pack(pady=20)

        # =======================================
        #   TABLA DE DOCTORES
        # =======================================
        tabla_frame = tk.Frame(self.frame)
        tabla_frame.pack()

        columnas = ("ID", "Nombre", "Especialidad", "Turno")
        self.tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings", height=12)

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Especialidad", text="Especialidad")
        self.tabla.heading("Turno", text="Turno")

        self.tabla.column("ID", width=70, anchor="center")
        self.tabla.column("Nombre", width=220)
        self.tabla.column("Especialidad", width=180)
        self.tabla.column("Turno", width=130, anchor="center")

        self.tabla.pack()

        # =======================================
        #   BOTONES DE ACCIÓN
        # =======================================
        botones = tk.Frame(self.frame, bg="#f5f6fa")
        botones.pack(pady=15)

        tk.Button(
            botones,
            text="✏ Editar",
            font=("Arial", 11),
            bg="#fbc531",
            command=self.editar_doctor
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            botones,
            text="🗑 Eliminar",
            font=("Arial", 11),
            bg="#e84118",
            fg="white",
            command=self.eliminar_doctor
        ).grid(row=0, column=1, padx=10)

        self.cargar_doctores()

    # ===========================================
    #   Cargar datos a la tabla
    # ===========================================
    def cargar_doctores(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for doc in self.doctores:
            self.tabla.insert("", "end", values=(doc["id"], doc["nombre"], doc["especialidad"], doc["turno"]))

    # ===========================================
    #   Abrir modal para agregar doctor
    # ===========================================
    def agregar_doctor(self):
        self.abrir_modal_doctor("Agregar Doctor")

    # ===========================================
    #   Abrir modal para editar doctor
    # ===========================================
    def editar_doctor(self):
        item = self.tabla.selection()
        if not item:
            messagebox.showwarning("Error", "Seleccione un doctor para editar.")
            return

        datos = self.tabla.item(item)["values"]
        self.abrir_modal_doctor("Editar Doctor", datos)

    # ===========================================
    #   Eliminar doctor
    # ===========================================
    def eliminar_doctor(self):
        item = self.tabla.selection()
        if not item:
            messagebox.showwarning("Error", "Seleccione un doctor para eliminar.")
            return

        datos = self.tabla.item(item)["values"]
        nombre = datos[1]

        if messagebox.askyesno("Confirmar", f"¿Eliminar al doctor {nombre}?"):
            self.doctores = [d for d in self.doctores if d["id"] != datos[0]]
            self.cargar_doctores()

    # ===========================================
    #   Modal de registro/edición
    # ===========================================
    def abrir_modal_doctor(self, titulo, datos=None):
        modal = tk.Toplevel(self.master)
        modal.title(titulo)
        modal.geometry("370x320")
        modal.resizable(False, False)

        tk.Label(modal, text=titulo, font=("Arial", 14, "bold")).pack(pady=10)

        # Campo nombre
        tk.Label(modal, text="Nombre:", font=("Arial", 12)).pack()
        nombre_var = tk.StringVar()
        tk.Entry(modal, textvariable=nombre_var, font=("Arial", 12)).pack(pady=5)

        # Campo especialidad
        tk.Label(modal, text="Especialidad:", font=("Arial", 12)).pack()
        espec_var = tk.StringVar()
        tk.Entry(modal, textvariable=espec_var, font=("Arial", 12)).pack(pady=5)

        # Turno
        tk.Label(modal, text="Turno:", font=("Arial", 12)).pack()
        turno_var = tk.StringVar()
        turno_select = ttk.Combobox(
            modal,
            textvariable=turno_var,
            values=["Mañana", "Tarde", "Noche"],
            state="readonly",
            font=("Arial", 12)
        )
        turno_select.pack(pady=5)

        # Si está editando, cargar datos
        if datos:
            nombre_var.set(datos[1])
            espec_var.set(datos[2])
            turno_var.set(datos[3])

        def guardar():
            if not nombre_var.get() or not espec_var.get() or not turno_var.get():
                messagebox.showwarning("Error", "Todos los campos son obligatorios.")
                return

            if datos:
                # EDITAR
                for d in self.doctores:
                    if d["id"] == datos[0]:
                        d["nombre"] = nombre_var.get()
                        d["especialidad"] = espec_var.get()
                        d["turno"] = turno_var.get()

            else:
                # AGREGAR
                nuevo_id = max([d["id"] for d in self.doctores]) + 1 if self.doctores else 1
                self.doctores.append({
                    "id": nuevo_id,
                    "nombre": nombre_var.get(),
                    "especialidad": espec_var.get(),
                    "turno": turno_var.get()
                })

            self.cargar_doctores()
            modal.destroy()

        tk.Button(
            modal,
            text="Guardar",
            font=("Arial", 12, "bold"),
            bg="#44bd32",
            fg="white",
            command=guardar
        ).pack(pady=15)
