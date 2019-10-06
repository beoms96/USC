import csv
from textblob import TextBlob

total_sentiment = 0

with open('Data.csv', encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count=0
    for row in csv_reader:
        '''print(row[0])
        print(row[1])'''
        if line_count == 0:
            line_count = line_count+1

        else:
            txt = row[1]
            sentiment = TextBlob(txt).polarity
            total_sentiment = total_sentiment + sentiment
            line_count = line_count + 1

    print("FINAL!")
    print(total_sentiment / (line_count - 1))