def evaluar_diabetes(datos):
    """
    Recibe un diccionario con los datos del formulario y devuelve:
    - nivel_riesgo: BAJO / MODERADO / ALTO
    - descripcion_general
    - factores_relevantes
    - recomendacion_principal
    - plan_recomendado
    """

    ayunas = convertir_float(datos.get("ayunas"))
    post = convertir_float(datos.get("post"))
    peso = convertir_float(datos.get("peso"))
    estatura = convertir_float(datos.get("estatura"))

    sed = datos.get("sed")
    miccion = datos.get("miccion")
    fatiga = datos.get("fatiga")
    antecedentes = datos.get("antecedentes")

    sintomas = sum([sed, miccion, fatiga])  # True = 1

    bmi = None
    if peso and estatura:
        bmi = round(peso / (estatura ** 2), 1)

    factores = []
    descripcion = ""
    recomendacion = ""
    plan = ""
    nivel = ""

    # ================================
    #     CRITERIOS DIAGNÓSTICOS ADA
    # ================================
    # Ayunas:
    # Normal < 100
    # Prediabetes 100-125
    # Diabetes >= 126

    # Postprandial (2h):
    # Normal < 140
    # Prediabetes 140–199
    # Diabetes >= 200

    # ================================
    #       EVALUACIÓN DE AYUNAS
    # ================================
    if ayunas is not None:
        if ayunas >= 126:
            nivel = "ALTO"
            factores.append(f"Glucosa en ayunas muy elevada ({ayunas} mg/dL).")
        elif 100 <= ayunas <= 125:
            if nivel != "ALTO":
                nivel = "MODERADO"
            factores.append(f"Glucosa en ayunas en rango de prediabetes ({ayunas} mg/dL).")

    # ================================
    #   EVALUACIÓN POSTPRANDIAL
    # ================================
    if post is not None:
        if post >= 200:
            nivel = "ALTO"
            factores.append(f"Glucosa postprandial muy elevada ({post} mg/dL).")
        elif 140 <= post <= 199:
            if nivel != "ALTO":
                nivel = "MODERADO"
            factores.append(f"Glucosa postprandial elevada ({post} mg/dL).")

    # ================================
    #     EVALUACIÓN DE SÍNTOMAS
    # ================================
    if sintomas >= 2:
        if nivel != "ALTO":
            nivel = "MODERADO"
        factores.append("Presencia de síntomas compatibles con hiperglucemia.")

    # ================================
    #    EVALUACIÓN DE ANTECEDENTES
    # ================================
    if antecedentes:
        factores.append("Antecedentes familiares de diabetes.")
        if nivel == "":
            nivel = "MODERADO"

    # ================================
    #   EVALUACIÓN DE IMC (Opcional)
    # ================================
    if bmi:
        if bmi >= 30:
            factores.append(f"SOBREPESO significativo (IMC = {bmi}).")
            if nivel == "BAJO" or nivel == "":
                nivel = "MODERADO"
        elif bmi < 18.5:
            factores.append(f"Bajo peso (IMC = {bmi}).")
    
    # Si no hubo riesgos claros
    if nivel == "":
        nivel = "BAJO"

    # ================================
    #   DESCRIPCIÓN GENERAL
    # ================================
    if nivel == "BAJO":
        descripcion = "Los valores ingresados no indican riesgo significativo de diabetes."
        recomendacion = "Mantenga un estilo de vida saludable y controles preventivos regulares."
        plan = (
            "- Mantener alimentación balanceada.\n"
            "- Realizar actividad física 3–4 veces por semana.\n"
            "- Control de glucosa anual."
        )

    elif nivel == "MODERADO":
        descripcion = "Se observan indicadores que sugieren riesgo de prediabetes."
        recomendacion = "Se recomienda evaluación médica y cambios en el estilo de vida."
        plan = (
            "- Reducir consumo de azúcares y carbohidratos.\n"
            "- Realizar actividad física frecuente.\n"
            "- Control de glucosa en 3 meses.\n"
            "- Evaluar peso e IMC."
        )

    elif nivel == "ALTO":
        descripcion = "Los valores registrados sugieren alta probabilidad de diabetes no controlada."
        recomendacion = "Se recomienda acudir a atención médica lo antes posible."
        plan = (
            "- Realizar una prueba de glucosa confirmatoria.\n"
            "- Acudir a emergencia si presenta visión borrosa o debilidad extrema.\n"
            "- Iniciar ajustes dietéticos inmediatos.\n"
            "- Control médico especializado."
        )

    return {
        "nivel_riesgo": nivel,
        "descripcion_general": descripcion,
        "factores_relevantes": factores,
        "recomendacion_principal": recomendacion,
        "plan_recomendado": plan
    }


def convertir_float(valor):
    """Convierte entradas a float de manera segura."""
    try:
        return float(valor)
    except:
        return None
