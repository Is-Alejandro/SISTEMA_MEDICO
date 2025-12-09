import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import datetime


class PantallaLogsSistema:

    def __init__(self, master, on_back):
        self.master = master
        self.on_back = on_back

        # ============================
        #   LOGS SIMULADOS
        # ============================
        self.logs = [
            {"fecha": "2025-01-01 10:00", "tipo": "INFO", "mensaje": "Sistema iniciado correctamente."},
            {"fecha": "2025-01-01 10:05", "tipo": "WARNING", "mensaje": "Conexión lenta detectada."},
            {"fecha": "2025-01-01 10:10", "tipo": "ERROR", "mensaje": "No se pudo cargar el módulo IMC."},
        ]

        # ============================
        #   CONTENEDOR PRINCIPAL
        # ============================
        self.frame = tk.Frame(master, bg="#f5f6fa")
        self.frame.pack(fill="both", expand=True)

        # ============================
        #   BARRA SUPERIOR
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
            text="Registros del Sistema (Logs)",
            font=("Arial", 22, "bold"),
            bg="#ffffff",
            fg="#2f3640"
        ).place(x=150, y=15)

        # ============================
        #   BOTONES DE ACCIÓN
        # ============================
        botones = tk.Frame(self.frame, bg="#f5f6fa")
        botones.pack(pady=20)

        tk.Button(
            botones,
            text="🧹 Limpiar Logs",
            font=("Arial", 12, "bold"),
            bg="#e84118",
            fg="white",
            width=15,
            command=self.limpiar_logs
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            botones,
            text="💾 Exportar Logs",
            font=("Arial", 12, "bold"),
            bg="#00a8ff",
            fg="white",
            width=15,
            command=self.exportar_logs
        ).grid(row=0, column=1, padx=10)

        # ============================
        #   TABLA DE LOGS
        # ============================
        tabla_frame = tk.Frame(self.frame)
        tabla_frame.pack(pady=10)

        columnas = ("Fecha", "Tipo", "Mensaje")
        self.tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings", height=12)

        self.tabla.heading("Fecha", text="Fecha")
        self.tabla.heading("Tipo", text="Tipo")
        self.tabla.heading("Mensaje", text="Mensaje")

        self.tabla.column("Fecha", width=170)
        self.tabla.column("Tipo", width=100, anchor="center")
        self.tabla.column("Mensaje", width=500)

        self.tabla.pack()

        self.cargar_logs()

    # ============================================================
    #   CARGAR LOGS EN LA TABLA
    # ============================================================
    def cargar_logs(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for log in self.logs:
            self.tabla.insert("", "end", values=(log["fecha"], log["tipo"], log["mensaje"]))

    # ============================================================
    #   LIMPIAR LOGS
    # ============================================================
    def limpiar_logs(self):
        if messagebox.askyesno("Confirmar", "¿Desea eliminar todos los registros?"):
            self.logs = []
            self.cargar_logs()
            messagebox.showinfo("Éxito", "Los registros han sido eliminados.")

    # ============================================================
    #   EXPORTAR LOGS A ARCHIVO
    # ============================================================
    def exportar_logs(self):
        if not self.logs:
            messagebox.showwarning("Aviso", "No hay logs para exportar.")
            return

        archivo = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Archivo de texto", "*.txt")],
            title="Guardar logs como..."
        )

        if archivo:
            with open(archivo, "w", encoding="utf-8") as f:
                for log in self.logs:
                    f.write(f"{log['fecha']} [{log['tipo']}] - {log['mensaje']}\n")

            messagebox.showinfo("Éxito", "Logs exportados correctamente.")
