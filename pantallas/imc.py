import tkinter as tk


class PantallaIMC(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="#f8f9fa")   # Fondo suave profesional
        self.app = app

        # ============================================================
        # BOTÓN VOLVER
        # ============================================================
        btn_volver = tk.Button(
            self,
            text="⬅ Volver al menú",
            font=("Arial", 12, "bold"),
            bg="white",
            relief="solid",
            borderwidth=1,
            command=lambda: app.mostrar_pantalla("menu")
        )
        btn_volver.pack(anchor="nw", padx=20, pady=20)

        # ============================================================
        # TÍTULO + ICONO
        # ============================================================
        icono = tk.Label(
            self,
            text="🍏",
            font=("Arial", 60),
            bg="#f8f9fa"
        )
        icono.pack(pady=(10, 0))

        titulo = tk.Label(
            self,
            text="Asistente Nutricional - Cálculo de IMC",
            font=("Arial", 26, "bold"),
            bg="#f8f9fa"
        )
        titulo.pack(pady=(5, 5))

        subtitulo = tk.Label(
            self,
            text="Ingresa tus datos para obtener un análisis nutricional completo",
            font=("Arial", 14),
            fg="#555",
            bg="#f8f9fa"
        )
        subtitulo.pack(pady=(0, 25))

        # ============================================================
        # CONTENEDOR HORIZONTAL (FORM + RESULTADOS)
        # ============================================================
        contenedor = tk.Frame(self, bg="#f8f9fa")
        contenedor.pack(pady=10)

        # ============================================================
        # FORMULARIO A LA IZQUIERDA
        # ============================================================
        card_form = tk.Frame(
            contenedor,
            bg="white",
            relief="solid",
            borderwidth=1,
            padx=30,
            pady=20
        )
        card_form.grid(row=0, column=0, padx=40)

        tk.Label(card_form, text="Peso (kg):", font=("Arial", 14), bg="white").grid(row=0, column=0, pady=10, sticky="e")
        self.entry_peso = tk.Entry(card_form, font=("Arial", 14), width=10)
        self.entry_peso.grid(row=0, column=1, padx=10)

        tk.Label(card_form, text="Estatura (cm):", font=("Arial", 14), bg="white").grid(row=1, column=0, pady=10, sticky="e")
        self.entry_estatura = tk.Entry(card_form, font=("Arial", 14), width=10)
        self.entry_estatura.grid(row=1, column=1, padx=10)

        tk.Label(card_form, text="Edad:", font=("Arial", 14), bg="white").grid(row=2, column=0, pady=10, sticky="e")
        self.entry_edad = tk.Entry(card_form, font=("Arial", 14), width=10)
        self.entry_edad.grid(row=2, column=1, padx=10)

        btn_calcular = tk.Button(
            card_form,
            text="Calcular IMC",
            font=("Arial", 16, "bold"),
            bg="#0d9488",
            fg="white",
            padx=20,
            pady=10,
            command=self.calcular_imc
        )
        btn_calcular.grid(row=3, column=0, columnspan=2, pady=20)

        # ============================================================
        # RESULTADOS A LA DERECHA
        # ============================================================
        card_res = tk.Frame(
            contenedor,
            bg="white",
            relief="solid",
            borderwidth=1,
            padx=25,
            pady=20
        )
        card_res.grid(row=0, column=1, padx=40, sticky="n")

        self.lbl_titulo_res = tk.Label(
            card_res,
            text="📊 Resultado del análisis",
            font=("Arial", 18, "bold"),
            bg="white"
        )
        self.lbl_titulo_res.pack()

        self.lbl_resultado = tk.Label(
            card_res,
            text="Ingrese sus datos y presione Calcular IMC.",
            font=("Arial", 14),
            bg="white",
            justify="left"
        )
        self.lbl_resultado.pack(pady=10)

    # ============================================================
    # LÓGICA DEL IMC
    # ============================================================
    def calcular_imc(self):
        try:
            peso = float(self.entry_peso.get())
            estatura_cm = float(self.entry_estatura.get())
            edad = int(self.entry_edad.get())

            if peso <= 0 or estatura_cm <= 0:
                self.lbl_resultado.config(text="⚠️ Por favor ingresa valores válidos.", fg="red")
                return

            estatura_m = estatura_cm / 100
            imc = peso / (estatura_m ** 2)
            imc_redondeado = round(imc, 2)

            # Clasificación OMS
            if imc < 18.5:
                clasificacion = "Bajo peso"
                texto_clas = "Tu IMC indica un peso por debajo de lo recomendado."
                recomendacion = "Incluye alimentos energéticos como frutos secos, huevos, avena y consulta con nutrición."
            elif 18.5 <= imc < 24.9:
                clasificacion = "Normal"
                texto_clas = "Te encuentras dentro del rango saludable."
                recomendacion = "Mantén una dieta equilibrada y actividad física regular."
            elif 25 <= imc < 29.9:
                clasificacion = "Sobrepeso"
                texto_clas = "Tu peso está por encima del rango adecuado."
                recomendacion = "Disminuye azúcares y grasas, aumenta frutas, verduras y actividad física."
            elif 30 <= imc < 34.9:
                clasificacion = "Obesidad I"
                texto_clas = "Tu IMC indica obesidad leve."
                recomendacion = "Se recomienda evaluación nutricional profesional."
            elif 35 <= imc < 39.9:
                clasificacion = "Obesidad II"
                texto_clas = "Tu peso indica obesidad moderada."
                recomendacion = "Acude a un especialista para seguimiento continuo."
            else:
                clasificacion = "Obesidad III"
                texto_clas = "Presentas obesidad severa."
                recomendacion = "Riesgo elevado. Busca atención médica urgente."

            texto_final = (
                f"📌 *Resultado del análisis nutricional*\n\n"
                f"• IMC calculado: {imc_redondeado}\n"
                f"• Clasificación: {clasificacion}\n"
                f"• {texto_clas}\n\n"
                f"🩺 Recomendación:\n{recomendacion}"
            )

            self.lbl_resultado.config(text=texto_final, fg="#333")

        except ValueError:
            self.lbl_resultado.config(text="⚠️ Ingresa solo números válidos.", fg="red")
