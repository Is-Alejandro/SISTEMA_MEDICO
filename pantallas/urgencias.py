import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class PantallaUrgencias(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="white")
        self.app = app

        # ============================================================
        # FONDO CON IMAGEN
        # ============================================================
        self.bg_raw = Image.open("assets/fondo_medico.png")
        self.bg_raw = self.bg_raw.resize((1400, 900), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_raw)

        fondo = tk.Label(self, image=self.bg_img)
        fondo.place(x=0, y=0, relwidth=1, relheight=1)

        # ============================================================
        # ICONOS PNG
        # ============================================================
        self.icon_signos = self.cargar_icono("assets/icons/signos_vitales.png", 38)
        self.icon_sintomas = self.cargar_icono("assets/icons/sintomas_criticos.png", 38)
        self.icon_diag = self.cargar_icono("assets/icons/diagnostico_rapido.png", 38)

        # ============================================================
        # BOTÓN VOLVER
        # ============================================================
        btn_volver = tk.Label(
            self,
            text="⬅ Volver al menú",
            font=("Segoe UI", 12, "bold"),
            bg="#e8f7f6",
            fg="#0f766e",
            padx=15,
            pady=7,
            cursor="hand2"
        )
        btn_volver.bind("<Button-1>", lambda e: app.mostrar_pantalla("menu"))
        btn_volver.bind("<Enter>", lambda e: btn_volver.config(bg="#d4f0ef"))
        btn_volver.bind("<Leave>", lambda e: btn_volver.config(bg="#e8f7f6"))
        btn_volver.place(x=20, y=15)

        # ============================================================
        # TÍTULOS
        # ============================================================
        tk.Label(
            self,
            text="Urgencias – Evaluación Rápida",
            font=("Segoe UI", 28, "bold"),
            fg="#222",
            bg="white"
        ).pack(pady=(55, 0))

        tk.Label(
            self,
            text="Complete los datos necesarios para una evaluación inmediata",
            font=("Segoe UI", 14),
            fg="#444",
            bg="white"
        ).pack(pady=(0, 25))

        # ============================================================
        # CONTENEDOR PRINCIPAL
        # ============================================================
        contenedor = tk.Frame(self, bg="white")
        contenedor.pack(pady=20)

        # ============================================================
        # VALORES PARA COMBOBOX
        # ============================================================
        temperaturas = [f"{x:.1f}" for x in [t * 0.5 for t in range(70, 85)]]
        frecuencias_cardiacas = [40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]
        respiraciones = [10, 12, 14, 16, 18, 20, 22, 24, 28, 30, 35, 40]
        saturaciones = [85, 88, 90, 92, 94, 95, 96, 97, 98, 99, 100]

        # ============================================================
        # CARD SIGNOS VITALES
        # ============================================================
        self.card_vitales = self.crear_card(contenedor, 350)
        self.card_vitales.grid(row=0, column=0, padx=35)

        self.agregar_titulo_card(self.card_vitales, self.icon_signos, "Signos Vitales", "#0d6efd")

        self.entry_temp = self.crear_combo(self.card_vitales, "Temperatura (°C):", temperaturas)
        self.entry_fc = self.crear_combo(self.card_vitales, "Frecuencia cardíaca (lpm):", frecuencias_cardiacas)
        self.entry_fr = self.crear_combo(self.card_vitales, "Frecuencia respiratoria (rpm):", respiraciones)
        self.entry_o2 = self.crear_combo(self.card_vitales, "Saturación de O₂ (%):", saturaciones)

        # ============================================================
        # CARD SÍNTOMAS
        # ============================================================
        self.card_sintomas = self.crear_card(contenedor, 350)
        self.card_sintomas.grid(row=0, column=1, padx=35)

        self.agregar_titulo_card(self.card_sintomas, self.icon_sintomas, "Síntomas Críticos", "#b45309")

        self.sintomas_vars = {}
        sintomas = [
            "Dolor en el pecho",
            "Dificultad respiratoria severa",
            "Confusión o desorientación",
            "Vómitos persistentes",
            "Sangrado activo",
            "Mareos extremos",
            "Convulsiones"
        ]

        for s in sintomas:
            var = tk.BooleanVar()
            tk.Checkbutton(self.card_sintomas, text=s, variable=var, font=("Segoe UI", 12),
                           bg="white").pack(anchor="w", pady=3)
            self.sintomas_vars[s] = var

        # ============================================================
        # CARD DIAGNÓSTICO
        # ============================================================
        self.card_diag = self.crear_card(contenedor, 360)
        self.card_diag.grid(row=0, column=2, padx=35)

        self.agregar_titulo_card(self.card_diag, self.icon_diag, "Diagnóstico Rápido", "#111")

        self.lbl_diag = tk.Label(
            self.card_diag,
            text="A la espera de evaluación...",
            font=("Segoe UI", 13),
            fg="#555",
            bg="white",
            justify="left",
            wraplength=300
        )
        self.lbl_diag.pack(anchor="w", pady=15)

        # ============================================================
        # BOTÓN EVALUAR
        # ============================================================
        btn_eval = tk.Label(
            self,
            text="Evaluar urgencia",
            font=("Segoe UI", 16, "bold"),
            bg="#14b8a6",
            fg="white",
            padx=40,
            pady=12,
            cursor="hand2"
        )
        btn_eval.bind("<Enter>", lambda e: btn_eval.config(bg="#0f766e"))
        btn_eval.bind("<Leave>", lambda e: btn_eval.config(bg="#14b8a6"))
        btn_eval.bind("<Button-1>", lambda e: self.evaluar_urgencia())
        btn_eval.pack(pady=40)

    # ============================================================
    # UTILIDADES
    # ============================================================
    def cargar_icono(self, ruta, size):
        img = Image.open(ruta)
        img = img.resize((size, size), Image.LANCZOS)
        return ImageTk.PhotoImage(img)

    def crear_card(self, parent, width):
        return tk.Frame(
            parent,
            bg="white",
            relief="solid",
            borderwidth=1,
            padx=25,
            pady=20,
            highlightbackground="#d1d1d1",
            width=width
        )

    def agregar_titulo_card(self, parent, icono, texto, color):
        cont = tk.Frame(parent, bg="white")
        cont.pack(anchor="w", pady=(0, 15))

        tk.Label(cont, image=icono, bg="white").pack(side="left", padx=(0, 10))

        tk.Label(cont, text=texto, font=("Segoe UI", 18, "bold"), fg=color, bg="white").pack(side="left")

    def crear_combo(self, parent, label_text, opciones):
        frame = tk.Frame(parent, bg="white")
        frame.pack(anchor="w", pady=8)

        tk.Label(frame, text=label_text, font=("Segoe UI", 13), bg="white").pack(side="left")

        combo = ttk.Combobox(frame, values=opciones, width=10, state="readonly", font=("Segoe UI", 12))
        combo.pack(side="left", padx=10)
        combo.current(0)

        return combo

    # ============================================================
    # LÓGICA
    # ============================================================
    def evaluar_urgencia(self):
        motivos = []
        riesgo = "VERDE"
        color = "green"

        temp = float(self.entry_temp.get())
        fc = float(self.entry_fc.get())
        fr = float(self.entry_fr.get())
        o2 = float(self.entry_o2.get())

        # ROJO
        if o2 < 90:
            riesgo = "ROJO"; motivos.append("Saturación críticamente baja")
        if fr > 30:
            riesgo = "ROJO"; motivos.append("Dificultad respiratoria severa")
        if fc > 130:
            riesgo = "ROJO"; motivos.append("Taquicardia severa")
        if temp >= 40:
            riesgo = "ROJO"; motivos.append("Hipertermia grave")

        for s, var in self.sintomas_vars.items():
            if var.get():
                riesgo = "ROJO"; motivos.append(s)

        # AMARILLO
        if riesgo != "ROJO":
            if o2 < 94:
                riesgo = "AMARILLO"; motivos.append("Oxigenación reducida")
            if 100 < fc <= 130:
                riesgo = "AMARILLO"; motivos.append("Taquicardia moderada")
            if 22 < fr <= 30:
                riesgo = "AMARILLO"; motivos.append("Respiración acelerada")
            if 38.5 <= temp < 40:
                riesgo = "AMARILLO"; motivos.append("Fiebre alta")

        # COLOR Y RECOMENDACIÓN
        if riesgo == "ROJO":
            color = "red"
            recomendacion = "Emergencia inmediata. Acudir a un centro médico YA MISMO."
        elif riesgo == "AMARILLO":
            color = "#b45309"
            recomendacion = "Acudir a un centro de atención en las próximas horas."
        else:
            recomendacion = "Reposo, hidratación y observación."

        texto = f"🔎 Nivel de riesgo: {riesgo}\n\n"
        if motivos:
            texto += "Motivos:\n" + "\n".join([f"• {m}" for m in motivos]) + "\n\n"
        texto += f"📘 Recomendación:\n{recomendacion}"

        self.lbl_diag.config(text=texto, fg=color)
