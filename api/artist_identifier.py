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
    artists in your response in JSON format. The key should be "artist" and the value
    should be the name of the artist in quotes.

    query: <<<{query}>>>
    answer: """

    prompt = PromptTemplate(
        input_variables=["query"], template=template
    )
    llmchain = LLMChain(llm=llm, prompt=prompt)
    raw_output = llmchain.invoke({"query": query})

    # Extract and parse the JSON from the response
    try:
        # Extract the 'text' field from the raw_output
        json_string = raw_output["text"]

        # Parse the JSON string into a dictionary
        result = json.loads(json_string)

        if 'artist' in result:
            print("\n\n # ————————————————————————————————————o identify_artists —> \n")
            print(result)
            return result
        else:
            raise ValueError("Artist key not found in the response JSON.")
    except json.JSONDecodeError:
        raise ValueError("The response is not in valid JSON format.")

# Example usage:
# identify_artists("The query for the AI would be mentioning Bonobo in some context.")