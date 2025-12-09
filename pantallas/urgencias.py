import tkinter as tk
from tkinter import ttk


class PantallaUrgencias(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="#f0f2f5")
        self.app = app

        # ============================================================
        # BOTÓN VOLVER
        # ============================================================
        btn_volver = tk.Button(
            self, text="⬅ Volver al menú", font=("Arial", 12, "bold"),
            bg="white", relief="solid", borderwidth=1,
            command=lambda: app.mostrar_pantalla("menu")
        )
        btn_volver.pack(anchor="nw", padx=20, pady=20)

        # ============================================================
        # TÍTULOS
        # ============================================================
        titulo = tk.Label(
            self, text="Urgencias - Evaluación Rápida",
            font=("Arial", 28, "bold"), bg="#f0f2f5"
        )
        titulo.pack(pady=(5, 0))

        subtitulo = tk.Label(
            self,
            text="Complete los signos vitales y síntomas críticos para una evaluación inmediata",
            font=("Arial", 14), fg="#555", bg="#f0f2f5"
        )
        subtitulo.pack(pady=(0, 30))

        # ============================================================
        # CONTENEDOR PRINCIPAL
        # ============================================================
        contenedor = tk.Frame(self, bg="#f0f2f5")
        contenedor.pack()

        # ------------------------------------------------------------
        # TARJETA SIGNOS VITALES
        # ------------------------------------------------------------
        card_vitales = tk.Frame(
            contenedor, bg="white", relief="solid", borderwidth=1, padx=25, pady=20
        )
        card_vitales.grid(row=0, column=0, padx=30)

        tk.Label(card_vitales, text="🩺 Signos vitales", font=("Arial", 18, "bold"), bg="white").pack(anchor="w", pady=(0, 10))

        self.entry_temp = self.crear_input(card_vitales, "Temperatura (°C):")
        self.entry_fc = self.crear_input(card_vitales, "Frecuencia cardíaca (lpm):")
        self.entry_fr = self.crear_input(card_vitales, "Frecuencia respiratoria (rpm):")
        self.entry_o2 = self.crear_input(card_vitales, "Saturación de O₂ (%):")

        # ------------------------------------------------------------
        # TARJETA SÍNTOMAS CRÍTICOS
        # ------------------------------------------------------------
        card_sintomas = tk.Frame(
            contenedor, bg="white", relief="solid", borderwidth=1, padx=25, pady=20
        )
        card_sintomas.grid(row=0, column=1, padx=30)

        tk.Label(card_sintomas, text="⚠️ Síntomas críticos", font=("Arial", 18, "bold"), bg="white").pack(anchor="w", pady=(0, 10))

        self.sintomas_vars = {}
        lista_sintomas = [
            "Dolor en el pecho",
            "Dificultad respiratoria severa",
            "Confusión o desorientación",
            "Vómitos persistentes",
            "Sangrado activo",
            "Mareos extremos",
            "Convulsiones"
        ]

        for sintoma in lista_sintomas:
            var = tk.BooleanVar()
            chk = tk.Checkbutton(card_sintomas, text=sintoma, variable=var, font=("Arial", 13),
                                 bg="white", anchor="w")
            chk.pack(fill="x", pady=3)
            self.sintomas_vars[sintoma] = var

        # ------------------------------------------------------------
        # TARJETA DIAGNÓSTICO
        # ------------------------------------------------------------
        card_diag = tk.Frame(
            contenedor, bg="white", relief="solid", borderwidth=1, padx=25, pady=20
        )
        card_diag.grid(row=0, column=2, padx=30)

        tk.Label(card_diag, text="📘 Diagnóstico rápido", font=("Arial", 18, "bold"), bg="white").pack(anchor="w")

        self.lbl_diag = tk.Label(
            card_diag,
            text="A la espera de evaluación...",
            font=("Arial", 14),
            fg="#888",
            bg="white",
            justify="left"
        )
        self.lbl_diag.pack(pady=10)

        # ------------------------------------------------------------
        # BOTÓN
        # ------------------------------------------------------------
        btn_eval = tk.Button(
            self,
            text="Evaluar urgencia",
            font=("Arial", 16, "bold"),
            bg="#0d6efd",
            fg="white",
            padx=25,
            pady=12,
            command=self.evaluar_urgencia
        )
        btn_eval.pack(pady=35)

    # ------------------------------------------------------------
    # MÉTODO PARA CREAR INPUTS
    # ------------------------------------------------------------
    def crear_input(self, parent, label_text):
        frame = tk.Frame(parent, bg="white")
        frame.pack(anchor="w", pady=8)

        tk.Label(frame, text=label_text, font=("Arial", 14), bg="white").pack(side="left")
        entry = tk.Entry(frame, font=("Arial", 14), width=6)
        entry.pack(side="left", padx=10)

        return entry

    # ------------------------------------------------------------
    # LÓGICA CLÍNICA DEL TRIAGE
    # ------------------------------------------------------------
    def evaluar_urgencia(self):
        motivos = []
        riesgo = "VERDE"
        recomendacion = "Puede mantenerse en observación o acudir a consulta general."

        try:
            temp = float(self.entry_temp.get())
            fc = float(self.entry_fc.get())
            fr = float(self.entry_fr.get())
            o2 = float(self.entry_o2.get())
        except:
            self.lbl_diag.config(text="⚠️ Por favor ingrese valores numéricos válidos.", fg="red")
            return

        # ----------- Criterios de riesgo ROJO (emergencia inmediata) -----------
        if o2 < 90:
            riesgo = "ROJO"
            motivos.append("Saturación de oxígeno críticamente baja")
        if fr > 30:
            riesgo = "ROJO"
            motivos.append("Dificultad respiratoria severa")
        if fc > 130:
            riesgo = "ROJO"
            motivos.append("Taquicardia severa")
        if temp >= 40:
            riesgo = "ROJO"
            motivos.append("Fiebre extremadamente alta")

        # Síntomas críticos
        for s, var in self.sintomas_vars.items():
            if var.get():
                riesgo = "ROJO"
                motivos.append(s)

        # ----------- Criterios AMARILLO (riesgo moderado) -----------
        if riesgo != "ROJO":
            if o2 < 94:
                riesgo = "AMARILLO"
                motivos.append("Oxigenación reducida")
            if 100 < fc <= 130:
                riesgo = "AMARILLO"
                motivos.append("Taquicardia moderada")
            if 22 < fr <= 30:
                riesgo = "AMARILLO"
                motivos.append("Respiración acelerada")
            if 38.5 <= temp < 40:
                riesgo = "AMARILLO"
                motivos.append("Fiebre alta")

        # ----------- RECOMENDACIONES ----------
        if riesgo == "ROJO":
            color = "red"
            recomendacion = "Emergencia inmediata. Acudir a un centro médico ya mismo."
        elif riesgo == "AMARILLO":
            color = "#c28a00"
            recomendacion = "Acudir a un centro de atención en las próximas horas."
        else:
            color = "green"
            recomendacion = "Reposo, hidratación y seguimiento de síntomas."

        texto_final = f"🔎 Nivel de riesgo: {riesgo}\n\n"

        if motivos:
            texto_final += "Motivos:\n" + "\n".join([f"• {m}" for m in motivos]) + "\n\n"

        texto_final += f"📘 Recomendación:\n{recomendacion}"

        self.lbl_diag.config(text=texto_final, fg=color)
