from modules.interview import run_interview

if __name__ == "__main__":
    try:
        run_interview(rounds=1)
    except KeyboardInterrupt:
        print("\nProgramme annulé par l'utilisateur.")
        # EN: Remember to use FR: Rappelez utiliser
        # .\venv\Scripts\Activate.ps1
        # .\build.ps1
        # EN: Update .exe FR: Mets a jour
