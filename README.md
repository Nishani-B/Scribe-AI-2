# Scribe AI — AI-Powered Clinical Documentation

Scribe AI is a web application designed to streamline clinical documentation by transforming doctor–patient conversations into structured **SOAP notes** using speech recognition and AI-assisted text processing.

The application provides a workflow for audio intake, transcription, transcript review, and structured clinical note generation. It aims to reduce manual documentation effort while keeping healthcare professionals responsible for reviewing and approving the generated notes.

## Features

- **User Authentication:** Login and registration interface.
- **Audio Upload and Transcription:** Convert supported consultation recordings into text using Whisper.
- **AI-Assisted SOAP Notes:** Organize consultation information into a structured clinical documentation format.
- **Transcript Review:** Review and confirm transcription results before using them for documentation.
- **Speaker Labelling:** Suggest doctor and patient labels, with options for manual correction.
- **Audio Validation:** Validate supported audio files for file type, size, duration, silence, and readability.
- **Privacy-Conscious Audio Processing:** The documented audio pipeline processes temporary audio files and removes them after processing rather than retaining the original audio.
- **Web Dashboard:** Access the documentation workflow through a browser.
- **API Documentation:** Explore available backend endpoints through FastAPI's interactive Swagger UI.

## Technology Stack

| Component | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, FastAPI |
| Speech Recognition | OpenAI Whisper |
| AI-Assisted Note Generation | Google Gemini API, where configured |
| Audio Processing | FFmpeg |
| API Documentation | FastAPI / Swagger UI |
| Version Control | Git and GitHub |

## How It Works

1. The user signs in to the application.
2. A supported consultation recording is uploaded, or a transcript is provided where supported.
3. The backend validates the input and processes the audio.
4. Speech recognition generates a transcript.
5. The transcript and speaker labels are reviewed and corrected where necessary.
6. The configured AI provider helps organize the consultation information into SOAP notes.
7. A healthcare professional reviews the generated documentation before clinical use.

## Understanding SOAP Notes

SOAP is a widely used format for organizing clinical documentation.

- **S — Subjective:** Symptoms and information reported by the patient.
- **O — Objective:** Available examination findings, observations, and measurements.
- **A — Assessment:** Clinical assessment based on the information provided.
- **P — Plan:** Proposed next steps, investigations, treatment, or follow-up for clinician review.

Scribe AI assists with documentation and does not replace professional medical judgement.

## Project Structure

The main project directories are organized as follows:

```text
Scribe-AI-2/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── ...
├── frontend/
│   └── ...
├── .gitignore
└── README.md
```

The backend contains the API and processing logic. The frontend contains the browser-based interface.

## Prerequisites

Install the following before running the project:

- Python 3.10 or a compatible version supported by the dependencies.
- Git.
- FFmpeg for audio decoding and transcription.
- A modern web browser.
- An API key for the configured AI provider, if required.

Verify your installations in PowerShell:

```powershell
python --version
git --version
ffmpeg -version
```

### Install FFmpeg on Windows

If FFmpeg is not installed and you have Windows Package Manager (`winget`), run:

```powershell
winget install Gyan.FFmpeg
```

Restart the terminal and verify the installation:

```powershell
ffmpeg -version
```

## Installation and Setup

### Step 1: Clone the Repository

Open a terminal in VS Code and run:

```powershell
git clone https://github.com/Nishani-B/Scribe-AI-2.git
cd Scribe-AI-2
```

If you already have the project on your computer, open the existing project folder instead.

### Step 2: Set Up the Backend

Open the first VS Code terminal at the project root and run:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If the Whisper package is not installed by the requirements file, install it in the same virtual environment:

```powershell
python -m pip install openai-whisper
```

Whisper may require additional build dependencies depending on your Python and Windows environment.

### Step 3: Configure Environment Variables

Check whether `backend/.env.example` exists. If it does, use it as the reference for the environment variables supported by your current backend.

Create `backend/.env` and provide the required values. For a setup using Gemini and Whisper, the configuration may look like this:

