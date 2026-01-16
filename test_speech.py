import os
import azure.cognitiveservices.speech as speechsdk

# Obtener las variables de entorno
key = os.getenv("AZURE_SPEECH_KEY")
region = os.getenv("AZURE_SPEECH_REGION")

if not key or not region:
    raise ValueError("Faltan AZURE_SPEECH_KEY o AZURE_SPEECH_REGION en variables de entorno.")

# Configurar Speech
speech_config = speechsdk.SpeechConfig(subscription=key, region=region)
speech_config.speech_synthesis_voice_name = "fr-CA-SylvieNeural"

synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

texto = "Bonjour Carlos, ceci est un test de la voix en français canadien."

result = synthesizer.speak_text_async(texto).get()

if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Síntesis OK: deberías haber escuchado la voz.")
else:
    print("Error de síntesis:", result.reason)
