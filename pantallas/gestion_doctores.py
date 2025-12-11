import tkinter as tk
from tkinter import ttk, messagebox


class PantallaGestionDoctores:

    def __init__(self, master, app, on_back):
        self.master = master
        self.app = app
        self.on_back = on_back

        # Crear lista global si no existe
        if not hasattr(self.app, "doctores"):
            self.app.doctores = []

        # Si está vacía, cargar doctores iniciales
        if len(self.app.doctores) == 0:
            self.app.doctores.extend([
                {"id": 1, "nombre": "Dr. Carlos Pérez", "especialidad": "General", "turno": "Mañana"},
                {"id": 2, "nombre": "Dra. Ana Torres", "especialidad": "Pediatría", "turno": "Tarde"},
            ])

        # ============================
        # CONTENEDOR PRINCIPAL
        # ============================
        self.frame = tk.Frame(master, bg="#f5f6fa")
        self.frame.pack(fill="both", expand=True)

        # ============================
        # BARRA SUPERIOR
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
            text="Gestión de Doctores (Turnos)",
            font=("Arial", 22, "bold"),
            bg="#ffffff",
            fg="#2f3640"
        ).place(x=150, y=15)

        # ============================
        # BOTÓN AGREGAR
        # ============================
        tk.Button(
            self.frame,
            text="➕ Agregar Doctor",
            font=("Arial", 12, "bold"),
            bg="#4cd137",
            fg="white",
            relief="flat",
            command=self.agregar_doctor
        ).pack(pady=20)

        # ============================
        # TABLA
        # ============================
        tabla_frame = tk.Frame(self.frame)
        tabla_frame.pack()

        columnas = ("ID", "Nombre", "Especialidad", "Turno")
        self.tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings", height=12)

        for col in columnas:
            self.tabla.heading(col, text=col)

        self.tabla.column("ID", width=70, anchor="center")
        self.tabla.column("Nombre", width=220)
        self.tabla.column("Especialidad", width=180)
        self.tabla.column("Turno", width=130, anchor="center")

        self.tabla.pack()

        # BOTONES
        botones = tk.Frame(self.frame, bg="#f5f6fa")
        botones.pack(pady=15)

        tk.Button(botones, text="✏ Editar", bg="#fbc531", font=("Arial", 11),
                  command=self.editar_doctor).grid(row=0, column=0, padx=10)

        tk.Button(botones, text="🗑 Eliminar", bg="#e84118", fg="white", font=("Arial", 11),
                  command=self.eliminar_doctor).grid(row=0, column=1, padx=10)

        self.cargar_doctores()

    # ============================
    def cargar_doctores(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for doc in self.app.doctores:
            self.tabla.insert("", "end",
                              values=(doc["id"], doc["nombre"], doc["especialidad"], doc["turno"]))

    # ============================
    def agregar_doctor(self):
        self.abrir_modal("Agregar Doctor")

    def editar_doctor(self):
        item = self.tabla.selection()
        if not item:
            messagebox.showwarning("Error", "Seleccione un doctor.")
            return

        datos = self.tabla.item(item)["values"]
        self.abrir_modal("Editar Doctor", datos)

    # ============================
    def eliminar_doctor(self):
        item = self.tabla.selection()
        if not item:
            messagebox.showwarning("Error", "Seleccione un doctor.")
            return

        datos = self.tabla.item(item)["values"]

        if messagebox.askyesno("Confirmar", f"¿Eliminar al doctor {datos[1]}?"):
            self.app.doctores = [d for d in self.app.doctores if d["id"] != datos[0]]

        self.cargar_doctores()

    # ============================
    def abrir_modal(self, titulo, datos=None):
        modal = tk.Toplevel(self.master)
        modal.title(titulo)
        modal.geometry("370x320")
        modal.resizable(False, False)

        tk.Label(modal, text=titulo, font=("Arial", 14, "bold")).pack(pady=10)

        nombre = tk.StringVar()
        espec = tk.StringVar()
        turno = tk.StringVar()

        tk.Label(modal, text="Nombre:", font=("Arial", 12)).pack()
        tk.Entry(modal, textvariable=nombre, font=("Arial", 12)).pack(pady=5)

        tk.Label(modal, text="Especialidad:", font=("Arial", 12)).pack()
        tk.Entry(modal, textvariable=espec, font=("Arial", 12)).pack(pady=5)

        tk.Label(modal, text="Turno:", font=("Arial", 12)).pack()
        ttk.Combobox(modal, textvariable=turno,
                     values=["Mañana", "Tarde", "Noche"],
                     state="readonly", font=("Arial", 12)).pack(pady=5)

        # Cargar datos si edita
        if datos:
            nombre.set(datos[1])
            espec.set(datos[2])
            turno.set(datos[3])

        def guardar():
            if not nombre.get() or not espec.get() or not turno.get():
                messagebox.showwarning("Error", "Todos los campos son obligatorios.")
                return

            if datos:
                for d in self.app.doctores:
                    if d["id"] == datos[0]:
                        d["nombre"] = nombre.get().strip()
                        d["especialidad"] = espec.get().strip()
                        d["turno"] = turno.get().strip()
            else:
                nuevo_id = max([d["id"] for d in self.app.doctores]) + 1
                self.app.doctores.append({
                    "id": nuevo_id,
                    "nombre": nombre.get().strip(),
                    "especialidad": espec.get().strip(),
                    "turno": turno.get().strip()
                })

            self.cargar_doctores()
            modal.destroy()

        tk.Button(modal, text="Guardar", font=("Arial", 12, "bold"),
                  bg="#44bd32", fg="white", command=guardar).pack(pady=15)
