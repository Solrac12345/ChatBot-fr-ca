"""
EN: Module for correcting the user's spoken answer.
FR: Module pour corriger la réponse orale de l'utilisateur.
"""

def correct_answer(answer: str, question_type: str = "general") -> str:
    """
    EN: Advanced rewriting engine for Quebec French interview answers.
    FR: Moteur avancé de réécriture pour réponses d'entrevue en français québécois.
    
    - Corrige erreurs grammaticales simples
    - Améliore vocabulaire professionnel
    - Adapte le ton selon le type de question
    - Produit une réponse naturelle de 20–25 mots
    """

    if not answer or len(answer.strip()) < 3:
        return "Je n’ai pas bien compris ta réponse, pourrais-tu reformuler brièvement?"

    text = answer.strip()

    # ============================================================
    # 1. RULE-BASED GRAMMAR FIXES (simple linguistic corrections)
    # ============================================================
    grammar_rules = {
        "je suis travailler": "je travaille",
        "je suis appris": "j’ai appris",
        "je suis fait": "j’ai réalisé",
        "je attire": "je suis attiré par",
        "je veux travailler": "je souhaite travailler",
        "dans le marché": "sur le marché",
        "au défi": "au défi de",
    }

    for wrong, correct in grammar_rules.items():
        text = text.replace(wrong, correct)

    # ============================================================
    # 2. VOCABULARY ENRICHMENT (statistical-style transformations)
    # ============================================================
    enrich = {
        "projet": "mandat concret",
        "travail": "milieu professionnel",
        "expérience": "expérience pertinente",
        "compétences": "compétences techniques et humaines",
        "équipe": "équipe multidisciplinaire",
        "important": "essentiel",
        "difficile": "complexe",
        "intéressant": "stimulant",
    }

    for basic, rich in enrich.items():
        text = text.replace(basic, rich)

    # ============================================================
    # 3. TONE ADAPTATION BASED ON QUESTION TYPE
    # ============================================================
    tones = {
        "tech": (
            "Je mets l’accent sur la rigueur, l’automatisation et la résolution efficace de problèmes "
            "dans un contexte technologique québécois."
        ),
        "comportementale": (
            "J’accorde une grande importance à la collaboration, à l’adaptabilité et à la communication claire "
            "au sein d’équipes multidisciplinaires."
        ),
        "leadership": (
            "J’aime mobiliser les équipes, clarifier les objectifs et favoriser un climat de confiance "
            "pour atteindre des résultats concrets."
        ),
        "general": (
            "Je valorise la collaboration, la rigueur et l’amélioration continue dans le milieu professionnel québécois."
        ),
    }

    tone = tones.get(question_type, tones["general"])

    # ============================================================
    # 4. FINAL REWRITE (20–25 words)
    # ============================================================
    # Combine corrected text + tone, then compress to 20–25 words
    combined = f"{text}. {tone}"

    words = combined.split()
    if len(words) > 25:
        combined = " ".join(words[:25])
    elif len(words) < 20:
        combined += " Je m’assure toujours de contribuer de façon professionnelle."

    return combined.strip()