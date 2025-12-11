import tkinter as tk

from modulos.control_medico.control_form import construir_formulario
from modulos.control_medico.control_core import evaluar_control_medico
from modulos.control_medico.control_resultados import construir_panel_resultados, actualizar_diagnostico
from modulos.control_medico.control_graficos import construir_panel_graficos, actualizar_graficos


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
        # CONTENEDOR PRINCIPAL PARA GRID
        # ============================================================
        contenedor_grid = tk.Frame(self, bg="#f4f6f9")
        contenedor_grid.pack()

        # FORMULARIO (col 0 y col 1)
        self.form_frame, self.form_refs = construir_formulario(contenedor_grid)
        self.form_frame.grid(row=0, column=0, columnspan=2, padx=20)

        # RESULTADOS (col 2)
        self.result_frame, self.result_refs = construir_panel_resultados(contenedor_grid)
        self.result_frame.grid(row=0, column=2, padx=20)

        # ============================================================
        # GRÁFICOS (debajo)
        # ============================================================
        self.graficos_frame, self.graficos_refs = construir_panel_graficos(self)

        # BOTÓN EVALUAR
        btn_eval = tk.Button(
            self,
            text="Evaluar estado clínico",
            font=("Segoe UI", 15, "bold"),
            bg="#0d6efd",
            fg="white",
            padx=25,
            pady=10,
            borderwidth=0,
            command=self.evaluar
        )
        btn_eval.pack(pady=25)

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

            resultado = evaluar_control_medico(temp, dias, sintomas, tipo_tos, signos)

            actualizar_diagnostico(self.result_refs, resultado)

            # Gráficos (temporalmente ficticios)
            datos_temp = [temp - 0.3, temp]
            datos_sintomas = len(sintomas)
            actualizar_graficos(self.graficos_refs, datos_temp, datos_sintomas)

        except ValueError:
            actualizar_diagnostico(self.result_refs, {
                "nivel": "ERROR",
                "color": "#dc3545",
                "motivos": ["Ingresa valores válidos."],
                "recomendacion": "Corrige los datos e inténtalo nuevamente."
            })
