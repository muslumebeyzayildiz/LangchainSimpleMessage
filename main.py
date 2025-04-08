from dotenv import load_dotenv, dotenv_values

load_dotenv()#bu fonk otomatik .env i arayacak

print(dotenv_values(".env").get("OPENAI_API_KEY"))#bunu çok kullanmayacağız
if __name__ == '__main__':
    print('PyCharm')

