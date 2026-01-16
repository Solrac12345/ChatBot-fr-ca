"""
EN: Module for correcting the user's spoken answer.
FR: Module pour corriger la réponse orale de l'utilisateur.
"""

def correct_answer(text):
    """
    EN: Produce a corrected version of the user's answer.
        Light correction: grammar, clarity, structure.
    FR: Produire une version corrigée de la réponse de l'utilisateur.
        Correction légère : grammaire, clarté, structure.
    """

    if not text or len(text.strip()) < 3:
        return "Je n'ai pas assez d'information pour corriger la réponse."

    corrected = text.strip()

    # Capitalize first letter
    corrected = corrected[0].upper() + corrected[1:]

    # Ensure sentence ends with a period
    if not corrected.endswith("."):
        corrected += "."

    # Basic replacements (expandable)
    replacements = {
        " probleme": " problème",
        " mecanique": " mécanique",
        " intelligence artificielle": " intelligence artificielle",
        " robotique": " robotique",
        " cloud": " cloud",
        " python": " Python",
        " java": " Java"
    }

    for wrong, right in replacements.items():
        corrected = corrected.replace(wrong, right)

    return corrected