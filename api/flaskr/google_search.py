import os
from dotenv import load_dotenv
from langchain.tools import Tool
from langchain_community.utilities import GoogleSearchAPIWrapper

load_dotenv()

os.environ["GOOGLE_CSE_ID"] = os.getenv("GOOGLE_CSE_ID")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

from flask import (
    Blueprint
)

bp = Blueprint('google_search', __name__, url_prefix='/google-search')

@bp.route('/search')
def search():
    google_search = GoogleSearchAPIWrapper()

    def top5_results(query):
        return google_search.results(query, 5)


    tool = Tool(
        name="Google Search Snippets",
        description="Search Google for recent results.",
        func=top5_results,
    )

    result = tool.run("What is House music?")

    return result
    return f'Hello, google_search! {result}'