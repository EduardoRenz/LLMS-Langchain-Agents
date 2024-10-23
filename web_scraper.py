# %%
from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import BeautifulSoupTransformer
from langchain.prompts import PromptTemplate
from llm_factory import create_model
import nest_asyncio
# %%
llm = create_model()
nest_asyncio.apply()
url = "https://www.sefaz.rs.gov.br/ASP/AAE_ROOT/NFE/SAT-WEB-NFE-NFC_2.asp?HML=false&chaveNFe=43240202721998000149650030000836801447941365"

loader = AsyncChromiumLoader(
    [url], user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36")
docs = loader.load()
transformer = BeautifulSoupTransformer()
fd = transformer.transform_documents(docs, tags_to_extract=["table"])

# %%
prompt = PromptTemplate.from_template(
    """Extraia apenas a tabela de itens de mercado, preco e quantidade e transforme em csv o seguinte input nao diga mais nada, apenas extria o csv puro pronto para ser jogado em um arquivo. 

    Adicione mais duas colunas no final, descricao reduzida e categoria, e preencha as
    As categorias disponiveis sao:
        -  alimentos
        -  bebidas
        -  limpeza
        -  higiene
        -  outros
        -  utensilhos

    A descricao reduzida deve ser em minusculo, sem acentos

    Nao coloque nenhum tipo de markdown, o csv tem que ser puro e pronto para uso
    Segue o input:
    --------
    {input}
    -------
    """
)

chain = prompt | llm

# %%
result = chain.invoke({"input": fd[0].page_content})

# %%
cleaned_result = result.content.replace(',', '.').replace(';', ',')
# Create a csv file
with open('output.csv', 'w') as f:
    f.write(cleaned_result)
# %%
print(result)

# %%
llm.invoke("Qual foi a ultima palavra dita por voce?")
