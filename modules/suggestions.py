"""
EN: Module for loading and selecting suggested answers.
FR: Module pour charger et sélectionner les réponses suggérées.
"""

import json
import unicodedata
import sys
import os

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)



def load_suggestions():
    """
    EN: Load suggested answers from a JSON file.
    FR: Charger les réponses suggérées depuis un fichier JSON.
    """
    path = resource_path("suggestions.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("suggestions", [])



def normalize_text(text):
    """
    EN: Normalize text by removing accents and converting to lowercase.
    FR: Normaliser le texte en retirant les accents et en mettant en minuscules.
    """
    text = text.lower()
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return text


def suggest_answer(question, suggestions_dict):
    """
    EN: Return a suggested answer based on robust keyword matching.
    FR: Retourner une réponse suggérée selon une correspondance robuste de mots-clés.
    """

    normalized_question = normalize_text(question)

    for key, suggestion in suggestions_dict.items():
        normalized_key = normalize_text(key)

        # EN: If the normalized key is contained in the normalized question → match
        # FR: Si la clé normalisée est contenue dans la question normalisée → correspondance
        if normalized_key in normalized_question:
            return suggestion

    # Default fallback
    return (
        "Pour cette question, vous pouvez donner un exemple concret de votre expérience, "
        "expliquer votre rôle et décrire le résultat obtenu."
    )
