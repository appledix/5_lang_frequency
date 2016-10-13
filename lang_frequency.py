import argparse
import collections
import re
import os


def load_data(filepath):
    with open(filepath, 'r') as text_file:
        data = text_file.read()
    return data

def get_words_from_text(text):
    words = re.findall(r'\w+', text)
    return [word.lower() for word in words]

def get_most_frequent_words(text):
    words = get_words_from_text(text)
    number_of_words = 10
    return collections.Counter(words).most_common(number_of_words)

def filepath_is_valid(filepath):
    if os.path.isfile(filepath) and filepath.endswith(".txt"):
        return True
    else:
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", help="Адрес текстового файла.", type=str)
    args = parser.parse_args()
    filepath = args.filepath
    
    if filepath_is_valid(filepath):
        data = load_data(filepath)
        most_frequent_words = get_most_frequent_words(data)
        print("Десять наиболее часто используемых в данном " + \
            "тексте слов в порядке убывания:\n", most_frequent_words)
    else:
        print("Некорректные входные данные!")
