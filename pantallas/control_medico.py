import tkinter as tk
from tkinter import ttk

from modulos.control_medico.control_form import construir_formulario
from modulos.control_medico.control_core import evaluar_control_medico
from modulos.control_medico.control_resultados import (
    construir_panel_resultados,
    actualizar_diagnostico
)

from componentes_ui.scrollable_frame import ScrollableFrame  # IMPORTANTE


class PantallaControlMedico(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="#f4f6f9")
        self.app = app

        # BOTÓN VOLVER
        btn_volver = tk.Button(
            self,
            text="⬅ Volver al menú",
            font=("Segoe UI", 11, "bold"),
            bg="white",
            relief="solid",
            borderwidth=1,
            command=lambda: app.mostrar_pantalla("menu")
        )
        btn_volver.pack(anchor="nw", padx=20, pady=20)

        # TÍTULO
        titulo = tk.Label(
            self,
            text="Control Médico - Evaluación de Síntomas",
            font=("Segoe UI", 28, "bold"),
            bg="#f4f6f9",
            fg="#1c1c1c"
        )
        titulo.pack(pady=(0, 5))

        subtitulo = tk.Label(
            self,
            text="Completa la información para obtener una orientación clínica inicial",
            font=("Segoe UI", 14),
            bg="#f4f6f9",
            fg="#6c757d"
        )
        subtitulo.pack(pady=(0, 25))

        # ============================================================
        # SCROLL GENERAL
        # ============================================================
        scroll = ScrollableFrame(self)
        scroll.pack(fill="both", expand=True)

        contenedor = scroll.scrollable_frame
        contenedor.config(bg="#f4f6f9")

        # ============================================================
        # GRID DE 2 COLUMNAS
        # ============================================================
        contenedor.grid_columnconfigure(0, weight=1)
        contenedor.grid_columnconfigure(1, weight=1)

        # ============================================================
        # COLUMNA IZQUIERDA → FORMULARIO
        # ============================================================
        self.form_frame, self.form_refs = construir_formulario(contenedor)
        self.form_frame.grid(
            row=0, column=0,
            padx=(30, 15), pady=(0, 15),
            sticky="nw"
        )

        # BOTÓN EVALUAR
        btn_eval = tk.Button(
            contenedor,
            text="Evaluar estado clínico",
            font=("Segoe UI", 15, "bold"),
            bg="#0d6efd",
            fg="white",
            padx=25,
            pady=10,
            borderwidth=0,
            command=self.evaluar
        )
        btn_eval.grid(
            row=1, column=0,
            padx=(30, 15),
            pady=(0, 15),
            sticky="w"
        )

        # ============================================================
        # COLUMNA DERECHA → PANEL GRANDE DE RESULTADOS
        # ============================================================
        self.result_frame, self.result_refs = construir_panel_resultados(contenedor)
        self.result_frame.grid(
            row=0,
            column=1,
            rowspan=3,
            padx=(15, 30),
            pady=(0, 15),
            sticky="n"
        )

    # ============================================================
    # FUNCIÓN EVALUAR
    # ============================================================
    def evaluar(self):
        try:
            temp = float(self.form_refs["temp"].get())
            dias = int(self.form_refs["dias"].get())
            tipo_tos = self.form_refs["tos"].get()

            sintomas = [
                s for s, var in self.form_refs["sintomas"].items() if var.get()
            ]

            signos = {
                "pecho": self.form_refs["signos_alarma"]["pecho"].get(),
                "conciencia": self.form_refs["signos_alarma"]["conciencia"].get()
            }

            # Datos nuevos
            spo2 = self.form_refs["spo2"].get()
            fc = self.form_refs["fc"].get()
            fr = self.form_refs["fr"].get()

            resultado = evaluar_control_medico(
                temp, dias, sintomas, tipo_tos, signos,
                spo2, fc, fr
            )

            resultado["sintomas"] = sintomas
            resultado["dias"] = dias
            resultado["temp"] = temp
            resultado["spo2"] = spo2
            resultado["fc"] = fc
            resultado["fr"] = fr

            # Se muestra SOLO en el panel grande
            actualizar_diagnostico(self.result_refs, resultado)

        except ValueError:
            error = {
                "nivel": "ERROR",
                "color": "#dc3545",
                "motivos": ["Ingresa datos válidos."],
                "recomendacion": "Corrige los datos e inténtalo nuevamente.",
            }
            actualizar_diagnostico(self.result_refs, error)
