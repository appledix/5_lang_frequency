import sys

def read_console_args():
    return sys.argv[1:]

def load_data(filepath):
    data = ""
    text_file = open(filepath, "r")
    data = text_file.read()
    text_file.close()
    return data

def text_to_words_array(text):
    text = text.lower().replace("\n", " ").replace("\t", " ").split(" ")
    words_array = []
    current_word = ""
    for word in text:
        current_word = ""
        for char in word:
            if char.isalpha() or char == "-":
                current_word += char
            else:
                continue
        if current_word != "":
            words_array.append(current_word)
    return words_array

def get_unique_words(words_array):
    words_dict = {}
    for word in words_array:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    return words_dict


def get_most_frequent_words(text):
    words_array = text_to_words_array(text)
    unique_words = get_unique_words(words_array)
    most_frequent_words = []
    for i in range(10):
        most_frequent_word = {"name":None, "frequency":0}   
        for word in unique_words:
            current_frequency = unique_words[word]
            if current_frequency > most_frequent_word["frequency"]:
                most_frequent_word["name"] = word
                most_frequent_word["frequency"] = current_frequency
            else:
                continue
        del unique_words[most_frequent_word["name"]]
        most_frequent_words.append(most_frequent_word["name"])
    return most_frequent_words


if __name__ == '__main__':
    parameters = read_console_args()
    try:
        if len(parameters) != 1:
            raise Exception
        filepath = parameters[0]
        data = load_data(filepath)
    except Exception:
        print\
        ("Для работы скрипта необходимо передать ему валидный адрес текстового файла.")
    else:
        most_frequent_words = get_most_frequent_words(data)
        print\
        ("Десять наиболее часто используемых в данном тексте слов в порядке убывания:\n",\
            most_frequent_words)