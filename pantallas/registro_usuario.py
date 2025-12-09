import tkinter as tk
from tkinter import ttk, messagebox


class PantallaRegistroUsuario:

    def __init__(self, master, app, on_back):
        self.master = master
        self.app = app
        self.on_back = on_back

        # Lista global temporal de usuarios registrados
        if not hasattr(app, "usuarios"):
            app.usuarios = []

        self.frame = tk.Frame(master, bg="#f5f6fa")
        self.frame.pack(fill="both", expand=True)

        # BARRA SUPERIOR
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
            font=("Arial", 22, "bold"),
            bg="white",
            fg="#2f3640"
        ).place(x=160, y=15)

        # FORMULARIO
        form = tk.Frame(self.frame, bg="white", padx=30, pady=30, bd=1, relief="solid")
        form.place(relx=0.5, rely=0.5, anchor="center")

        campos = [
            ("Nombre completo", "nombre"),
            ("DNI", "dni"),
            ("Edad", "edad"),
            ("Teléfono", "telefono"),
            ("Dirección", "direccion"),
            ("Correo", "correo")
        ]

        self.vars = {}
        for etiqueta, campo in campos:
            tk.Label(form, text=etiqueta + ":", bg="white", font=("Arial", 12, "bold")).pack(anchor="w", pady=(10, 0))
            var = tk.StringVar()
            self.vars[campo] = var
            tk.Entry(form, textvariable=var, font=("Arial", 12), width=35).pack()

        tk.Button(
            form,
            text="Registrar",
            font=("Arial", 12, "bold"),
            bg="#44bd32",
            fg="white",
            width=20,
            command=self.guardar_usuario
        ).pack(pady=20)

    def guardar_usuario(self):
        datos = {campo: var.get() for campo, var in self.vars.items()}

        # Validaciones
        if not datos["nombre"] or not datos["dni"]:
            messagebox.showwarning("Error", "Nombre y DNI son obligatorios.")
            return
        
        # Guardamos usuario
        self.app.usuarios.append(datos)
        messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
        self.on_back()
