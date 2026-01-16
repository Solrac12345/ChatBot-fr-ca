"""
EN: Speech utilities module for TTS and STT using Azure Speech SDK.
FR: Module utilitaire pour la synthèse et la reconnaissance vocale avec Azure Speech SDK.
"""

import os
import time
import azure.cognitiveservices.speech as speechsdk


# ============================================================
#  AZURE SPEECH INITIALIZATION
#  EN: Initialize Azure Speech configuration
#  FR: Initialiser la configuration Azure Speech
# ============================================================

def init_speech_services():
    """
    EN: Load Azure credentials and initialize TTS and STT services.
    FR: Charger les identifiants Azure et initialiser les services TTS et STT.
    """

    speech_key = os.getenv("AZURE_SPEECH_KEY")
    speech_region = os.getenv("AZURE_SPEECH_REGION")

    if not speech_key or not speech_region:
        raise ValueError("Azure Speech credentials missing. Set AZURE_SPEECH_KEY and AZURE_SPEECH_REGION.")

    # EN: Configure speech settings
    # FR: Configurer les paramètres vocaux
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
    speech_config.speech_recognition_language = "fr-CA"
    speech_config.speech_synthesis_voice_name = "fr-CA-SylvieNeural"

    # EN: Create synthesizer (speaker output)
    # FR: Créer le synthétiseur (sortie haut-parleur)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    # EN: Create recognizer (microphone input)
    # FR: Créer le reconnaisseur (entrée microphone)
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    return synthesizer, recognizer


# ============================================================
#  TEXT-TO-SPEECH
#  EN: Make the bot speak using Azure TTS
#  FR: Faire parler le bot avec Azure TTS
# ============================================================

def speak_text(synthesizer, text):
    """
    EN: Speak text using Azure TTS.
    FR: Lire un texte à voix haute avec Azure TTS.
    """
    print(f"[BOT] {text}")
    result = synthesizer.speak_text_async(text).get()

    if result.reason != speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("TTS error:", result.reason)


# ============================================================
#  CONTINUOUS SPEECH-TO-TEXT (2 MINUTES + CANCEL)
#  EN: Listen continuously for up to 120 seconds with voice cancel
#  FR: Écouter en continu pendant 120 secondes avec annulation vocale
# ============================================================

def listen_continuous(recognizer, silence_limit_sec=10):
    """
    EN: Listen continuously until silence is detected for 'silence_limit_sec' seconds.
    FR: Écouter en continu jusqu'à ce qu'un silence de 'silence_limit_sec' secondes soit détecté.
    """

    print("Listening...")

    full_text = []
    done = False
    last_speech_time = time.time()

    def on_recognized(evt):
        nonlocal done, last_speech_time
        text = evt.result.text

        if text:
            last_speech_time = time.time()
            lower = text.lower()
            print("Recognized:", text)

            if "cancelar" in lower or "fermer" in lower or "stop" in lower:
                full_text.append("__CANCEL__")
                done = True
                return

            full_text.append(text)

    def on_stop(evt):
        nonlocal done
        done = True

    recognizer.recognized.connect(on_recognized)
    recognizer.session_stopped.connect(on_stop)
    recognizer.canceled.connect(on_stop)

    recognizer.start_continuous_recognition()

    while not done:
        time.sleep(0.5)

        if time.time() - last_speech_time > silence_limit_sec:
            recognizer.stop_continuous_recognition()
            return "__NO_SPEECH__"

    recognizer.stop_continuous_recognition()

    if "__CANCEL__" in full_text:
        return "__CANCEL__"

    final_text = " ".join(full_text).strip()
    return final_text

def listen_once(recognizer):
    print("Listening...")
    result = recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        text = result.text.strip()
        print(f"Recognized: {text}")
        return text

    print("No speech detected.")
    return ""