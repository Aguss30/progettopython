import os
from flask import Flask, request, jsonify
from google import genai

app = Flask(__name__)
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

@app.route("/")
def home():
    return "Ciao, questa è la versione 2!"

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/analyze-logs", methods=["POST"])
def analyze_logs():
    dati = request.get_json()
    log_text = dati.get("logs", "") 

    prompt = f"""Sei un assistente per incident management.
Analizza questi log e rispondi in italiano con:
1. Cosa è successo (in breve)
2. Causa probabile
3. Un suggerimento per risolvere

LOG:
{log_text}"""
    
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return jsonify({"analisi": response.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)