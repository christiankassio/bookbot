file_dir = "books/frankenstein.txt"

def word_count(text): #prints count of words in text
        words = text.split() #creates a list where each word in text is a value inside
        words_count = len(words)
        print(f"""

{words_count} words found in the document
""")


def char_count(text): #prints a dict that contains the frequency of each character in text
    characters = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0,}
    lower_text = text.lower() #makes all characters lowercase
    for char in lower_text: #iterates over every character
        if char in characters: #only accounts for letters a-z
            characters[char] += 1 #adds 1 to the total count of the current character being iterated
    
    sorted_characters = sorted(characters.items(), key=lambda item: item[1], reverse=True)

    for char, count in sorted_characters:
        print(f"The '{char}' character was found {count} times")


def main():
    with open(file_dir) as f: #brings .txt file into python file
        file_contents = f.read() #converts .txt file to string

    print(f"--- Begin report of {file_dir} ---")


    word_count(file_contents)
    char_count(file_contents)
    print("""
          
--- End report ---""")
main()