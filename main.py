# main.py

from langchain.agents import AgentExecutor
from agents.OpenAiAlunoAgent import AgenteOpenAIFunctions
from dotenv import load_dotenv

load_dotenv()
pergunta = "Em qual Ano Pedro ingressou?"
pergunta = "Quais os dados de Luiza e de Pedro?"
pergunta = "Quais os dados de Luiza e sua nota final?, se ela for superior a 7, diga que está aprovada"


agente = AgenteOpenAIFunctions()
executor = AgentExecutor(agent=agente.agente,
                         tools=agente.tools,
                         verbose=True)
resposta = executor.invoke({"input": pergunta})
print(resposta)
