from langchain_openai import ChatOpenAI #OPENAI İLE DİREKT OLARKA İLETİŞİME GEÇECEĞİM
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage #chat promptları 2 türlü alıyor 1-sen bir senior yazılımcısın2-python nedir
from langchain_core.output_parsers import StrOutputParser #LLM geri döndürdüğü çıktıları daha iyi Parse etmek İŞLEMEK için

load_dotenv()
model = ChatOpenAI(model="gpt-4", temperature=0.1)

messages = [
    SystemMessage(content="Translate the following from English into Spanish"),#Yazdığımız bu proptu daha iyi sonuç almak için İNgilizce yazdık
    HumanMessage(content="hi!"),
]

myparser = StrOutputParser()#şeklinde oluşturabiliyorz

result = model.invoke(messages)
print(result.content)

if __name__ == "__main__":
    print(myparser.invoke(result))

    