import json
import difflib

# Load the JSON file into a Python dictionary
def load_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data

# Get the definition of a word
def get_definition(word, data):
    word = word.lower()
    if word in data:
        return data[word]['definition']
    else:
        return None

# Suggest a word if the input is misspelled
def suggest_word(word, data):
    suggestions = difflib.get_close_matches(word, data.keys(), n=1, cutoff=0.8)
    if suggestions:
        return suggestions[0]
    else:
        return None

# Main program that interacts with the user
def main():
    data = load_data()

    # Prompt the user to enter a word
    word = input("Enter a word to look up: ")

    # Get the definition
    definition = get_definition(word, data)

    if definition:
        print(f"Definition of {word}: {definition}")
    else:
        print(f"{word} not found in the dictionary.")
        suggestion = suggest_word(word, data)
        if suggestion:
            print(f"Did you mean {suggestion}?")
        else:
            print("No suggestions available.")

# Run the program
if __name__ == "__main__":
    main()
