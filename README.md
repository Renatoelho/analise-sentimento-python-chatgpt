# Como criar uma análise de sentimento utilizando o Python e ChatGPT-3

A análise de sentimento é uma técnica de processamento de linguagem natural que permite identificar a opinião expressa em um texto. Ela pode ser utilizada para entender a opinião dos clientes sobre um produto ou serviço, monitorar a reputação de uma marca ou empresa, ou até mesmo identificar tendências em redes sociais.

Neste tutorial, vamos utilizar a linguagem de programação Python e o modelo de linguagem natural ChatGPT, da OpenAI, para criar uma análise de sentimento simples.

## Passo 1: Instalar as dependências

Antes de começar, é necessário instalar algumas bibliotecas do Python. Para isso, abra o terminal ou prompt de comando e execute o seguinte comando:

```bash
pip install python-dotenv requests
```

Ou 

```bash
pip install -r requirements.txt
```

Isso instalará as bibliotecas Python-dotenv e Requests, que são necessárias para utilizar na análise.

## Passo 2: Criar uma função para análise de sentimento

Em seguida, vamos criar uma função que recebe um texto e retorna um outro texto que indica o sentimento expresso. Que pode ser positivo ,negativo ou um sentimento neutro.

Nesta função, utilizamos o modelo GPT-3 da OpenAI por meio da API para gerar uma saída a partir do texto de entrada. Em seguida, aplicamos essa função a um determinado texto e obtemos o resultado da análise de sentimento.

```python
import requests
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def analise_sentimento(texto: str) -> str:
    try:
        chave_api = getenv("CHAVE_API", None)
        modelo_engine = "text-davinci-003"
        comando = (
            "Faça uma análise de sentimento no "
            "seguinte texto e classifique em "
            f"positivo, negativo ou neutro: '{texto}'"
        )

        cabecalho = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {chave_api}",
        }

        dados = {
            "prompt": comando,
            "temperature": 0.7,
            "max_tokens": 100,
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

```

## Passo 3: Testar a função com exemplos

Para testar a função de análise de sentimento, podemos utilizar alguns exemplos simples de textos com diferentes sentimentos. Por exemplo:

```python
from avaliacoes_clientes import avaliacoes_clientes
from analise_sentimento import analise_sentimento

for texto in avaliacoes_clientes:
    sentimento = analise_sentimento(texto)
    print(f"'{texto}' é um sentimento: {sentimento}")
```

Este código vai imprimir o texto e o sentimento para cada um dos exemplos de texto. O resultado pode ser algo como:

```bash
'Adorei este produto!' é um sentimento: positivo.
'Ótima qualidade, superou minhas expectativas!' é um sentimento: positivo.
'Muito bom, recomendo!' é um sentimento: positivo.
'O produto atendeu às minhas expectativas.' é um sentimento: positivo.
'Nada de excepcional, mas não há nada de errado com ele.' é um sentimento: neutro.
'Não se deixe enganar pelas avaliações positivas.' é um sentimento: negativo.
'Produto de qualidade duvidosa.' é um sentimento: negativo
'Definitivamente não compraria novamente.' é um sentimento: negativo.
```

## Referência:

A documentação oficial da API do ChatGPT está disponível no site da OpenAI, no endereço https://beta.openai.com/docs/api-reference/introduction. Você encontrará informações detalhadas sobre como utilizar a API, incluindo exemplos de código em diferentes linguagens de programação, guias de integração e explicações sobre os parâmetros disponíveis.