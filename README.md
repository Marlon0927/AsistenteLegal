# Asistente Legal Laboral con IA ⚖️ 

Un asistente conversacional desarrollado en **Python** que responde preguntas sobre el **Código Sustantivo del Trabajo de Colombia** utilizando el modelo **Gemini** de Google.

El sistema analiza una **base de conocimiento jurídica** y genera respuestas estructuradas en **formato JSON**, proporcionando:

* Explicación clara
* Referencia al artículo legal
* Interpretación del significado de la norma

#Características

* Consulta normativa laboral colombiana
* Integración con el modelo **Gemini**
* Uso de contexto legal para mejorar la precisión
* Respuestas estructuradas en JSON
* Manejo seguro de API Keys con variables de entorno
* Interfaz simple en consola

# Arquitectura del Proyecto

El sistema sigue una estructura simple:
1. **Base de conocimiento**
   * Contiene artículos del Código Sustantivo del Trabajo.

2. **Configuración del modelo**
   * Define el rol del asistente.
   * Establece reglas de interpretación jurídica.

3. **Prompt dinámico**
   * Combina el contexto legal con la pregunta del usuario.

4. **Modelo de IA**
   * Genera la respuesta basada en el contexto.

5. **Salida estructurada**
   * Respuesta generada en formato JSON.

# Tecnologías utilizadas

* Python
* Gemini API
* dotenv
* Procesamiento de prompts

# Ejecucion


Crear entorno virtual
- python -m venv env

Activar entorno:
- env\Scripts\activate

Instalar dependencias

-pip install -r requirements.txt

# Configuración de API Key

El proyecto utiliza **variables de entorno** para manejar la clave de la API.
- Crear un archivo `.env` en la raíz del proyecto:
- GENAI_API_KEY=tu_api_key_aqui


# Ejecución del programa

Ejecutar el script principal:

- python asistente.py

ASISTENTE LEGAL / NORMATIVO IA
Puedes preguntar sobre contratos o derechos laborales.
Escribe 'salir' para terminar

Ejemplo: 

Tu: ¿Cuántos días de vacaciones tiene un trabajador?

Respuesta:
{
 "respuesta": "En Colombia el trabajador tiene derecho a 15 días hábiles consecutivos de vacaciones remuneradas por cada año de servicio.",
 "referencia": "Artículo 186",
 "interpretacion": "La ley laboral establece el derecho mínimo anual a vacaciones pagadas."
}


