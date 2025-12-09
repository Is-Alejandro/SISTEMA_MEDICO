import tkinter as tk
from tkinter import ttk


class PantallaControlMedico(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="#f4f6f9")  # Fondo institucional moderno
        self.app = app

        # Colores del sistema
        self.color_azul = "#0d6efd"
        self.color_verde = "#198754"
        self.color_ambar = "#ffc107"
        self.color_rojo = "#dc3545"

        # ---------------------------------------------------------
        # BOTÓN VOLVER
        # ---------------------------------------------------------
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

        # ---------------------------------------------------------
        # TÍTULO PRINCIPAL
        # ---------------------------------------------------------
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

        # ---------------------------------------------------------
        # CONTENEDOR GENERAL (3 COLUMNAS)
        # ---------------------------------------------------------
        contenedor = tk.Frame(self, bg="#f4f6f9")
        contenedor.pack(pady=10)

        # =========================================================
        # 1) COLUMNA DE SÍNTOMAS (CON CHIPS MODERNOS)
        # =========================================================
        card_sintomas = self.crear_card(contenedor, width=300, height=330)
        card_sintomas.grid(row=0, column=0, padx=25)

        tk.Label(
            card_sintomas,
            text="Síntomas",
            font=("Segoe UI", 16, "bold"),
            bg="white"
        ).pack(anchor="w", pady=(5, 10))

        self.sintomas_vars = {}
        sintomas_lista = [
            "Fiebre", "Tos", "Dolor de garganta", "Congestión nasal",
            "Dolor de cabeza", "Dolor corporal",
            "Náuseas", "Dificultad para respirar"
        ]

        self.frame_chips = tk.Frame(card_sintomas, bg="white")
        self.frame_chips.pack()

        for sintoma in sintomas_lista:
            self.crear_chip(self.frame_chips, sintoma)

        # =========================================================
        # 2) COLUMNA DE DATOS CLÍNICOS
        # =========================================================
        card_datos = self.crear_card(contenedor, width=300, height=330)
        card_datos.grid(row=0, column=1, padx=25)

        tk.Label(
            card_datos,
            text="Datos clínicos",
            font=("Segoe UI", 16, "bold"),
            bg="white"
        ).pack(anchor="w", pady=(5, 10))

        form = tk.Frame(card_datos, bg="white")
        form.pack(pady=5)

        # Temperatura
        tk.Label(form, text="Temperatura (°C):", font=("Segoe UI", 13), bg="white").grid(row=0, column=0, sticky="w", pady=8)
        self.entry_temp = tk.Entry(form, font=("Segoe UI", 13), width=10)
        self.entry_temp.grid(row=0, column=1, padx=10)

        # Días con síntomas
        tk.Label(form, text="Días con síntomas:", font=("Segoe UI", 13), bg="white").grid(row=1, column=0, sticky="w", pady=8)
        self.entry_dias = tk.Entry(form, font=("Segoe UI", 13), width=10)
        self.entry_dias.grid(row=1, column=1, padx=10)

        # Tipo de tos
        tk.Label(form, text="Tipo de tos:", font=("Segoe UI", 13), bg="white").grid(row=2, column=0, sticky="w", pady=8)
        self.combo_tos = ttk.Combobox(form, values=["seca", "con flema"], state="readonly", font=("Segoe UI", 12), width=12)
        self.combo_tos.grid(row=2, column=1, padx=10)
        self.combo_tos.set("seca")

        # Signos de alarma
        tk.Label(card_datos, text="Signos de alarma", font=("Segoe UI", 14, "bold"), fg=self.color_rojo, bg="white").pack(pady=(15, 5))

        self.var_pecho = tk.BooleanVar()
        self.var_conciencia = tk.BooleanVar()

        tk.Checkbutton(card_datos, text="Dolor en el pecho", variable=self.var_pecho, bg="white", font=("Segoe UI", 12)).pack(anchor="w")
        tk.Checkbutton(card_datos, text="Pérdida de conciencia", variable=self.var_conciencia, bg="white", font=("Segoe UI", 12)).pack(anchor="w")

        # =========================================================
        # 3) COLUMNA DE DIAGNÓSTICO (VACÍA HASTA EVALUACIÓN)
        # =========================================================
        self.card_diag = self.crear_card(contenedor, width=320, height=330)
        self.card_diag.grid(row=0, column=2, padx=25)

        self.lbl_diag_titulo = tk.Label(
            self.card_diag,
            text="Diagnóstico clínico",
            font=("Segoe UI", 16, "bold"),
            bg="white"
        )
        self.lbl_diag_titulo.pack(pady=(10, 5))

        self.lbl_diag_contenido = tk.Label(
            self.card_diag,
            text="(Esperando evaluación...)",
            font=("Segoe UI", 13),
            bg="white",
            fg="#6c757d",
            justify="left",
            wraplength=260
        )
        self.lbl_diag_contenido.pack()

        # =========================================================
        # BOTÓN EVALUAR
        # =========================================================
        btn_eval = tk.Button(
            self,
            text="Evaluar estado clínico",
            font=("Segoe UI", 15, "bold"),
            bg=self.color_azul,
            fg="white",
            padx=25,
            pady=10,
            borderwidth=0,
            command=self.evaluar
        )
        btn_eval.pack(pady=25)

    # =========================================================
    # FUNCIÓN: CREAR CARD PROFESIONAL
    # =========================================================
    def crear_card(self, parent, width, height):
        frame = tk.Frame(
            parent,
            bg="white",
            relief="solid",
            borderwidth=1,
            padx=20,
            pady=15
        )
        frame.config(width=width, height=height)
        frame.pack_propagate(False)
        return frame

    # =========================================================
    # FUNCIÓN: CREAR CHIPS DE SÍNTOMAS
    # =========================================================
    def crear_chip(self, parent, texto):
        var = tk.BooleanVar()
        self.sintomas_vars[texto] = var

        chip = tk.Checkbutton(
            parent,
            text=f" {texto} ",
            variable=var,
            font=("Segoe UI", 12),
            bg="white",
            relief="solid",
            borderwidth=1,
            selectcolor="#e7f1ff",
            activebackground="#e7f1ff"
        )
        chip.pack(anchor="w", pady=3)

    # =========================================================
    # EVALUACIÓN CLÍNICA
    # =========================================================
    def evaluar(self):
        try:
            temp = float(self.entry_temp.get())
            dias = int(self.entry_dias.get())
            tos = self.combo_tos.get()

            sintomas = [s for s, v in self.sintomas_vars.items() if v.get()]
            riesgo = 0
            motivos = []

            # --- Temperatura ---
            if temp >= 39:
                riesgo += 2
                motivos.append("Fiebre muy alta")
            elif temp >= 38:
                riesgo += 1
                motivos.append("Fiebre elevada")

            # --- Días con síntomas ---
            if dias >= 5:
                riesgo += 1
                motivos.append("Síntomas prolongados")

            # --- Tipo de tos ---
            if tos == "con flema":
                motivos.append("Tos productiva")

            # --- Síntomas fuertes ---
            if "Dificultad para respirar" in sintomas:
                riesgo += 3
                motivos.append("Dificultad respiratoria")

            if "Dolor de cabeza" in sintomas and "Fiebre" in sintomas:
                motivos.append("Cefalea febril")

            # --- Signos de alarma ---
            if self.var_pecho.get():
                riesgo += 3
                motivos.append("Dolor en el pecho")

            if self.var_conciencia.get():
                riesgo += 3
                motivos.append("Alteración de conciencia")

            # -----------------------------------------------------
            # CLASIFICACIÓN FINAL
            # -----------------------------------------------------
            if riesgo >= 6:
                nivel = "ALTO"
                color = self.color_rojo
                recomendacion = "Acudir inmediatamente a emergencias."
            elif riesgo >= 3:
                nivel = "MODERADO"
                color = self.color_ambar
                recomendacion = "Revisar en consulta médica en las próximas 24-48 horas."
            else:
                nivel = "BAJO"
                color = self.color_verde
                recomendacion = "Reposo, hidratación y vigilancia de síntomas."

            # -----------------------------------------------------
            # MOSTRAR RESULTADO PROFESIONAL
            # -----------------------------------------------------
            texto_final = f"Nivel de riesgo: {nivel}\n\n"
            texto_final += "Motivos:\n"
            for m in motivos:
                texto_final += f"• {m}\n"
            texto_final += f"\nRecomendación:\n{recomendacion}"

            self.lbl_diag_contenido.config(
                text=texto_final,
                fg=color
            )

        except ValueError:
            self.lbl_diag_contenido.config(
                text="⚠️ Ingresa datos válidos.",
                fg=self.color_rojo
            )
