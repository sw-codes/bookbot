def count_words(string):
    word_count = string.split()
    return len(word_count)

def count_characters(string):
    characters = {}
    for character in string.lower():
        if not character in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    return characters

def sort_dictionary(dictionary):
    character_list = []
    for character in dictionary:
        if character.isalpha():
            character_list.append({"char" : character, "count" : dictionary[character]})
    character_list.sort(reverse=True, key=sort_on)
    return character_list

def sort_on(items):
    return items["count"]