#  CAREEGAR DADOS.

import json
import pandas as pd
import requests
import streamlit as st

# CONFIGURAÇÃO.
OLLAMA_URL =
MODELO = ""


perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/tarnsacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# MONTAR CONTEXTO.
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMONIO:  R$ {perfil['patrimonio_total']} | RESERVA {perfil['reserva_emergencia_atual']}

TRANSACOES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONIVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# SYSTEM PROMPT.
SYSTEM_PROMPT = """Você é o Max um educador finánceiro  amigavél e didático.

OBJETIVO:
Ensinar conceitos de finanças pessoais de forma simples, usando dados do cliente como exemplos práticos.

REGRAS:
- NUNCA recomende investimentos específicos, apenas explique como funciona;
- JAMAIS responda perguntas fora do tema ensino de finanças pessoais.
Quando ocorrer, responda lembrando seu papel de educador financeiro;
- Use os dados fornecidos para dar exemplos personalizados;
- Linguagem simples, como se explicasse para um amigo;
- Se não souber algo, adimita: "Não tenho essa informação, mas posso explicar...";
- Sempre pergunte ao cliente entendeu;
- Responda de forma sucinta e direta, com no máximo 3 paragrafos.
"""

# CHAMAR O OLLAMA.
def perguntar (msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json{"mode1": MODELO, "prompt": prompt, "stream": False})
    return r.json() ['response']

# INTERFACE.

st.title ("Max, seu educador financeiro")

if pergunta := st.chat_input("Sua duvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assintant").write(perguntar(pergunta))
