from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from llm_factory import create_model
from langchain.tools import BaseTool
import json
from pydantic import BaseModel, Field
from repositories.aluno_repository import get_aluno, get_nota_final


class Aluno(BaseModel):
    nome: str = Field(
        "Nome do estudante informado, sempre em letras minúsculas. Exemplo: joão, carlos, joana, carla.")
    email: str = Field("Email do estudante")
    matricula: str = Field("Matricula do estudante")
    ano: int = Field("Ano de ingresso do estudante")


class NotaFinal(BaseModel):
    nome: str = Field(
        "Nome do estudante informado, sempre em letras minúsculas. Exemplo: joão, carlos, joana, carla.")
    nota: float = Field("Nota final do estudante")


class DadosDeEstudante(BaseTool):
    name: str = "DadosDeEstudante"
    description: str = """Esta ferramenta extrai o histórico e preferências de um estudante de acordo com seu histórico."""

    def _run(self, input: str) -> str:
        llm = create_model()
        parser = JsonOutputParser(pydantic_object=Aluno)
        template = PromptTemplate(template="""Você deve analisar a {input} e extrair o nome de usuário informado.
                        Formato de saída:
                        {formato_saida}""",
                                  input_variables=["input"],
                                  partial_variables={"formato_saida": parser.get_format_instructions()})
        cadeia = template | llm | parser
        resposta = cadeia.invoke({"input": input})
        nome_aluno = resposta['nome'].lower()
        dados = get_aluno(nome_aluno)
        return json.dumps(dados)


class DadosNotaFinal(BaseTool):
    name: str = "DadosNotaFinal"
    description: str = """Esta ferramenta extrai a nota final do ano letivo dado um nome do aluno."""

    def _run(self, input: str) -> str:
        llm = create_model()
        parser = JsonOutputParser(pydantic_object=NotaFinal)
        template = PromptTemplate(template="""Você deve analisar a {input} e extrair o nome de usuário informado.
                        Formato de saída:
                        {formato_saida}""",
                                  input_variables=["input"],
                                  partial_variables={"formato_saida": parser.get_format_instructions()})
        cadeia = template | llm | parser
        resposta = cadeia.invoke({"input": input})
        nome_aluno = resposta['nome'].lower()
        dados = get_nota_final(nome_aluno)
        return json.dumps(dados)
