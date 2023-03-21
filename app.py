
from avaliacoes_clientes import avaliacoes_clientes
from analise_sentimento import analise_sentimento

for texto in avaliacoes_clientes:
    sentimento = analise_sentimento(texto)
    print(f"'{texto}' é um sentimento: {sentimento}")