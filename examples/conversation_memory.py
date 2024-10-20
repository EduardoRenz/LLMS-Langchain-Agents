from llm_models.openai import create_model
from langchain.globals import set_debug
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryMemory
from langchain_core.runnables.history import RunnableWithMessageHistory

set_debug(False)
llm = create_model()

mensagens = [
    "Quero fazer uma viagem pela Patagonia, com roteiro de 20 dias",
    "Crie o ranking das 3 princiapais cidades",
    "Qual é o melhor período do ano para visitar em termos de clima? gostaria que fosse temperaturas mais quentes para trilhas",
    "Quanto devo esperar gastar?",
    "Na primeira cidade que você sugeriu lá atrás, quero saber 5 restaurantes para visitar. Responda somente o nome da cidade e o nome dos restaurantes.",
]

memory = ConversationSummaryMemory(llm=llm)

conversation = ConversationChain(llm=llm, verbose=False, memory=memory)

for mensagem in mensagens:
    response = conversation.predict(input=mensagem)
    print(response)
