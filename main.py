import os
from dotenv import load_dotenv

# Carrega o arquivo de configuração padrão
load_dotenv()

from fastapi import FastAPI, UploadFile, File, Form
import google.genai as genai
from google.genai import types

app = FastAPI(title="Cérebro M&M Soluções Inovadoras")

# Agora o sistema vai encontrar a chave perfeitamente
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))



PROMPT_SOCIO = (
    "Você é o sócio co-fundador da M&M Soluções Inovadoras. Seu parceiro é um desenvolvedor "
    "Full Stack experiente. Seja direto, focado em arquitetura limpa, escalabilidade e "
    "negócios. Sempre proponha o próximo passo prático de forma pragmática."
)

@app.post("/api/brain")
async def process_brain_input(
    text: str = Form(None),
    audio: UploadFile = File(None)
):
    contents = []

    if audio:
        audio_path = f"temp_{audio.filename}"
        with open(audio_path, "wb") as buffer:
            buffer.write(await audio.read())
            
        audio_uploaded = client.files.upload(file=audio_path)
        contents.append(audio_uploaded)
        os.remove(audio_path)

    if text:
        contents.append(text)

    if not contents:
        return {"error": "Nenhum comando de texto ou áudio foi enviado."}

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=contents,
        config=types.GenerateContentConfig(
            system_instruction=PROMPT_SOCIO,
        ),
    )

    return {
        "resposta_socio": response.text
    }
