from langchain_openai import ChatOpenAI #OPENAI İLE DİREKT OLARKA İLETİŞİME GEÇECEĞİM
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage #chat promptları 2 türlü alıyor 1-sen bir senior yazılımcısın2-python nedir

load_dotenv()
#from langchain_openai import ChatOpenAI----->sayesinde
model = ChatOpenAI(model="gpt-4", temperature=0.1) # 0 oldukça LLM daha gerçekçi cevaplar verecek.
# diyerek direkt olarak chatgpt ile iletişeme geçebiliyorum

#temperature=0.1
# 1 e yaklaştıkça uydurmaya başlıyo yani
# DAHA YARATICI CEVAPLAR VERMEYE BAŞLIYOR


messages = [
    SystemMessage(content="Translate the following from English into Turkish"),#Yazdığımız bu proptu daha iyi sonuç almak için İNgilizce yazdık
    HumanMessage(content="hi!"),
    #humanmessaje KULLANICI NE SORUYORSA O
]

response = model.invoke(messages)


if __name__ == "__main__":
    print(response.content)