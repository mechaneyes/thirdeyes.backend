import spacy
from spacy.matcher import PhraseMatcher
from data.artists_list import artists

nlp = spacy.load("en_core_web_sm")
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")  # Use 'LOWER' to match tokens in lowercase

# Filter out names with non-ASCII characters
artists_ascii = [name for name in artists if name.isascii()]

patterns = [nlp.make_doc(name) for name in artists_ascii]

# Add patterns to the matcher
matcher.add("MUSIC_ARTIST", patterns)

def match_artists(text):
    # Create a `Doc` object
    doc = nlp(text)

    # Call the matcher on the doc
    matches = matcher(doc)

    # Iterate over the matches and return them
    matched_artists = [str(doc[start:end]) for match_id, start, end in matches]
    return matched_artists