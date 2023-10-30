# takes a string and replaces some words with other words

def replace_word():
    
    str = "hello everyone, this is a test string. hi hi hi hihi"
    word_to_replace = input("Enter the word you want to replace: ")
    replacement_word = input("Enter the word replacement: ")
    print(str.replace(word_to_replace, replacement_word))
    
replace_word()