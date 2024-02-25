import os
from dotenv import load_dotenv
from flask_cors import CORS
from langchain.tools import Tool
from langchain_community.utilities import GoogleSearchAPIWrapper
from flask import Flask, Blueprint, request

app = Flask(__name__)

load_dotenv()

os.environ["GOOGLE_CSE_ID"] = os.getenv("GOOGLE_CSE_ID")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


bp = Blueprint("google_search", __name__)
CORS(bp, origins="*")


@bp.route("/google", methods=("GET", "POST"))
def google():
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

    # form_input = request.args.get('form-input', '')
    result = tool.run(request.args.get("form-input", ""))

    # return f'You submitted: {result}'

    # return result
    return tool.run(request.args.get("form-input", ""))
