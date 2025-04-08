from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate #message=[SystemMessage(),HumanMessage()] yerine kullnamak için
#

load_dotenv()
model = ChatOpenAI(model="gpt-4")

#dinamik bir şekilde
system_template = "Translate the following into {language}:"

#kullanıcının söyleyeceği kısım:
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)
#hangi dile çevireceği language DİNAMİK oldu ** ve kullanıcın yazacağı kısım dinamik oldu

parser = StrOutputParser()

chain = prompt_template | model | parser
#prompt_template al--> MODELE ver Modeli-->parser a ver

#chain i invoke ederek hepsini gör

if __name__ == "__main__":
    print(chain.invoke({"language": "italian", "text": "hi, what's up?"}))