import re
import csv
from textblob import TextBlob
import collections
import matplotlib.pyplot as plt
from natsort import natsorted

day_dictionary = {} #day message number
hour_dictionary = {} #hour message number
day_sentiment = {} #overall day sentimnet
hour_sentiment = {} #overall hour sentiment
day_side_sentiment = {} #positive negative day
hour_side_sentiment = {} #positive negative hour

def clean_msg(msg):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])| (\w +:\ / \ / \S +)", " ", msg).split())

with open('GoodDoctorWeek1_clean.csv', encoding = "UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0
    for row in csv_reader:
        if line_count==0:
            line_count = line_count+1
        else:
            txt = row[0]
            sentiment = TextBlob(clean_msg(txt)).polarity
            if str.isnumeric(row[6]):
                if row[6] not in day_dictionary:
                    day_dictionary[row[6]] = 1
                else:
                    day_dictionary[row[6]] = day_dictionary[row[6]] + 1
                if row[6] not in day_sentiment:
                    day_sentiment[row[6]] = sentiment
                else:
                    day_sentiment[row[6]] = day_sentiment[row[6]] + sentiment
                if row[6] not in day_side_sentiment:
                    if sentiment > 0:
                        day_side_sentiment[row[6]] = [1, 0]
                    elif sentiment < 0:
                        day_side_sentiment[row[6]] = [0, 1]
                    else:
                        continue
                else:
                    if sentiment > 0:
                        day_side_sentiment[row[6]][0] = day_side_sentiment[row[6]][0] + 1
                    elif sentiment < 0:
                        day_side_sentiment[row[6]][1] = day_side_sentiment[row[6]][1] + 1
                    else:
                        continue
            if str.isnumeric(row[7]):
                if row[7] not in hour_dictionary:
                    hour_dictionary[row[7]] = 1
                else:
                    hour_dictionary[row[7]] = hour_dictionary[row[7]] + 1
                if row[7] not in hour_sentiment:
                    hour_sentiment[row[7]] = sentiment
                else:
                    hour_sentiment[row[7]] = hour_sentiment[row[7]] + sentiment
                if row[7] not in hour_side_sentiment:
                    if sentiment > 0:
                        hour_side_sentiment[row[7]] = [1, 0]
                    elif sentiment < 0:
                        hour_side_sentiment[row[7]] = [0, 1]
                    else:
                        continue
                else:
                    if sentiment > 0:
                        hour_side_sentiment[row[7]][0] = hour_side_sentiment[row[7]][0] + 1
                    elif sentiment < 0:
                        hour_side_sentiment[row[7]][1] = hour_side_sentiment[row[7]][1] + 1
                    else:
                        continue
            line_count = line_count+1

    hour_dictionary = dict(collections.OrderedDict(natsorted(hour_dictionary.items())))
    hour_sentiment = dict(collections.OrderedDict(natsorted(hour_sentiment.items())))
    hour_side_sentiment = dict(collections.OrderedDict(natsorted(hour_side_sentiment.items())))

    dayList = list(day_dictionary.keys())
    hourList = list(hour_dictionary.keys())
    for i in dayList:
        day_sentiment[i]=day_sentiment.get(i)/day_dictionary.get(i)
    for i in hourList:
        hour_sentiment[i]=hour_sentiment.get(i)/hour_dictionary.get(i)

    print("Message Per Day", day_dictionary)
    print("Meesage Per Hour", hour_dictionary)
    print("Sentiment Per Day", day_sentiment)
    print("Sentiment Per Hour", hour_sentiment)
    print("Compare Sentiment Per Day", day_side_sentiment)
    print("Compare Sentiment Per Hour", hour_side_sentiment)

    plt.bar(list(day_dictionary.keys()), day_dictionary.values(), align= 'center')
    plt.xlabel('Day')
    plt.ylabel('Number of Message')
    plt.title("Message Per Day")
    plt.ylim(0,20000)
    plt.show()

    plt.bar(list(hour_dictionary.keys()), hour_dictionary.values(), align='center')
    plt.xlabel('Hour')
    plt.ylabel('Number of Message')
    plt.title("Message Per Hour")
    plt.ylim(0, 10000)
    plt.show()

    plt.bar(list(day_sentiment.keys()), day_sentiment.values(), align='center')
    plt.xlabel('Day')
    plt.ylabel('Average Sentiment')
    plt.title("Sentimnet Per Day")
    plt.ylim(-1, 1)
    plt.show()

    plt.bar(list(hour_sentiment.keys()), hour_sentiment.values(), align='center')
    plt.xlabel('Hour')
    plt.ylabel('Average Sentimnet')
    plt.title("Sentiment Per Hour")
    plt.ylim(-1,1)
    plt.show()

    sentiment_list = list(day_side_sentiment.values())
    positive = []
    negative = []

    for w in sentiment_list:
        positive.append(w[0])
        negative.append(w[1])

    plt.bar(list(day_side_sentiment.keys()), positive, align='center')
    plt.bar(list(day_side_sentiment.keys()), negative, align='center', color = 'r')
    plt.xlabel('Day')
    plt.ylabel('Sentiment Positive vs Negative')
    plt.title("Count of Sentimnet")
    plt.ylim(-1000, 15000)
    plt.show()

    sentiment_list = list(hour_side_sentiment.values())
    positive = []
    negative = []

    for w in sentiment_list:
        positive.append(w[0])
        negative.append(w[1])

    plt.bar(list(hour_side_sentiment.keys()), positive, align='center')
    plt.bar(list(hour_side_sentiment.keys()), negative, align='center', color='r')
    plt.xlabel('Hour')
    plt.ylabel('Sentiment Positive vs Negative')
    plt.title("Count of Sentimnet")
    plt.ylim(-100, 5000)
    plt.show()
