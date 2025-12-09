import requests

# ===== CONFIGURACIÓN DE WHATSAPP CLOUD API =====
TOKEN = "EAARYBfydR9sBQE0xZAQLZBmtDx08MR04ASRpyYldNkkcUvhk9cFBRuZCmXtnCbI6K50B3j0jlwaMifvMxQUmdlykIAYi18lJXQX7BZCGgMistEh10Uny114Fn47CNq66042vLAp9WtJjqUj6mPbjC1gBblVKkcUeARSYwOBmyZBoRRcphLRifdCJak0oTZCFpfihNDvhTmlRvV719Q8Glx3ro72o8qTZBvV2FImlHORFn7Pyjj0jZBW4qikHBX39qNUx90qpU5yYBfQnn4SI2nZC6gecT"   # Token temporal (24 horas)
PHONE_NUMBER_ID = "825020954038229"  # Este es fijo para tu app

def enviar_whatsapp(numero, mensaje):
    """
    Envía un mensaje de texto a un número de WhatsApp usando la API oficial de Meta.
    """
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "text",
        "text": {"body": mensaje}
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