```dotenv
SCRIBE_ENV=dev
GEMINI_API_KEY=your_gemini_api_key
SCRIBE_SECRET_KEY=replace_with_a_random_secret_of_32_or_more_characters
SCRIBE_CORS_ORIGINS=http://localhost:5500,http://127.0.0.1:5500
SCRIBE_ASR_PROVIDER=whisper
WHISPER_MODEL=tiny
```

Use the variable names and values expected by your actual backend configuration. Do not copy example placeholders as real credentials.

**Security note:** Never commit `.env` files, API keys, authentication secrets, or real patient data to GitHub.

### Step 4: Run the Backend Server

In the **first terminal**, make sure you are inside the `backend` directory and that the virtual environment is activated.

Run:

```powershell
python -m uvicorn main:app --reload
```

The backend should start on:

- **API base URL:** http://127.0.0.1:8000
- **Interactive API documentation:** http://127.0.0.1:8000/docs

Keep this terminal open while using the application.

### Step 5: Run the Frontend

Open a **second VS Code terminal**. Starting from the project root, run:

```powershell
cd frontend
python -m http.server 5500
```

Open the application in your browser:

**http://localhost:5500**

Keep both terminals running:

- Terminal 1 runs the FastAPI backend.
- Terminal 2 serves the frontend.

If your frontend entry point or API URL differs from these assumptions, use the paths and settings configured in your current project.

### Step 6: Stop the Application

To stop either server, select its terminal and press:

```text
Ctrl + C
```

## Troubleshooting

### 1. PowerShell Blocks Virtual Environment Activation

If PowerShell prevents activation, you can use the virtual environment's Python executable directly from the `backend` directory:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Then start the backend with:

```powershell
.\.venv\Scripts\python.exe -m uvicorn main:app --reload
```

### 2. Whisper Is Not Installed

Activate the backend virtual environment and run:

```powershell
python -m pip install openai-whisper
```

Confirm that the package is installed in the same Python environment used to run the backend.

### 3. FFmpeg Is Not Found

Run:

```powershell
ffmpeg -version
```

If the command is not recognized, install FFmpeg and ensure its executable directory is included in the system PATH. Restart VS Code after changing PATH if necessary.

### 4. The Frontend Cannot Connect to the Backend

Check that:

- The backend is running on port `8000`.
- The frontend is running on port `5500`.
- The frontend is configured to call the correct backend API URL.
- The backend CORS configuration allows the frontend origin.

### 5. AI Note Generation Fails

Check that the required API key is configured correctly, the selected provider is enabled, and the backend terminal does not report an authentication, network, or provider error.

## Privacy and Responsible Use

Scribe AI is intended to assist with clinical documentation. Responsible use requires:

- Using synthetic or properly de-identified consultation data during development.
- Protecting API keys and authentication secrets.
- Verifying the data-handling requirements of any external AI provider before processing sensitive information.
- Reviewing transcripts and generated notes for omissions and inaccuracies.
- Obtaining appropriate consent and authorization before recording or processing consultations.
- Ensuring a qualified healthcare professional reviews and approves all clinical documentation.

Do not use the application as a substitute for medical diagnosis, treatment decisions, or professional judgement.

## Current Limitations

- Transcription accuracy depends on recording quality, accents, background noise, and the selected speech-recognition model.
- Speaker-role suggestions may require manual correction.
- AI-generated notes may omit, misinterpret, or incorrectly organize clinical information.
- Local setup and provider availability affect which features can be used.
- Real-world healthcare deployment requires appropriate privacy, security, reliability, and compliance validation.

## Future Enhancements

Potential improvements include:

- Exporting clinical notes to downloadable formats.
- Additional speech-recognition and AI providers.
- Enhanced speaker diarization.
- Electronic health record integration using appropriate healthcare interoperability standards.
- Secure deployment with stronger operational monitoring and access controls.

## Author

**Nishani Balaji**

GitHub: [Nishani-B](https://github.com/Nishani-B)

Project Repository: [Scribe-AI-2](https://github.com/Nishani-B/Scribe-AI-2)

---

*Built as an AI-assisted clinical documentation project. All generated clinical content requires professional review before use.*
