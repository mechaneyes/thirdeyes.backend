import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain import PromptTemplate

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY, model_name="gpt-4-0125-preview", temperature=0
)

context = ""


# ————————————————————————————————————o identify_artists —>
#
def identify_artists(query):

    template = """
    context: Below is a prompt identified by three less than signs (<<<) and 
    three greater than signs (>>>).
    
    Take that provided prompt and determine if there is a music artist name in it.
    They can be a musician, band, producer, dj, etc.

    If there is a music artist name in the prompt, return the name or names of the 
    artists in JSON format. The key should be "artist" and the value should be the 
    name of the artist.

    query: <<<{query}>>>
    answer: """

    prompt = PromptTemplate(
        input_variables=["query"], template=template
    )
    llmchain = LLMChain(llm=llm, prompt=prompt)
    output = llmchain.run({"query": query})

    print(
        "\n\n # ————————————————————————————————————o identify_artists —> \n"
    )
    # print(context[0].metadata)
    # print(type(context[0].metadata))
    print(output)

    # the returned output is in some strange data format.
    # so this is us processing it
    context_list = [doc.metadata for doc in context[:5]]

    return [output, context_list]
