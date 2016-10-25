import argparse
import collections
import re

def load_data(filepath):
    with open(filepath, 'r') as text_file:
        data = text_file.read()
    return data

def get_words_from_text(text):
    return re.findall(r'\w+', text.lower())

def get_most_frequent_words(text):
    words = get_words_from_text(text)
    number_of_words = 10
    return collections.Counter(words).most_common(number_of_words)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", help="Адрес текстового файла.", type=str)
    args = parser.parse_args()
    filepath = args.filepath
    
    try:
        data = load_data(filepath)
    except Exception:
        print("Некорректные входные данные!")
    else:
        most_frequent_words = get_most_frequent_words(data)
        print("Десять наиболее часто используемых в данном " + \
            "тексте слов в порядке убывания:\n", most_frequent_words)

if __name__ == '__main__':
    main()
