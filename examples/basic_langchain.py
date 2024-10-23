from langchain.prompts.prompt import PromptTemplate
from llm_factory import create_model

llm = create_model()

# Opcional, cria um template de prompt, bom quando tem palavaras chaves
prompt_model = PromptTemplate.from_template(
    "Message: {message}\n"
)

prompt = prompt_model.format(message="Hello")
print(prompt)
response = llm.invoke(prompt)

print(response.content)
