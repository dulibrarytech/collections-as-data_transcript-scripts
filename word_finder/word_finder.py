import argparse
import re


def load_dictionary(file_name):
    with open(file_name) as file:
        loaded_txt = file.read().strip().split('\n')
        loaded_txt = [s.lower() for s in loaded_txt]
        return loaded_txt


def word_to_pattern(word):
    new_word = word
    new_word = re.sub(r'\.', r'\\w', new_word)
    new_word = re.sub(r'_', r'\\w{1,2}', new_word)
    new_word = re.sub(r'\?', r'\\w?', new_word)
    new_word = re.sub(r"\$c", r"[^aeiou]", new_word)
    new_word = re.sub(r"\$v", r"[aeiou]", new_word)
    new_word = re.sub(r"\+", r'\\w+', new_word)
    pattern = re.compile(new_word)
    return pattern


def find_matching_words(pattern, word_list):
    matched_words_list = list()
    for word in word_list:
        if pattern.fullmatch(word):
            matched_words_list.append(word)
    return matched_words_list


def print_list(matched_words_list, sentence):
    last_letter = ""
    for w in matched_words_list:
        if w[0] != last_letter:
            print("\n-" + w[0].upper() + "-\n")
            last_letter = w[0]
        if sentence is None:
            print(w)
        else:
            print(sentence.replace('?', w))


def main():
    parser = argparse.ArgumentParser(prog='Word Finder',
                                     description="Tool for helping transcribe hard to read words.")
    parser.add_argument('word',
                        help="""Word to be searched.
                        Special Characters:
                        '.' = 1 unknown character;
                        '_' = 1-2 unknown characters;
                        '?' = 0-1 unknown characters;
                        '+' = 1 or more unknown characters;
                        '[<any group of letters>]' = single unknown character that is one of the letters in the group
                        (ex. [adf] is an unknown character that is 'a', 'd', or 'f');
                        '$c' = any consonant;
                        '$v' = any vowel;""")
    parser.add_argument('-s', '--sentence',
                        help="Will display word list as part of sentence.  "
                             "Use ? to denote where the word should be inserted.")

    args = parser.parse_args()
    word = args.word
    sentence = args.sentence

    word_list = load_dictionary(r'R:\Digital Production Services\Scripts\12dicts\American\2of12inf.txt')
    pattern = word_to_pattern(word)
    matched_words_list = find_matching_words(pattern, word_list)
    if len(matched_words_list) > 0:
        print_list(matched_words_list, sentence)
    else:
        print("No matching words found.")


if __name__ == '__main__':
    main()