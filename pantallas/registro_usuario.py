import tkinter as tk
from tkinter import ttk
import re
from PIL import Image, ImageTk


class PantallaRegistroUsuario:

    def __init__(self, master, app, on_back):
        self.master = master
        self.app = app
        self.on_back = on_back

        if not hasattr(app, "usuarios"):
            app.usuarios = []

        self.frame = tk.Frame(master, bg="#f5f6fa")
        self.frame.pack(fill="both", expand=True)

        # ================================
        # BARRA SUPERIOR
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
            text="Registro de Usuario",
            font=("Arial", 24, "bold"),
            bg="white",
            fg="#2f3640"
        ).place(x=160, y=15)

        # ================================
        # TARJETA FORMULARIO
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

        # ================================
        # ICONO DEL PERFIL
        # ================================
        try:
            img_raw = Image.open("assets/icons/perfil_medico.png")
            img_raw = img_raw.resize((80, 80), Image.LANCZOS)
            self.icono_usuario = ImageTk.PhotoImage(img_raw)

            tk.Label(form, image=self.icono_usuario, bg="white").pack(pady=(0, 10))
        except:
            pass

        # ================================
        # CAMPOS
        # ================================
        campos = [
            ("Nombre completo", "nombre"),
            ("DNI", "dni"),
            ("Edad", "edad"),
            ("Teléfono", "telefono"),
            ("Dirección", "direccion"),
            ("Correo", "correo")
        ]

        self.vars = {}
        self.error_labels = {}

        for etiqueta, campo in campos:
            # Título del campo
            tk.Label(
                form,
                text=f"{etiqueta}:",
                font=("Arial", 12, "bold"),
                bg="white"
            ).pack(anchor="w", pady=(10, 0))

            # Entry
            var = tk.StringVar()
            self.vars[campo] = var
            entry = tk.Entry(
                form,
                textvariable=var,
                font=("Arial", 12),
                width=35,
                relief="solid",
                bd=1
            )
            entry.pack()

            # Etiqueta de error invisible inicialmente
            error_lbl = tk.Label(
                form,
                text="",
                font=("Arial", 10, "italic"),
                fg="#e84118",
                bg="white"
            )
            error_lbl.pack(anchor="w", pady=(2, 0))

            self.error_labels[campo] = error_lbl

        # ================================
        # BOTÓN REGISTRAR
        # ================================
        tk.Button(
            form,
            text="Registrar",
            font=("Arial", 12, "bold"),
            bg="#44bd32",
            fg="white",
            width=20,
            command=self.guardar_usuario
        ).pack(pady=20)

    # ============================================================
    # VALIDACIONES CON ERRORES POR CAMPO
    # ============================================================
    def limpiar_errores(self):
        for lbl in self.error_labels.values():
            lbl.config(text="")

    def mostrar_error(self, campo, mensaje):
        self.error_labels[campo].config(text=mensaje)

    def guardar_usuario(self):
        self.limpiar_errores()
        datos = {campo: var.get().strip() for campo, var in self.vars.items()}
        ok = True

        # -------- Nombre -----------
        if not datos["nombre"]:
            self.mostrar_error("nombre", "Ingrese el nombre completo.")
            ok = False

        # -------- DNI -----------
        if not datos["dni"].isdigit() or len(datos["dni"]) != 8:
            self.mostrar_error("dni", "El DNI debe tener 8 dígitos numéricos.")
            ok = False
        else:
            for u in self.app.usuarios:
                if u["dni"] == datos["dni"]:
                    self.mostrar_error("dni", "Este DNI ya está registrado.")
                    ok = False

        # -------- Edad -----------
        if not datos["edad"].isdigit() or int(datos["edad"]) <= 0:
            self.mostrar_error("edad", "Ingrese una edad válida.")
            ok = False

        # -------- Teléfono -----------
        if not datos["telefono"].isdigit() or len(datos["telefono"]) != 9:
            self.mostrar_error("telefono", "El teléfono debe tener 9 dígitos.")
            ok = False

        # -------- Dirección --------
        if not datos["direccion"]:
            self.mostrar_error("direccion", "La dirección es obligatoria.")
            ok = False

        # -------- Correo -----------
        patron_correo = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(patron_correo, datos["correo"]):
            self.mostrar_error("correo", "Correo electrónico inválido.")
            ok = False

        # -------- FINAL --------
        if not ok:
            return  # Hay errores → no guardar

        # Guardar usuario
        self.app.usuarios.append(datos)
        self.on_back()
