from flask import Flask, request, jsonify
from flask_cors import CORS

# ✅ Correct imports (no "backend." here)
from services.stt_service import transcribe_audio
from services.soap_service import generate_soap_note

app = Flask(__name__)
CORS(app)


# --------------------------------------------------
# Health check
# --------------------------------------------------
@app.route("/", methods=["GET"])
def health():
    return {"status": "Scribe AI backend running"}


# --------------------------------------------------
# STEP 1: Transcription
# --------------------------------------------------
@app.route("/transcribe", methods=["POST"])
def transcribe():
    try:
        if "audio" not in request.files:
            return jsonify({"error": "Audio file required"}), 400

        audio_file = request.files["audio"]
        transcript = transcribe_audio(audio_file)

        return jsonify({"transcript": transcript})

    except Exception as e:
        print("ERROR in /transcribe:", e)
        return jsonify({"error": str(e)}), 500


# --------------------------------------------------
# STEP 2: SOAP note generation
# --------------------------------------------------
@app.route("/generate-note", methods=["POST"])
def generate_note():
    try:
        data = request.get_json()

        if not data or "transcript" not in data:
            return jsonify({"error": "Transcript required"}), 400

        soap_note = generate_soap_note(data["transcript"])
        return jsonify(soap_note)

    except Exception as e:
        print("ERROR in /generate-note:", e)
        return jsonify({"error": str(e)}), 500


# --------------------------------------------------
# FINAL PIPELINE
# Audio → Transcript → SOAP
# --------------------------------------------------
@app.route("/process-audio", methods=["POST"])
def process_audio():
    try:
        if "audio" not in request.files:
            return jsonify({"error": "Audio file required"}), 400

        audio_file = request.files["audio"]

        # Step 1: Transcription
        transcript = transcribe_audio(audio_file)

        # Step 2: SOAP note
        soap_note = generate_soap_note(transcript)

        return jsonify({
            "transcript": transcript,
            "soap_note": soap_note
        })

    except Exception as e:
        print("ERROR in /process-audio:", e)
        return jsonify({"error": str(e)}), 500


# --------------------------------------------------
# Run app
# --------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)