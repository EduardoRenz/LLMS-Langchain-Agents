from chain_domains.Place import Place
from llm_models.openai import create_model
from langchain.prompts.prompt import PromptTemplate

from langchain.globals import set_debug
from langchain_core.output_parsers import JsonOutputParser

set_debug(True)
llm = create_model()

parser = JsonOutputParser(pydantic_object=Place)

prompt = PromptTemplate.from_template(
    template="Sugira um pais para iniciar nomadismo com budget inicial de  {budget}, retorne apenas o nome do pais e uma cidade indicada pelo nome do pais. deve retornar no formato {formatacao_de_saida}",
    partial_variables={
        "formatacao_de_saida": parser.get_format_instructions()},
)

chain = prompt | llm | parser
result = chain.invoke("800 dolares")


print(result)
