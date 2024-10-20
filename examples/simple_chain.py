from llm_models.openai import create_model
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.chains.sequential import SimpleSequentialChain
from langchain.chains import LLMChain
from langchain.globals import set_debug

set_debug(True)
llm = create_model()

modelo_pais = ChatPromptTemplate.from_template(
    "Sugira um pais para iniciar nomadismo com budget inicial de  {budget}"
)

modelo_cidade = ChatPromptTemplate.from_template(
    "Sugira uma {cidade}"
)


cadeia_cidade = LLMChain(prompt=modelo_cidade, llm=llm)
cadeia_restaurantes = LLMChain(prompt=modelo_cidade, llm=llm)


cadeia = SimpleSequentialChain(
    chains=[cadeia_cidade, cadeia_restaurantes],)

result = cadeia.invoke("800 dolares mensais")

print(result)
