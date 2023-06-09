
import requests
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def analise_sentimento(texto: str) -> str:
    try:
        chave_api = getenv("CHAVE_API", None)
        modelo_engine = "text-davinci-003"
        comando = (
            "Responda em uma única palavra, sendo positivo, "
            "negativo ou neutro o sentimento contido no seguinte "
            f"texto: '{texto}'"
        )

        cabecalho = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {chave_api}",
        }

        dados = {
            "prompt": comando,
            "temperature": 0.7,
            "max_tokens": 35,
            "n": 1,
            "stop": None,
        }

        reposta = requests.post(
            f"https://api.openai.com/v1/engines/{modelo_engine}/completions",
            headers=cabecalho,
            json=dados,
        )

        if reposta.status_code != 200:
            assert "indeterminado"

        return reposta.json()["choices"][0]["text"].strip().lower()
    
    except Exception as _:
        return "indeterminado"
