import os
import json

def load_tagalog_terms():
    """Loads the Tagalog terms from the JSON file."""
    json_file_path = os.path.join(os.path.dirname(__file__), 'tagalog_terms.json')
    
    # Open and load the JSON file
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        tagalog_terms = json.load(json_file)

    # Flatten the JSON categories into a single list of words
    all_terms = []
    for category, terms in tagalog_terms.items():
        all_terms.extend(terms)

    return all_terms

def check_file_for_tagalog_terms(file_path):
    """Check if the file contains any Tagalog terms."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File {file_path} not found.")

    # Load the file content
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().lower()

    # Load the Tagalog terms from the JSON file
    tagalog_words = load_tagalog_terms()

    # Check if any Tagalog word is in the content
    return any(word in content for word in tagalog_words)

def check_string_for_tagalog_terms(input_string):
    """Check if the input string contains any Tagalog terms."""
    content = input_string.lower()

    # Load the Tagalog terms from the JSON file
    tagalog_words = load_tagalog_terms()

    # Check if any Tagalog word is in the content
    return any(word in content for word in tagalog_words)
