# test rebuild

"""
EN: Interview orchestration module.
FR: Module d'orchestration de l'entrevue.
"""

import json
import random

from modules.speech_utils import init_speech_services, speak_text, listen_continuous
from modules.feedback import evaluate_answer
from modules.suggestions import load_suggestions, suggest_answer
from modules.correction import correct_answer

import sys
import os

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)



# ============================================================
#  LOAD QUESTIONS
#  EN: Load interview questions from JSON file
#  FR: Charger les questions d'entrevue depuis un fichier JSON
# ============================================================

def load_questions():
    """
    EN: Load questions from a JSON file.
    FR: Charger les questions depuis un fichier JSON.
    """
    path = resource_path("questions.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("questions", [])



# ============================================================
#  INTERVIEW LOGIC
#  EN: Main interview loop
#  FR: Boucle principale de l'entrevue
# ============================================================

def run_interview(rounds=3):
    """
    EN: Run the full interview simulation.
    FR: Exécuter la simulation complète d'entrevue.
    """

    # Load questions and suggestions
    questions = load_questions()
    suggestions_dict = load_suggestions()

    if not questions:
        print("No questions found in questions.json")
        return

    # Initialize Azure speech services
    synthesizer, recognizer = init_speech_services()

    # Greeting
    speak_text(synthesizer, "Bonjour Carlos. Commençons l'entrevue en français québécois.")

    for i in range(1, rounds + 1):
        print(f"\n--- Question {i} ---")

        # Select a random question
        question = random.choice(questions)
        #print("Question:", question)
        speak_text(synthesizer, question)

        # Listen until silence (10 seconds)
        answer = listen_continuous(recognizer)

        # ============================================================
        #  HANDLE SILENCE
        # ============================================================
        if answer == "__NO_SPEECH__":
            print("\nNo speech detected.")
            speak_text(synthesizer, "Je n'ai rien entendu... Cependant ici une petite suggestion.")

            suggested = suggest_answer(question, suggestions_dict)
            print("\nSuggested answer:")
            #print(suggested)
            speak_text(synthesizer, suggested)

            continue  # Move to next question

        # ============================================================
        #  HANDLE VOICE CANCEL
        # ============================================================
        if answer == "__CANCEL__":
            print("Interview canceled by voice command.")
            speak_text(synthesizer, "Programme annulé. À bientôt Carlos.")
            break

        print("\nYour answer:")
        print(answer)

        # ============================================================
        #  FEEDBACK
        # ============================================================
        feedback_list = evaluate_answer(answer)
        print("\nFeedback:")
        for fb in feedback_list:
            print("-", fb)

        speak_text(
            synthesizer,
            "Merci pour ta réponse. Voici quelques commentaires pour t'aider à t'améliorer."
        )

        # ============================================================
        #  CORRECTION
        # ============================================================
        corrected = correct_answer(answer)

        print("\nCorrected version:")
        print(corrected)

        speak_text(synthesizer, "Voici une version corrigée de ta réponse.")
        speak_text(synthesizer, corrected)

        # ============================================================
        #  SUGGESTED MODEL ANSWER
        # ============================================================
        suggested = suggest_answer(question, suggestions_dict)

        print("\nSuggested answer:")
        print(suggested)

        speak_text(synthesizer, "Et maintenant, voici une suggestion professionnelle.")
        speak_text(synthesizer, suggested)

    # Closing message
    speak_text(synthesizer, "Merci Carlos. L'entrevue est terminée. Bonne journée!")