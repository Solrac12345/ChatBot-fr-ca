"""
EN: Module for evaluating user answers.
FR: Module pour évaluer les réponses de l'utilisateur.
"""

def evaluate_answer(text):
    """
    EN: Provide feedback on length, clarity, and vocabulary.
    FR: Fournir une rétroaction sur la longueur, la clarté et le vocabulaire.
    """
    words = text.split()
    length = len(words)
    feedback = []

    # Length
    if length == 0:
        feedback.append("Je n'ai pas reçu de réponse.")
    elif length < 8:
        feedback.append("Ta réponse est trop courte, ajoute plus de détails.")
    elif length < 20:
        feedback.append("Bonne base, mais développe avec des exemples concrets.")
    else:
        feedback.append("Bonne longueur pour une réponse d'entrevue.")

    # Connectors
    connectors = ["parce que", "donc", "ensuite", "premièrement", "finalement"]
    lower = text.lower()

    if any(c in lower for c in connectors):
        feedback.append("Bonne structure, tu utilises des connecteurs.")
    else:
        feedback.append("Ajoute des connecteurs comme 'parce que', 'ensuite', 'finalement'.")

    # Professional vocabulary
    pro_words = ["expérience", "projet", "résultat", "équipe", "objectif", "défi"]
    if any(w in lower for w in pro_words):
        feedback.append("Bon vocabulaire professionnel.")
    else:
        feedback.append("Essaie d'utiliser plus de vocabulaire professionnel.")

    return feedback