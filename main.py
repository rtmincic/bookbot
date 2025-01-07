def count_words(book_words):
    words = book_words.split()
    word_count = len(words)
    return word_count

def count_characters(book_words):
    lowercase_words = book_words.lower()
    letter_count = {}
    words = lowercase_words.split()
    for word in words:
        letters = list(word)
        for letter in letters:
            if letter.isalpha():
                if letter in letter_count:
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1
    letter_count = dict(sorted(letter_count.items(), key=lambda item: item[1], reverse=True))
    return letter_count

def report(word_count, letter_count):
    print("------ Begin Report of book/frankenstein.txt ------")
    print(f"{word_count} words found in the document.")
    for key in letter_count:
        print(f"The {key} character is found {letter_count[key]} times.")
    print("------ End of Report ------")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    letters_count = count_characters(file_contents)
    report(word_count, letters_count)




main()


    

