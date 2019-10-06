import csv
import matplotlib.pyplot as plt

final_dicitionary = {}
final_dicitionary['positive'] = 0
final_dicitionary['neutral'] = 0
final_dicitionary['negative'] = 0

with open('nltk_output.txt', encoding="UTF-8") as my_file:
    csv_reader = csv.reader(my_file, delimiter='\t')

    for row in csv_reader:
        txt = row[0]
        sentiment = float(row[1])
        if sentiment == 0:
            final_dicitionary['neutral'] += 1
        elif sentiment < 0:
            final_dicitionary['negative'] +=1
        else:
            final_dicitionary['positive'] +=1

    print("# of tweets labeled as positive: " + str(final_dicitionary['positive']))
    print("# of tweets labeled as neutral: " + str(final_dicitionary['neutral']))
    print("# of tweets labeled as negative: " + str(final_dicitionary['negative']))

temp = list(final_dicitionary.values())
for i in range(len(temp)):
    temp[i] = temp[i]-10
    print(temp)

plt.title('Tweet Sentiment')
plt.bar(final_dicitionary.keys(), final_dicitionary.values(), alpha=0.5)
plt.bar(final_dicitionary.keys(), temp, alpha = 0.5, color = 'g')
plt.ylabel('Number of sentimnet')
plt.xlabel('Sentimnet')
plt.show()