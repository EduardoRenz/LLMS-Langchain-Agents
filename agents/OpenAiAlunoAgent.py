# agente.py
from langchain.agents import create_openai_tools_agent
from langchain import hub
from langchain.agents import Tool
from chain_domains.Aluno import DadosDeEstudante
from llm_models.openai import create_model


class AgenteOpenAIFunctions:
    def __init__(self):
        llm = create_model()

        dados_de_estudante = DadosDeEstudante()
        self.tools = [
            Tool(name=dados_de_estudante.name,
                 func=dados_de_estudante.run,
                 description=dados_de_estudante.description)
        ]

        prompt = hub.pull("hwchase17/openai-functions-agent")
        self.agente = create_openai_tools_agent(llm, self.tools, prompt)
