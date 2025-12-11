# ============================================================
# CONTROL MÉDICO - LÓGICA CLÍNICA CENTRAL
# ============================================================

def evaluar_control_medico(temp, dias, sintomas, tipo_tos, signos_alarma,
                           spo2, fc, fr):
    """
    Evalúa el estado clínico del paciente.

    Parámetros:
    - temp (float)
    - dias (int)
    - sintomas (list[str])
    - tipo_tos (str)
    - signos_alarma (dict)
    - spo2 (str): categoría SpO₂ seleccionada
    - fc (str): categoría de frecuencia cardíaca
    - fr (str): categoría de frecuencia respiratoria

    Retorna un diccionario con nivel, motivos, color y recomendación.
    """

    riesgo = 0
    motivos = []

    # ============================================================
    # TEMPERATURA
    # ============================================================
    if temp >= 39:
        riesgo += 2
        motivos.append("Fiebre muy alta")
    elif temp >= 38:
        riesgo += 1
        motivos.append("Fiebre elevada")

    # ============================================================
    # DURACIÓN DE SÍNTOMAS
    # ============================================================
    if dias >= 5:
        riesgo += 1
        motivos.append("Síntomas prolongados")

    # ============================================================
    # TIPO DE TOS
    # ============================================================
    if tipo_tos == "con flema":
        motivos.append("Tos productiva")

    # ============================================================
    # SÍNTOMAS FUERTES
    # ============================================================
    if "Dificultad para respirar" in sintomas:
        riesgo += 3
        motivos.append("Dificultad respiratoria")

    if "Dolor de cabeza" in sintomas and "Fiebre" in sintomas:
        motivos.append("Cefalea febril")

    # ============================================================
    # SIGNOS DE ALARMA
    # ============================================================
    if signos_alarma.get("pecho"):
        riesgo += 3
        motivos.append("Dolor en el pecho")

    if signos_alarma.get("conciencia"):
        riesgo += 3
        motivos.append("Alteración de conciencia")

    # ============================================================
    # SATURACIÓN SpO₂
    # ============================================================
    if "Grave" in spo2:
        riesgo += 4
        motivos.append("Saturación de oxígeno críticamente baja")
    elif "Moderada" in spo2:
        riesgo += 2
        motivos.append("Saturación baja")
    elif "Leve" in spo2:
        riesgo += 1
        motivos.append("Saturación algo reducida")

    # ============================================================
    # FRECUENCIA CARDIACA
    # ============================================================
    if "severa" in fc.lower():
        riesgo += 3
        motivos.append("Taquicardia severa")
    elif "moderada" in fc.lower():
        riesgo += 2
        motivos.append("Taquicardia moderada")
    elif "leve" in fc.lower():
        riesgo += 1
        motivos.append("Taquicardia leve")
    elif "bradicardia" in fc.lower():
        riesgo += 2
        motivos.append("Bradicardia")

    # ============================================================
    # FRECUENCIA RESPIRATORIA
    # ============================================================
    if "Severa" in fr:
        riesgo += 4
        motivos.append("Frecuencia respiratoria críticamente alta")
    elif "Moderada" in fr:
        riesgo += 2
        motivos.append("Frecuencia respiratoria elevada")
    elif "Leve" in fr:
        riesgo += 1
        motivos.append("Frecuencia respiratoria aumentada")

    # ============================================================
    # CLASIFICACIÓN FINAL
    # ============================================================
    if riesgo >= 8:
        nivel = "ALTO"
        color = "#dc3545"
        recomendacion = "Acudir inmediatamente a emergencias."
    elif riesgo >= 4:
        nivel = "MODERADO"
        color = "#ffc107"
        recomendacion = "Revisar en consulta médica en las próximas 24-48 horas."
    else:
        nivel = "BAJO"
        color = "#198754"
        recomendacion = "Reposo, hidratación y vigilancia de síntomas."

    # ============================================================
    # RETORNO PROFESIONAL
    # ============================================================
    return {
        "nivel": nivel,
        "color": color,
        "motivos": motivos,
        "recomendacion": recomendacion
    }
