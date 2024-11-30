import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

#call and set the environment variables

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "True"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant, please respond to the user request only based on the given context"),
        ("user","Question : {question}\nContext:{context}")
    ]
)

questions = "Can you summarize the speech?"
context="""
            I have three visions for India. In 3000 years of our history, people from all over the world have come and invaded us, captured our lands, conquered our minds. From Alexander onwards, The Greeks, the Turks, the Moguls, the Portuguese, the British, the French, the Dutch, all of them came and looted us, took over what was ours. Yet we have not done this to any other nation. We have not conquered anyone. We have not grabbed their land, their culture, their history and Tried to enforce our way of life on them. Why? Because we respect the freedom of others.

            That is why my first vision is that of FREEDOM. I believe that India got its first vision of this in 1857, when we started the war of Independence. It is this freedom that we must protect and nurture and build on. If we are not free, no one will respect us.

            My second vision for India's DEVELOPMENT, For fifty years we have been A developing nation. It is time we see ourselves as a developed nation. We are among top 5 nations of the world in terms of GDP. We have 10 percent growth rate in most areas. Our poverty levels are falling. Our achievements are being globally recognized today. Yet we lack the self-confidence to see ourselves as a developed nation, self-reliant and self-assured. Isn't this incorrect?
        """
        
model=ChatOpenAI(model="gpt-3.5-turbo")
outputParser=StrOutputParser()
chain = prompt|model|outputParser
print(chain.invoke({"question":questions,"context":context}))

