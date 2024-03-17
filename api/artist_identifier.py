import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts.prompt import PromptTemplate

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY, model_name="gpt-4-0125-preview", temperature=0
)

context = ""


def identify_artists(query):
    template = """
    context: Below is a prompt identified by three less than signs (<<<) and
    three greater than signs (>>>).

    Take that provided prompt and determine if there is a music artist name in it.
    They can be a musician, band, producer, DJ, etc.

    If there is a music artist name in the prompt, return the name or names of the
    artists in your response in JSON format. Give me a dictionary with the key 
    "artists" associated with a list of artist names.
    

    query: <<<{query}>>>
    answer: """

    prompt = PromptTemplate(input_variables=["query"], template=template)
    llmchain = LLMChain(llm=llm, prompt=prompt)
    raw_output = llmchain.invoke({"query": query})

    output = raw_output["text"]
    output = output.strip()  # Remove leading and trailing whitespace
    
    # Remove the Markdown formatting
    if output.startswith("```json"):
        output = output[7:]
    if output.endswith("```"):
        output = output[:-3]

    print(output)

    return output


# Testing usage:
# identify_artists("The query for the AI would be mentioning Brian Eno and david byrne.")
