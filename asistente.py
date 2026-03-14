import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
API_KEY = os.getenv("GENAI_API_KEY")

client = genai.Client(api_key=API_KEY)

configuration = types.GenerateContentConfig(
    max_output_tokens=2048,
    system_instruction = """
<rol>
Eres un asistente experto en el Código Sustantivo del Trabajo de Colombia.
</rol>

<objetivo>
Analizar y responder preguntas del usuario interpretando su contenido.
</objetivo>

<reglas>
1. Prioriza siempre la información del CONTEXTO proporcionado.
2. Si el contexto no contiene la respuesta exacta, usa tu conocimiento
general del derecho para orientar al usuario.
3. No inventes leyes, artículos o normas inexistentes.
4. Explica las respuestas en lenguaje claro.
</reglas>

<formato>
Responde SIEMPRE en formato JSON:

{
 "respuesta": "explicación clara",
 "referencia": "artículo si existe",
 "interpretacion": "explicación breve del significado"
}
</formato>

<ejemplos>

Ejemplo 1

CONTEXTO:
'''
Artículo 186: Todo trabajador que haya prestado sus servicios durante un
año tiene derecho a quince (15) días hábiles consecutivos de vacaciones
remuneradas.
'''

Pregunta:
¿Cuántos días de vacaciones tiene un trabajador en Colombia?

Respuesta:
{
 "respuesta": "En Colombia, el trabajador tiene derecho a 15 días hábiles consecutivos de vacaciones remuneradas por cada año de servicio.",
 "referencia": "Artículo 186",
 "interpretacion": "La ley laboral colombiana establece el derecho mínimo anual a vacaciones pagadas."
}

Ejemplo 2

CONTEXTO:
'''
Artículo 134: El salario debe pagarse directamente al trabajador o a la
persona que él autorice por escrito.
'''

Pregunta:
¿El salario debe pagarse directamente al trabajador?

Respuesta:
{
 "respuesta": "Sí, el salario debe pagarse directamente al trabajador o a la persona que él autorice por escrito.",
 "referencia": "Artículo 134",
 "interpretacion": "La ley establece que el pago del salario debe hacerse directamente al trabajador."
}

Ejemplo 3

CONTEXTO:
'''
Artículo 161: La duración máxima de la jornada ordinaria de trabajo es
de ocho (8) horas al día y cuarenta y ocho (48) horas a la semana.
'''

Pregunta:
¿Cuántas horas puede trabajar una persona al día según la ley?

Respuesta:
{
 "respuesta": "La jornada ordinaria máxima es de 8 horas al día y 48 horas a la semana.",
 "referencia": "Artículo 161",
 "interpretacion": "La norma establece el límite legal de la jornada laboral."
}

Ejemplo 4

CONTEXTO:
'''
Artículo 64: En caso de terminación unilateral del contrato de trabajo
sin justa causa, el empleador debe pagar una indemnización al trabajador.
'''

Pregunta:
¿Qué pasa si el empleador despide a un trabajador sin justa causa?

Respuesta:
{
 "respuesta": "Si el empleador termina el contrato sin justa causa, debe pagar una indemnización al trabajador.",
 "referencia": "Artículo 64",
 "interpretacion": "La ley protege al trabajador frente a despidos injustificados."
}

</ejemplos>
"""
)

base_conocimiento = """
Código Sustantivo del Trabajo de Colombia

---------------------------------------------------

Jornada laboral

Artículo 161: La duración máxima de la jornada ordinaria de trabajo es
de ocho (8) horas al día y cuarenta y ocho (48) horas a la semana.

Artículo 159: Trabajo suplementario o de horas extras es el que excede
la jornada ordinaria de trabajo.

---------------------------------------------------

Salario

Artículo 127: Constituye salario no sólo la remuneración ordinaria fija
o variable, sino todo lo que recibe el trabajador en dinero o en especie
como contraprestación directa del servicio.

Artículo 134: El salario debe pagarse directamente al trabajador o a la
persona que él autorice por escrito.

---------------------------------------------------

Vacaciones

Artículo 186: Todo trabajador que haya prestado sus servicios durante
un año tiene derecho a quince (15) días hábiles consecutivos de
vacaciones remuneradas.

---------------------------------------------------

Terminación del contrato

Artículo 62: Son justas causas para dar por terminado unilateralmente
el contrato de trabajo por parte del empleador o del trabajador las
establecidas por la ley.

Artículo 64: En caso de terminación unilateral del contrato de trabajo
sin justa causa, el empleador debe pagar una indemnización al trabajador.

---------------------------------------------------

Obligaciones del empleador

Artículo 57: Son obligaciones especiales del empleador, entre otras,
pagar la remuneración pactada en las condiciones, períodos y lugares
convenidos.

---------------------------------------------------

Obligaciones del trabajador

Artículo 58: Son obligaciones especiales del trabajador cumplir las
órdenes e instrucciones del empleador relacionadas con el trabajo y
cuidar los bienes de la empresa.
"""

print("\n===============================")
print("ASISTENTE LEGAL / NORMATIVO IA")
print("Puedes preguntar sobre contratos o derechos laborales.")
print("Escribe 'salir' para terminar")
print("===============================\n")

while True:

    pregunta_usuario = input("Tu: ")

    if pregunta_usuario.lower() in ["salir", "exit", "quit"]:
        print("\nAsistente: Hasta luego.")
        break

    try:

        prompt = f"""
CONTEXTO DEL DOCUMENTO:
\"\"\"
{base_conocimiento}
\"\"\"

PREGUNTA DEL USUARIO:
{pregunta_usuario}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=configuration,
            contents=prompt
        )

        print("\nRespuesta del asistente:\n")
        print(response.text)
        print()

    except Exception as e:
        print("Error:", e)