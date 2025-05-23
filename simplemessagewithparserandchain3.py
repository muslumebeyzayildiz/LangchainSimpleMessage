from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model = ChatOpenAI(model="gpt-4")

messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

parser = StrOutputParser()

#LCEL Chainler izincirleri bir birne bağlamka için. aşağıda da bunu kullanmımş olyorum.
chain = model | parser# bir model var çıktısını parsera ver diyorum



if __name__ == "__main__":
    print(chain.invoke(messages))