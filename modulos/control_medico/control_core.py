# ============================================================
# CONTROL MÉDICO - LÓGICA CLÍNICA CENTRAL
# ============================================================

def evaluar_control_medico(temp, dias, sintomas, tipo_tos, signos_alarma):
    """
    Evalúa el estado clínico del paciente.
    
    Parámetros:
    - temp (float): temperatura en °C
    - dias (int): días con síntomas
    - sintomas (list[str]): lista de síntomas seleccionados
    - tipo_tos (str): "seca" o "con flema"
    - signos_alarma (dict): {"pecho": bool, "conciencia": bool}

    Retorna un diccionario:
    {
        "nivel": "BAJO / MODERADO / ALTO",
        "color": "#HEX",
        "motivos": [lista de razones],
        "recomendacion": "texto"
    }
    """

    riesgo = 0
    motivos = []

    # ================================
    # TEMPERATURA
    # ================================
    if temp >= 39:
        riesgo += 2
        motivos.append("Fiebre muy alta")
    elif temp >= 38:
        riesgo += 1
        motivos.append("Fiebre elevada")

    # ================================
    # DURACIÓN DE SÍNTOMAS
    # ================================
    if dias >= 5:
        riesgo += 1
        motivos.append("Síntomas prolongados")

    # ================================
    # TIPO DE TOS
    # ================================
    if tipo_tos == "con flema":
        motivos.append("Tos productiva")

    # ================================
    # SÍNTOMAS FUERTES
    # ================================
    if "Dificultad para respirar" in sintomas:
        riesgo += 3
        motivos.append("Dificultad respiratoria")

    if "Dolor de cabeza" in sintomas and "Fiebre" in sintomas:
        motivos.append("Cefalea febril")

    # ================================
    # SIGNOS DE ALARMA
    # ================================
    if signos_alarma.get("pecho"):
        riesgo += 3
        motivos.append("Dolor en el pecho")

    if signos_alarma.get("conciencia"):
        riesgo += 3
        motivos.append("Alteración de conciencia")

    # ================================
    # CLASIFICACIÓN FINAL
    # ================================
    if riesgo >= 6:
        nivel = "ALTO"
        color = "#dc3545"  # rojo
        recomendacion = "Acudir inmediatamente a emergencias."
    elif riesgo >= 3:
        nivel = "MODERADO"
        color = "#ffc107"  # ámbar
        recomendacion = "Revisar en consulta médica en las próximas 24-48 horas."
    else:
        nivel = "BAJO"
        color = "#198754"  # verde
        recomendacion = "Reposo, hidratación y vigilancia de síntomas."

    # ================================
    # RETORNO PROFESIONAL
    # ================================
    return {
        "nivel": nivel,
        "color": color,
        "motivos": motivos,
        "recomendacion": recomendacion
    }
