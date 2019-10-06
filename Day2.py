import csv
import nltk
#nltk.download()
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from collections import OrderedDict
import operator

example_sentence = "This is a sample sentence."
word_tokens = word_tokenize(example_sentence)

for w in word_tokens:
    print(w)

example_sentence = "It's a Sample SentEnce."
final_sentence = example_sentence.lower()
print(final_sentence)

example_sentence = "It's a sample sentence"
tokenizer = RegexpTokenizer(r'\w+')
word_tokens = tokenizer.tokenize(example_sentence)

for w in word_tokens:
    print(w)

stop_words = set(stopwords.words('english'))
tokenizer = RegexpTokenizer(r'\w+')
word_tokens = tokenizer.tokenize(example_sentence)
filtered_sentence = [w for w in word_tokens if not w in stop_words]

for w in filtered_sentence:
    print(w)

final_dictionary = {}

with open('Data.csv', encoding = "UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            line_count = line_count + 1
        else:
            txt = row[1]
            final_txt = txt.lower()
            stop_words = set(stopwords.words('english'))
            tokenizer = RegexpTokenizer(r'\w+')
            word_tokens = tokenizer.tokenize(final_txt)
            filtered_sentence = [w for w in word_tokens if not w in stop_words]
            for w in filtered_sentence:
                if w not in final_dictionary:
                    final_dictionary[w] = 1
                else:
                    final_dictionary[w] = final_dictionary[w] + 1

            line_count = line_count + 1
sorted_d = sorted(final_dictionary.items(), key = operator.itemgetter(1), reverse=True)

print(sorted_d)

with open('wordCount.csv', mode = 'w', newline = '', encoding='UTF-8') as my_file:
    my_writer = csv.writer(my_file, delimiter=',')

    my_writer.writerow(['Word', 'Count'])

    for key in sorted_d:
        current_Word = str(key[0])
        current_Count = int(key[1])
        my_writer.writerow([current_Word, current_Count])