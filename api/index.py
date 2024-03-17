import os
from dotenv import load_dotenv
from flask_cors import CORS
from langchain.tools import Tool
from langchain_community.utilities import GoogleSearchAPIWrapper
from flask import Flask, Blueprint, request, jsonify
from api.artist_matcher import match_artists
from api.artist_identifier import identify_artists

app = Flask(__name__)

# 🚨: Tighten up CORS when running in production
CORS(app, resources={r"/*": {"origins": "*"}})

load_dotenv()

os.environ["GOOGLE_CSE_ID"] = os.getenv("GOOGLE_CSE_ID")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

@app.route("/google")
def hello_google():
    # return "<p>You've reached the /google route!</p>"
    google_search = GoogleSearchAPIWrapper()

    def top_results(query):
        return google_search.results(query, 4)
    
    def top5_results(query):
        return google_search.results(query, 5)

    tool = Tool(
        name="Google Search Snippets",
        description="Search Google for recent results.",
        func=top_results,
    )

    result = tool.run("What is House music?")
    # return result

    # form_input = request.args.get('form-input', '')
    # result = tool.run(request.args.get("form-input", ""))

    return tool.run(request.args.get("form-input", ""))

@app.route("/artist-match", methods=['GET'])
def match_artists_route():
    form_input = request.args.get("form-input", "")
    print(form_input)

    matches = match_artists(form_input)
    print(matches)

    return jsonify(matches)
    
@app.route("/identify-artists", methods=['GET'])
def identify_artists():
    form_input = request.args.get("form-input", "")
    print(form_input)

    identified = match_artists(form_input)
    print(identified)

    return jsonify(identified)
