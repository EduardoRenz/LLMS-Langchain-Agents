# main.py
# %%
from langchain.agents import AgentExecutor
from agents.AlunoAgent import AlunoAgent
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationBufferMemory
from langchain.schema import SystemMessage
from dotenv import load_dotenv
load_dotenv()


memory = ConversationBufferMemory(
    return_messages=True, memory_key='chat_history')

memory.chat_memory.add_message(SystemMessage(
    content="Voce é um assitente da escola, e só sabe responder perguntas sobre os alunos"))

# %%
agente = AlunoAgent()
executor = AgentExecutor.from_agent_and_tools(
    agent=agente.agente,
    tools=agente.tools,
    memory=memory,
    handle_parsing_errors=True,
    verbose=True)

# %%
pergunta = "Me traga as notas finais de Luiza e de Tafarel"

resposta = executor.invoke({"input": pergunta})
print(resposta)

# %%
print(resposta['output'])
# %%
