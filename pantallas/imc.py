import tkinter as tk
from tkinter import ttk
from componentes_ui.ui_base_screen import UIBaseScreen


class PantallaIMC(UIBaseScreen):
    def __init__(self, parent, controller):
        super().__init__(
            parent,
            controller,
            titulo="Cálculo de IMC",
            subtitulo="Evaluación del estado nutricional"
        )

        self.controller = controller

        # ===========================================
        # CARGAR ICONO PNG
        # ===========================================
        try:
            self.icon_imc = tk.PhotoImage(file="assets/icons/imc.png")
        except Exception:
            self.icon_imc = None

        if self.icon_imc:
            tk.Label(self, image=self.icon_imc, bg="white").pack(pady=(5, 0))

        # Separador visual
        ttk.Separator(self, orient="horizontal").pack(fill="x", pady=(10, 20))

        # ===========================================
        # CONTENEDOR
        # ===========================================
        container = self.get_card()
        container.configure(bg="white", padx=40, pady=30)

        cont = tk.Frame(container, bg="white")
        cont.pack()

        # ============================================================
        # FORMULARIO – IZQUIERDA
        # ============================================================
        form = tk.Frame(cont, bg="white")
        form.grid(row=0, column=0, padx=(0, 50), sticky="nw")

        def campo(label, row):
            ttk.Label(form, text=label, font=("Arial", 13), background="white").grid(
                row=row, column=0, sticky="w", pady=10
            )
            entry = ttk.Entry(form, width=14, font=("Arial", 12))
            entry.grid(row=row, column=1, padx=10)
            return entry

        self.entry_peso = campo("Peso (kg):", 0)
        self.entry_est = campo("Estatura (cm):", 1)
        self.entry_edad = campo("Edad:", 2)

        ttk.Button(form, text="Calcular IMC", style="Calcular.TButton",
                   command=self.calcular_imc).grid(row=3, column=0, columnspan=2, pady=20)

        ttk.Button(form, text="Limpiar", style="Limpiar.TButton",
                   command=self.limpiar).grid(row=4, column=0, columnspan=2)

        # ============================================================
        # CARD RESULTADOS – DERECHA
        # ============================================================
        self.card_res = tk.Frame(
            cont, bg="white", highlightbackground="#D8D8D8", highlightthickness=1,
            padx=25, pady=20
        )
        self.card_res.grid(row=0, column=1, sticky="n")

        # Barra vertical de color
        self.barra_color = tk.Frame(self.card_res, width=8, bg="#CCCCCC")
        self.barra_color.pack(side="left", fill="y", padx=(0, 15))

        self.frame_contenido = tk.Frame(self.card_res, bg="white")
        self.frame_contenido.pack(side="left")

        ttk.Label(
            self.frame_contenido,
            text="📊 Resultado del análisis clínico",
            font=("Arial", 16, "bold"),
            background="white"
        ).pack()

        self.lbl_resultado = ttk.Label(
            self.frame_contenido,
            text="Ingrese sus datos y presione Calcular IMC.",
            font=("Arial", 13),
            background="white"
        )
        self.lbl_resultado.pack(pady=(10, 5))

        self.frame_detalles = tk.Frame(self.frame_contenido, bg="white")
        self.frame_detalles.pack()

        # Indicador visual horizontal
        self.frame_barras = tk.Frame(self.frame_contenido, bg="white")
        self.frame_barras.pack(pady=(15, 0), fill="x")

        # Nota clínica inferior
        self.lbl_nota = ttk.Label(
            self,
            text="📘 El IMC es una referencia clínica general y no reemplaza una evaluación médica completa.",
            background="white", foreground="#444", font=("Arial", 11),
            wraplength=850, justify="center"
        )
        self.lbl_nota.pack(pady=(25, 10))

    # ============================================================
    # LIMPIAR
    # ============================================================
    def limpiar(self):
        self.entry_peso.delete(0, tk.END)
        self.entry_est.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)

        self.lbl_resultado.config(text="Ingrese sus datos y presione Calcular IMC.")
        self.barra_color.config(bg="#CCCCCC")

        for w in self.frame_detalles.winfo_children():
            w.destroy()
        for w in self.frame_barras.winfo_children():
            w.destroy()

    # ============================================================
    # CÁLCULO COMPLETO IMC + PESO IDEAL + CALORÍAS
    # ============================================================
    def calcular_imc(self):
        try:
            peso = float(self.entry_peso.get())
            est_cm = float(self.entry_est.get())
            edad = int(self.entry_edad.get())
            est = est_cm / 100
            if peso <= 0 or est <= 0:
                raise ValueError
        except:
            self.lbl_resultado.config(text="⚠️ Ingrese valores válidos.", foreground="red")
            return

        # IMC
        imc = round(peso / (est * est), 2)

        # Peso ideal (rango)
        peso_min = round(18.5 * est * est, 2)
        peso_max = round(24.9 * est * est, 2)

        # % respecto al ideal medio
        peso_ideal = (peso_min + peso_max) / 2
        porcentaje_ideal = round((peso / peso_ideal) * 100, 1)

        # Calorías estimadas TMB (método simplificado)
        tmb = round(10*peso + 6.25*est_cm - 5*edad + 5, 2)
        calorias = round(tmb * 1.55)

        # Estado clínico
        estado, color, recomendaciones, riesgos = self._interpretar_imc(imc)

        # Mostrar todo
        self._mostrar_resultado(
            imc, estado, color,
            recomendaciones, riesgos,
            peso_min, peso_max,
            porcentaje_ideal, calorias
        )

    # ============================================================
    # INTERPRETACIÓN CLÍNICA
    # ============================================================
    def _interpretar_imc(self, imc):

        if imc < 18.5:
            return ("Bajo peso", "#E0A800",
                    ["Aumentar consumo de proteínas.",
                     "Consultar si hay síntomas asociados.",
                     "Controles nutricionales frecuentes."],
                    ["Sistema inmune debilitado", "Fatiga crónica"])

        elif 18.5 <= imc <= 24.9:
            return ("Normal", "#1B9C5A",
                    ["Mantener dieta equilibrada.",
                     "Actividad física regular.",
                     "Controles preventivos recomendados."],
                    [])

        elif 25 <= imc <= 29.9:
            return ("Sobrepeso", "#D98218",
                    ["Reducir grasas y azúcares.",
                     "Aumentar actividad física.",
                     "Controlar peso regularmente."],
                    ["Riesgo cardiovascular moderado"])

        else:
            return ("Obesidad", "#C62828",
                    ["Evaluación clínica recomendada.",
                     "Plan nutricional supervisado.",
                     "Actividad física guiada."],
                    ["Alto riesgo cardiovascular", "Mayor riesgo metabólico"])

    # ============================================================
    # MOSTRAR RESULTADO COMPLETO
    # ============================================================
    def _mostrar_resultado(
        self, imc, estado, color,
        recomendaciones, riesgos,
        peso_min, peso_max, porcentaje_ideal,
        calorias
    ):

        self.lbl_resultado.config(
            text=f"IMC calculado: {imc}",
            foreground=color
        )
        self.barra_color.config(bg=color)

        # Limpiar
        for w in self.frame_detalles.winfo_children():
            w.destroy()
        for w in self.frame_barras.winfo_children():
            w.destroy()

        # Estado
        ttk.Label(
            self.frame_detalles,
            text=f"Estado: {estado}",
            font=("Arial", 14, "bold"),
            background="white",
            foreground=color
        ).pack(anchor="w", pady=(5, 10))

        # Peso ideal
        ttk.Label(
            self.frame_detalles,
            text=f"Peso recomendado: {peso_min} kg – {peso_max} kg",
            background="white", font=("Arial", 12)
        ).pack(anchor="w")

        # % respecto al ideal
        ttk.Label(
            self.frame_detalles,
            text=f"Porcentaje respecto al ideal: {porcentaje_ideal}%",
            background="white", font=("Arial", 12)
        ).pack(anchor="w", pady=(3, 8))

        # Calorías estimadas
        ttk.Label(
            self.frame_detalles,
            text=f"Calorías recomendadas por día (estimado): {calorias} kcal",
            background="white", font=("Arial", 12)
        ).pack(anchor="w", pady=(3, 10))

        # Rango IMC normal
        ttk.Label(
            self.frame_detalles,
            text="Rango de IMC normal: 18.5 – 24.9",
            font=("Arial", 11, "bold"),
            background="white"
        ).pack(anchor="w", pady=(5, 10))

        # Indicador horizontal visual
        self._crear_barra_visual(imc)

        # Recomendaciones
        ttk.Label(
            self.frame_detalles,
            text="\nRecomendaciones:",
            font=("Arial", 12, "bold"),
            background="white"
        ).pack(anchor="w")

        for r in recomendaciones:
            ttk.Label(
                self.frame_detalles,
                text=f"• {r}",
                font=("Arial", 11),
                background="white"
            ).pack(anchor="w")

        # Riesgos
        if riesgos:
            ttk.Label(
                self.frame_detalles,
                text="\nRiesgos asociados:",
                font=("Arial", 12, "bold"),
                background="white",
                foreground="#A80000"
            ).pack(anchor="w")
            for r in riesgos:
                ttk.Label(
                    self.frame_detalles,
                    text=f"• {r}",
                    background="white",
                    font=("Arial", 11),
                    foreground="#A80000"
                ).pack(anchor="w")

    # ============================================================
    # INDICADOR VISUAL HORIZONTAL
    # ============================================================
    def _crear_barra_visual(self, imc):
        # Limpiar contenido anterior
        for w in self.frame_barras.winfo_children():
            w.destroy()

        # Ajustes visuales
        width = 420      # ancho total de la barra
        height = 30      # alto de cada segmento
        espacio_vertical = 20

        canvas = tk.Canvas(
            self.frame_barras,
            width=width,
            height=height + 60,
            bg="white",
            highlightthickness=0
        )
        canvas.pack(pady=10)

        # Rangos IMC
        limites = [0, 18.5, 24.9, 29.9, 40]
        colores = ["#D9A404", "#1B9C5A", "#D98218", "#C62828"]
        etiquetas = ["Bajo peso", "Normal", "Sobrepeso", "Obesidad"]

        # Función para mapear el IMC al ancho de la barra
        def map_imc(val):
            val = max(0, min(40, val))
            return (val / 40) * width

        # Dibujar segmentos
                # Tamaño fijo para segmentos (4 iguales)
        segmento = width / 4

        for i in range(4):
            x1 = i * segmento
            x2 = x1 + segmento

            # Dibujar segmento con ancho fijo
            canvas.create_rectangle(
                x1, 0,
                x2, height,
                fill=colores[i],
                outline="white"
            )

            # Etiqueta centrada
            canvas.create_text(
                (x1 + x2) / 2,
                height / 2,
                text=etiquetas[i],
                font=("Arial", 11, "bold"),
                fill="white"
            )
        # Marcador ▲ (flecha)
        x_imc = map_imc(imc)
        canvas.create_polygon(
            x_imc - 8, height + 10,
            x_imc + 8, height + 10,
            x_imc, height - 2,
            fill="black"
        )

        # Texto IMC más separado y centrado
        canvas.create_text(
            x_imc,
            height + 30,
            text=f"Tu IMC: {imc}",
            font=("Arial", 11, "bold"),
            fill="black"
        )
