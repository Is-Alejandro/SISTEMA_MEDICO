# =========================================
#   LÓGICA CLÍNICA DEL CÁLCULO DE IMC
# =========================================

def interpretar_imc(imc):
    """Devuelve estado, color, recomendaciones, riesgos."""
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


def calcular_imc_completo(peso, estatura_cm, edad):
    """Devuelve IMC + análisis clínico y valores derivados."""

    est = estatura_cm / 100
    imc = round(peso / (est * est), 2)

    # Peso ideal
    peso_min = round(18.5 * est * est, 2)
    peso_max = round(24.9 * est * est, 2)

    # Peso ideal medio
    ideal = (peso_min + peso_max) / 2
    pct_ideal = round((peso / ideal) * 100, 1)

    # Calorías estimadas
    tmb = round(10*peso + 6.25*estatura_cm - 5*edad + 5, 2)
    kcal = round(tmb * 1.55)

    # Interpretación clínica
    estado, color, recomendaciones, riesgos = interpretar_imc(imc)

    return {
        "imc": imc,
        "estado": estado,
        "color": color,
        "peso_min": peso_min,
        "peso_max": peso_max,
        "pct_ideal": pct_ideal,
        "kcal": kcal,
        "recomendaciones": recomendaciones,
        "riesgos": riesgos
    }
