import tkinter as tk
from tkinter import ttk

from modulos.diabetes.diabetes_form import construir_formulario_diabetes
from modulos.diabetes.diabetes_core import evaluar_diabetes
from modulos.diabetes.diabetes_resultados import (
    construir_panel_resultados_diabetes,
    actualizar_resultados_diabetes
)

class PantallaDiabetes(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="white")
        self.app = app

        # ================================
        # TÍTULOS SUPERIORES
        # ================================
        titulo = tk.Label(
            self,
            text="Evaluación de Diabetes",
            font=("Segoe UI", 26, "bold"),
            bg="white",
            fg="#222"
        )
        titulo.pack(pady=(30, 5))

        subtitulo = tk.Label(
            self,
            text="Complete los datos para obtener un diagnóstico personalizado",
            font=("Segoe UI", 14),
            fg="#555",
            bg="white"
        )
        subtitulo.pack(pady=(0, 25))

        # ====================================================================
        # CONTENEDOR PRINCIPAL (DOS COLUMNAS)
        # ====================================================================
        layout = tk.Frame(self, bg="white")
        layout.pack(fill="both", expand=True, padx=40, pady=20)

        layout.columnconfigure(0, weight=1)  # columna formulario
        layout.columnconfigure(1, weight=1)  # columna resultados

        # ============================
        # COLUMNA IZQUIERDA: FORMULARIO
        # ============================
        cont_form = tk.Frame(layout, bg="white")
        cont_form.grid(row=0, column=0, sticky="nsew", padx=(0, 25))

        self.formulario = construir_formulario_diabetes(cont_form)

        # BOTÓN EVALUAR
        btn_evaluar = tk.Label(
            cont_form,
            text="Evaluar",
            font=("Segoe UI", 15, "bold"),
            bg="#0d9488",
            fg="white",
            padx=35,
            pady=12,
            cursor="hand2"
        )
        btn_evaluar.pack(pady=25)

        btn_evaluar.bind("<Button-1>", lambda e: self.evaluar())
        btn_evaluar.bind("<Enter>", lambda e: btn_evaluar.config(bg="#0a6f60"))
        btn_evaluar.bind("<Leave>", lambda e: btn_evaluar.config(bg="#0d9488"))

        # ============================
        # COLUMNA DERECHA: RESULTADOS
        # ============================
        cont_result = tk.Frame(layout, bg="white")
        cont_result.grid(row=0, column=1, sticky="nsew", padx=(25, 0))

        self.panel_resultados = construir_panel_resultados_diabetes(cont_result)
        self.panel_resultados["card"].pack_forget()

        # ============================
        # BOTÓN VOLVER
        # ============================
        btn_volver = tk.Label(
            self,
            text="⟵ Volver al menú",
            font=("Segoe UI", 12, "bold"),
            fg="#0d9488",
            bg="white",
            cursor="hand2"
        )
        btn_volver.pack(pady=(10, 10))
        btn_volver.bind("<Button-1>", lambda e: self.app.volver_menu())
        btn_volver.bind("<Enter>", lambda e: btn_volver.config(fg="#0a6f60"))
        btn_volver.bind("<Leave>", lambda e: btn_volver.config(fg="#0d9488"))

    # ======================================================
    # FUNCIÓN PARA EVALUAR
    # ======================================================
    def evaluar(self):
        datos = {
            "ayunas": self.formulario["ayunas"].get(),
            "post": self.formulario["post"].get(),
            "peso": self.formulario["peso"].get(),
            "estatura": self.formulario["estatura"].get(),
            "sed": self.formulario["sed"].get(),
            "miccion": self.formulario["miccion"].get(),
            "fatiga": self.formulario["fatiga"].get(),
            "antecedentes": self.formulario["antecedentes"].get()
        }

        resultado = evaluar_diabetes(datos)

        # MOSTRAR PANEL AL COSTADO
        card = self.panel_resultados["card"]
        card.pack(fill="both", expand=True)

        actualizar_resultados_diabetes(self.panel_resultados, resultado)
