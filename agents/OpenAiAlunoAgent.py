# agente.py
from langchain.agents import create_openai_tools_agent, create_react_agent
from langchain import hub
from langchain.agents import Tool
from chain_domains.Aluno import DadosDeEstudante, DadosNotaFinal
from llm_factory import create_model


class AlunoAgent:
    def __init__(self):
        llm = create_model()

        dados_de_estudante = DadosDeEstudante()
        dados_nota_final = DadosNotaFinal()
        self.tools = [
            Tool(name=dados_de_estudante.name,
                 func=dados_de_estudante.run,
                 description=dados_de_estudante.description),
            Tool(name=dados_nota_final.name,
                 func=dados_nota_final.run,
                 description=dados_nota_final.description),
        ]

        prompt = hub.pull("hwchase17/openai-functions-agent")
        # prompt = hub.pull("hwchase17/react")
        self.agente = create_openai_tools_agent(llm, self.tools, prompt)
        # self.agente = create_react_agent(llm, self.tools, prompt)
