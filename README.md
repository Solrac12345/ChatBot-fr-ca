# Chatbot FR-CA Interview Assistant

Voice-based interview practice assistant in Quebec French (`fr-CA`) using Azure Speech Services.

## Features

- Asks interview questions in French Canadian using text-to-speech (TTS)
- Listens to spoken answers with speech-to-text (STT)
- Gives simple feedback on answer quality (length, connectors, vocabulary)
- Generates a corrected version of the answer
- Provides a professional suggested answer for each question

## Requirements

- Windows with PowerShell
- Python 3.10+ (3.11 recommended)
- Azure Speech resource (key + region)
- Microphone and speakers/headphones

## Installation

1. Clone this repository.
2. Open PowerShell in the project folder.
3. Run the setup script:

```powershell
.\setup.ps1
```

If script execution is blocked, run PowerShell as your user and allow local scripts:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
```

## Configure Azure Credentials

Set these environment variables before running the app:

- `AZURE_SPEECH_KEY`
- `AZURE_SPEECH_REGION`

### Temporary (current PowerShell session)

```powershell
$env:AZURE_SPEECH_KEY = "your_key_here"
$env:AZURE_SPEECH_REGION = "your_region_here"
```

### Persistent (for your user account)

```powershell
[System.Environment]::SetEnvironmentVariable("AZURE_SPEECH_KEY", "your_key_here", "User")
[System.Environment]::SetEnvironmentVariable("AZURE_SPEECH_REGION", "your_region_here", "User")
```

Then restart PowerShell.

## Run the Project

Activate the virtual environment (if not already active):

```powershell
.\venv\Scripts\Activate.ps1
```

Run the app:

```powershell
python .\main.py
```

## Build Executable (Optional)

This repository includes `build.ps1` for PyInstaller-based packaging:

```powershell
.\build.ps1
```

If you use this step, ensure your PyInstaller spec/config is present and correct for your environment.

## Project Structure

- `main.py` - entry point; starts interview flow
- `modules/interview.py` - orchestrates question/answer loop
- `modules/speech_utils.py` - Azure speech init, TTS, and STT helpers
- `modules/feedback.py` - rule-based feedback for responses
- `modules/correction.py` - answer rewriting/correction logic
- `modules/suggestions.py` - suggested answer selection from JSON
- `questions.json` - interview questions
- `suggestions.json` - model suggested answers
- `setup.ps1` - local environment setup
- `build.ps1` - executable build script
- `requirements.txt` - Python dependencies

## Troubleshooting

- **Missing Azure credentials**  
  Ensure both `AZURE_SPEECH_KEY` and `AZURE_SPEECH_REGION` are set.

- **No audio input detected**  
  Verify microphone permissions in Windows and set your default input device.

- **No speech output**  
  Check system output device and volume.

- **Dependency issues**  
  Re-run:
  ```powershell
  pip install --upgrade pip
  pip install -r requirements.txt
  ```

## Notes

- The current default run in `main.py` uses one interview round (`rounds=1`).
- Question and suggestion content is in French and can be customized in JSON files.
