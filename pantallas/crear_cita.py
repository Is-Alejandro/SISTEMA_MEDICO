import tkinter as tk
from tkinter import ttk, messagebox
import datetime


class PantallaCrearCita:

    def __init__(self, master, app, on_back):
        self.master = master
        self.app = app
        self.on_back = on_back

        # Crear listas globales si no existen
        if not hasattr(app, "usuarios"):
            app.usuarios = []
        if not hasattr(app, "doctores"):
            app.doctores = []
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
            text="Crear Cita Médica",
            font=("Arial", 22, "bold"),
            bg="white",
            fg="#2f3640"
        ).place(x=160, y=15)

        # ================================
        #  TARJETA FORMULARIO
        # ================================
        form = tk.Frame(
            self.frame,
            bg="white",
            padx=40,
            pady=35,
            bd=1,
            relief="solid"
        )
        form.place(relx=0.5, rely=0.52, anchor="center")

        # Etiqueta de error general
        self.error_label = tk.Label(
            form,
            text="",
            fg="#e84118",
            bg="white",
            font=("Arial", 11, "bold")
        )
        self.error_label.pack(pady=(0, 10))

        # ----------------------------------------------------------
        # FUNCIÓN PARA CREAR CAMPOS CON PLACEHOLDER
        # ----------------------------------------------------------
        def crear_entry_placeholder(parent, var, placeholder):
            entry = tk.Entry(
                parent,
                textvariable=var,
                font=("Arial", 12),
                width=35,
                relief="solid",
                bd=1,
                fg="#7f8c8d"
            )
            entry.insert(0, placeholder)

            def on_focus_in(event):
                if entry.get() == placeholder:
                    entry.delete(0, "end")
                    entry.config(fg="#2c3e50")

            def on_focus_out(event):
                if entry.get().strip() == "":
                    entry.insert(0, placeholder)
                    entry.config(fg="#7f8c8d")

            entry.bind("<FocusIn>", on_focus_in)
            entry.bind("<FocusOut>", on_focus_out)

            return entry

        # =======================
        #  USUARIO
        # =======================
        tk.Label(form, text="Usuario:", font=("Arial", 12, "bold"), bg="white").pack(anchor="w")
        self.usuario_var = tk.StringVar()

        usuarios_nombres = [u["nombre"] for u in self.app.usuarios]
        self.usuario_select = ttk.Combobox(
            form, textvariable=self.usuario_var,
            values=usuarios_nombres, state="readonly"
        )
        self.usuario_select.set("Seleccione un usuario...")
        self.usuario_select.pack(pady=5)

        # =======================
        #  DOCTOR
        # =======================
        tk.Label(form, text="Doctor:", font=("Arial", 12, "bold"), bg="white").pack(anchor="w")
        self.doctor_var = tk.StringVar()

        doctores_nombres = [d["nombre"] for d in self.app.doctores]
        self.doctor_select = ttk.Combobox(
            form, textvariable=self.doctor_var,
            values=doctores_nombres, state="readonly"
        )
        self.doctor_select.set("Seleccione un doctor...")
        self.doctor_select.pack(pady=5)

        self.doctor_select.bind("<<ComboboxSelected>>", self.actualizar_info_doctor)

        # =======================
        #  ESPECIALIDAD Y TURNO
        # =======================
        self.lbl_especialidad = tk.Label(form, text="Especialidad: -", bg="white", font=("Arial", 11))
        self.lbl_especialidad.pack(anchor="w", pady=(5, 0))

        self.lbl_turno = tk.Label(form, text="Turno: -", bg="white", font=("Arial", 11))
        self.lbl_turno.pack(anchor="w")

        # =======================
        #  FECHA
        # =======================
        tk.Label(form, text="Fecha (AAAA-MM-DD):", font=("Arial", 12, "bold"), bg="white").pack(anchor="w", pady=(10, 0))
        self.fecha_var = tk.StringVar()
        crear_entry_placeholder(form, self.fecha_var, "Ejemplo: 2025-01-20").pack(pady=5)

        # =======================
        #  HORA
        # =======================
        tk.Label(form, text="Hora:", font=("Arial", 12, "bold"), bg="white").pack(anchor="w")
        self.hora_var = tk.StringVar()

        self.hora_select = ttk.Combobox(
            form, textvariable=self.hora_var,
            state="readonly"
        )
        self.hora_select.set("Seleccione una hora...")
        self.hora_select.pack(pady=5)

        # =======================
        #  MOTIVO
        # =======================
        tk.Label(form, text="Motivo de la consulta:", font=("Arial", 12, "bold"), bg="white").pack(anchor="w", pady=(10, 0))
        self.motivo_var = tk.StringVar()
        crear_entry_placeholder(form, self.motivo_var, "Describa brevemente el motivo...").pack(pady=5)

        # =======================
        #  DIAGNÓSTICO
        # =======================
        tk.Label(form, text="Diagnóstico preliminar:", font=("Arial", 12, "bold"), bg="white").pack(anchor="w", pady=(10, 0))
        self.diagnostico_var = tk.StringVar()
        crear_entry_placeholder(form, self.diagnostico_var, "Opcional...").pack(pady=5)

        # =======================
        #  BOTÓN GUARDAR
        # =======================
        tk.Button(
            form,
            text="Guardar Cita",
            font=("Arial", 13, "bold"),
            bg="#44bd32",
            fg="white",
            pady=5,
            width=20,
            command=self.guardar_cita
        ).pack(pady=20)

    # =================================================================
    #   ACTUALIZAR INFO DEL DOCTOR SELECCIONADO
    # =================================================================
    def actualizar_info_doctor(self, event):
        nombre = self.doctor_var.get()

        for d in self.app.doctores:
            if d["nombre"] == nombre:
                self.lbl_especialidad.config(text=f"Especialidad: {d['especialidad']}")
                self.lbl_turno.config(text=f"Turno: {d['turno']}")
                self.cargar_horas_turno(d["turno"])
                break

    # =================================================================
    #   HORARIOS POR TURNO
    # =================================================================
    def cargar_horas_turno(self, turno):
        if turno == "Mañana":
            horas = ["08:00", "09:00", "10:00", "11:00"]
        elif turno == "Tarde":
            horas = ["14:00", "15:00", "16:00", "17:00"]
        elif turno == "Noche":
            horas = ["18:00", "19:00", "20:00", "21:00"]
        else:
            horas = []

        self.hora_select["values"] = horas
        self.hora_select.set("Seleccione una hora...")

    # =================================================================
    #   GUARDAR CITA
    # =================================================================
    def guardar_cita(self):
        self.error_label.config(text="")

        if self.usuario_var.get().startswith("Seleccione"):
            self.error_label.config(text="Debe seleccionar un usuario.")
            return

        if self.doctor_var.get().startswith("Seleccione"):
            self.error_label.config(text="Debe seleccionar un doctor.")
            return

        if self.hora_var.get().startswith("Seleccione"):
            self.error_label.config(text="Debe seleccionar una hora.")
            return

        cita = {
            "usuario": self.usuario_var.get(),
            "doctor": self.doctor_var.get(),
            "especialidad": self.lbl_especialidad.cget("text").replace("Especialidad: ", ""),
            "turno": self.lbl_turno.cget("text").replace("Turno: ", ""),
            "fecha": self.fecha_var.get(),
            "hora": self.hora_var.get(),
            "motivo": self.motivo_var.get(),
            "diagnostico": self.diagnostico_var.get()
        }

        self.app.citas.append(cita)
        messagebox.showinfo("Éxito", "Cita registrada correctamente.")
        self.on_back()
