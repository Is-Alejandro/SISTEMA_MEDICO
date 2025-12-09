import tkinter as tk
from tkinter import ttk, messagebox


class PantallaVerCitas:

    def __init__(self, master, app, on_back):
        self.master = master
        self.app = app
        self.on_back = on_back

        if not hasattr(app, "citas"):
            app.citas = []

        # ================================
        #  CONTENEDOR PRINCIPAL
        # ================================
        self.frame = tk.Frame(master, bg="#f5f6fa")
        self.frame.pack(fill="both", expand=True)

        # ================================
        #  BARRA SUPERIOR
        # ================================
        barra = tk.Frame(self.frame, bg="white", height=70)
        barra.pack(fill="x")

        tk.Button(
            barra,
            text="⬅ Volver",
            bg="#dcdde1",
            font=("Arial", 11, "bold"),
            command=self.on_back
        ).place(x=20, y=20)

        tk.Label(
            barra,
            text="Citas Registradas",
            font=("Arial", 22, "bold"),
            bg="white",
            fg="#2f3640"
        ).place(x=170, y=15)

        # ================================
        #  FILTRO POR USUARIO
        # ================================
        filtro_frame = tk.Frame(self.frame, bg="#f5f6fa")
        filtro_frame.pack(pady=15)

        tk.Label(
            filtro_frame,
            text="Filtrar por usuario:",
            font=("Arial", 12, "bold"),
            bg="#f5f6fa"
        ).grid(row=0, column=0, padx=5)

        self.filtro_var = tk.StringVar()
        self.filtro_entry = tk.Entry(filtro_frame, textvariable=self.filtro_var, font=("Arial", 12))
        self.filtro_entry.grid(row=0, column=1, padx=5)

        tk.Button(
            filtro_frame,
            text="Buscar",
            font=("Arial", 12),
            bg="#00a8ff",
            fg="white",
            command=self.filtrar_citas
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            filtro_frame,
            text="Quitar Filtro",
            font=("Arial", 12),
            bg="#e1b12c",
            fg="white",
            command=self.cargar_citas
        ).grid(row=0, column=3, padx=5)

        # ================================
        #  TABLA DE CITAS
        # ================================
        tabla_frame = tk.Frame(self.frame)
        tabla_frame.pack()

        columnas = ("Usuario", "Doctor", "Especialidad", "Fecha", "Hora", "Motivo")
        self.tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings", height=12)

        for col in columnas:
            self.tabla.heading(col, text=col)

        self.tabla.column("Usuario", width=180)
        self.tabla.column("Doctor", width=180)
        self.tabla.column("Especialidad", width=150)
        self.tabla.column("Fecha", width=100)
        self.tabla.column("Hora", width=80)
        self.tabla.column("Motivo", width=250)

        self.tabla.pack()

        # ================================
        #  BOTONES DE ACCIÓN
        # ================================
        botones = tk.Frame(self.frame, bg="#f5f6fa")
        botones.pack(pady=10)

        tk.Button(
            botones,
            text="ℹ Ver Detalles",
            font=("Arial", 11),
            bg="#8c7ae6",
            fg="white",
            command=self.ver_detalles
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            botones,
            text="✏ Editar",
            font=("Arial", 11),
            bg="#fbc531",
            command=self.editar_cita
        ).grid(row=0, column=1, padx=10)

        tk.Button(
            botones,
            text="🗑 Eliminar",
            font=("Arial", 11),
            bg="#e84118",
            fg="white",
            command=self.eliminar_cita
        ).grid(row=0, column=2, padx=10)

        # Cargar citas
        self.cargar_citas()

    # ============================================================
    #   CARGAR CITAS
    # ============================================================
    def cargar_citas(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for c in self.app.citas:
            self.tabla.insert("", "end", values=(
                c["usuario"], c["doctor"], c["especialidad"],
                c["fecha"], c["hora"], c["motivo"]
            ))

    # ============================================================
    #   FILTRAR CITAS POR USUARIO
    # ============================================================
    def filtrar_citas(self):
        filtro = self.filtro_var.get().strip().lower()

        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for c in self.app.citas:
            if filtro in c["usuario"].lower():
                self.tabla.insert("", "end", values=(
                    c["usuario"], c["doctor"], c["especialidad"],
                    c["fecha"], c["hora"], c["motivo"]
                ))

    # ============================================================
    #   VER DETALLES DE UNA CITA
    # ============================================================
    def ver_detalles(self):
        item = self.tabla.selection()
        if not item:
            messagebox.showwarning("Error", "Seleccione una cita.")
            return

        datos = self.tabla.item(item)["values"]

        cita = next(c for c in self.app.citas if c["usuario"] == datos[0] and 
                    c["fecha"] == datos[3] and c["hora"] == datos[4])

        modal = tk.Toplevel(self.master)
        modal.title("Detalles de la Cita")
        modal.geometry("400x350")
        modal.resizable(False, False)

        info = f"""
Usuario: {cita['usuario']}
Doctor: {cita['doctor']}
Especialidad: {cita['especialidad']}

Fecha: {cita['fecha']}
Hora: {cita['hora']}

Motivo:
{cita['motivo']}

Diagnóstico preliminar:
{cita['diagnostico']}
"""

        tk.Label(modal, text=info, justify="left", font=("Arial", 12)).pack(padx=20, pady=20)

    # ============================================================
    #   ELIMINAR CITA
    # ============================================================
    def eliminar_cita(self):
        item = self.tabla.selection()
        if not item:
            messagebox.showwarning("Error", "Seleccione una cita.")
            return

        datos = self.tabla.item(item)["values"]
        usuario, fecha, hora = datos[0], datos[3], datos[4]

        if messagebox.askyesno("Confirmar", "¿Eliminar esta cita?"):
            self.app.citas = [
                c for c in self.app.citas
                if not (c["usuario"] == usuario and c["fecha"] == fecha and c["hora"] == hora)
            ]
            self.cargar_citas()

    # ============================================================
    #   EDITAR CITA
    # ============================================================
    def editar_cita(self):
        messagebox.showinfo("En desarrollo", "La edición de citas estará disponible pronto.")
