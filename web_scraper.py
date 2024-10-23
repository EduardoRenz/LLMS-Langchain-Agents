# %%
from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import Html2TextTransformer
from langchain.prompts import PromptTemplate
from llm_models.openai import create_model
import nest_asyncio
# %%
llm = create_model()

nest_asyncio.apply()
url = "https://www.sefaz.rs.gov.br/ASP/AAE_ROOT/NFE/SAT-WEB-NFE-NFC_2.asp?HML=false&chaveNFe=43240313891196000101650010000859501401545934"

loader = AsyncChromiumLoader(
    [url], user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36")
docs = loader.load()
tt = Html2TextTransformer()
fd = tt.transform_documents(docs)

# %%
prompt = PromptTemplate.from_template(
    """Extraia apenas a tabela de itens de mercado, preco e quantidade e transforme em csv o seguinte input nao diga mais nada, apenas extria o csv puro pronto para ser jogado em um arquivo, sem por markdown: 

    Adicione mais duas colunas no final, descricao reduzida e categoria, e preencha as
    --------
    {input}
    -------
    """
)


chain = prompt | llm
# %%

result = chain.invoke({"input": fd[0].page_content})
# %%
# Create a csv file
with open('output.csv', 'w') as f:
    f.write(result.content)
# %%
