# main.py
# %%
from langchain.agents import AgentExecutor
from agents.OpenAiAlunoAgent import AlunoAgent
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
resposta['output']
# %%
