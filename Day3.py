import csv
import time

import matplotlib.pyplot as plt
import operator
from collections import OrderedDict
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Abdullah_Alfarrarjeh_app")

#location = geolocator.geocode("마포구 임정로 47", addressdetails = True)

#print(location.address)
#print((location.latitude, location.longitude))

#print(location.raw)

#location = geolocator.reverse("37.5447267, 126.9579425", addressdetails = True)
#print(location.address)

#print(location.raw)
#print(location.raw['address']['city'])

def do_reverse_geocode(address):
    try:
        return geolocator.reverse(address)
    except GeocoderTimedOut:
        return do_reverse_geocode()

count = 0

f_input = open("tweet_input.csv", encoding="UTF-8")
final_dictionary = {}

lines = [x.strip() for x in f_input.readlines()]
for line in lines:
    count+=1

    if count==1:
        continue

    lineTokens = line.split(',')
    latitude = lineTokens[3]
    longitude = lineTokens[4]

    location = do_reverse_geocode(latitude+","+longitude)

    county = location.raw['address']['county']
    print(latitude + "\t" + longitude + "\t" + county)

    if county not in final_dictionary:
        final_dictionary[county] = 1
    else:
        final_dictionary[county] = final_dictionary[county] + 1

    time.sleep(0.300)

sorted_d = sorted(final_dictionary.items(), key=operator.itemgetter(1), reverse = True)
print(sorted_d)

f_input.close()

with open("GeoRegionCount.csv", mode = 'w', newline = '', encoding = 'UTF-8') as my_file:
    my_writer = csv.writer(my_file, delimiter = ',')

    my_writer.writerow(['GeoRegion', 'Count'])

    for key in sorted_d:
        current_RegionName = str(key[0])
        current_Count = int(key[1])

        my_writer.writerow([current_RegionName, current_Count])

plt.figure(figsize=(25,3))
plt.title('Spatial Distribution of Tweets')
plt.xlabel('Counties')
plt.ylabel('# of Tweets per county')
plt.bar(final_dictionary.keys(), final_dictionary.values(), width = 0.3, color = 'g')

plt.show()