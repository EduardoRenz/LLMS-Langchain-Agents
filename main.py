# main.py
# %%
from langchain.agents import AgentExecutor
from agents.AlunoAgent import AlunoAgent
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

# %%
agente = AlunoAgent()
executor = AgentExecutor(agent=agente.agente, tools=agente.tools, verbose=True)

# %%
pergunta = "Me traga as notas finais de Luiza e de Tafarel"

resposta = executor.invoke({"input": pergunta})
print(resposta)

# %%
print(resposta['output'])
# %%
