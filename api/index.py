import os
import json
from dotenv import load_dotenv
from flask_cors import CORS
from langchain.tools import Tool
from langchain_community.utilities import GoogleSearchAPIWrapper
from flask import Flask, Blueprint, request, jsonify
from lib.artist_identifier import identify_artists
from lib.spotify_artist_deets_getter import spotify_get_artist_deets

app = Flask(__name__)

# 🚨: Tighten up CORS when running in production
CORS(app, resources={r"/*": {"origins": "*"}})

load_dotenv()

os.environ["GOOGLE_CSE_ID"] = os.getenv("GOOGLE_CSE_ID")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# // ————————————————————————————————————o————————————————————————————————————o google -->
# // ————————————————————————————————————o get google results —>
# 
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

# // ————————————————————————————————————o————————————————————————————————————o identify -->
# // ————————————————————————————————————o identify artists in prompt —>
# 
@app.route("/identify-artists", methods=['GET'])
def identify():
    form_input = request.args.get("form-input", "")
    print(form_input)

    # identified = identify_artists(form_input)

    try:
        response = identify_artists(form_input)
        
        print(response)
        
        if isinstance(response, dict):
            data = response
        else:
            data = json.loads(response)
    except json.JSONDecodeError:
        raise ValueError("The response is not in valid JSON format.")

    print('datadata:', data.artists)
    return jsonify(data)
    
# // ————————————————————————————————————o————————————————————————————————————o spotify -->
# // ————————————————————————————————————o get spotify deets —>
# 
@app.route("/spotify-deets", methods=['GET'])
def spotify():
    form_input = request.args.get("form-input", "")
    print(form_input)

    # identified = identify_artists(form_input)

    try:
        response = identify_artists(form_input)
        
        print(response)
        
        if isinstance(response, dict):
            data = response
        else:
            data = json.loads(response)
    except json.JSONDecodeError:
        raise ValueError("The response is not in valid JSON format.")

    
    print('datadata:', data['artists'])

    artists_string = ', '.join(data['artists'])
    # print('artists_string:', artists_string)

    # spotify_get_artist_deets(data.artists[0])
    artist_deets = spotify_get_artist_deets(artists_string)
    print('artist_deets:', artist_deets)

    return artist_deets

    return jsonify(data)
