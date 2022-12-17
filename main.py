
import csv
from itertools import zip_longest

import requests
from bs4 import  BeautifulSoup

car_name = []
division = []
price = []
result = requests.get("https://eg.hatla2ee.com/ar/new-car/bmw/218-i-shape-new-generation")

src = result.content

soup = BeautifulSoup(src, "lxml")

# car name     #division      #price
car_names = soup.find_all("a", attrs={"class": "nCarListData_title"})

divisions = soup.find_all("span", attrs={"class": "classes_label"})

prices = soup.find_all("div", attrs={"class": "nCarListData_prices_elem"})
for i in range(0, len(divisions), 1):
    car_name.append(car_names[i].text.strip())
    division.append(divisions[i].text.strip())

x = 'السعر'
y = 'من'

for i in range(0, len(prices), 1):
    if x in prices[i].text.strip():
        price.append(prices[i].text.strip())
    if (y in prices[i].text.strip()):
        price.append(prices[i].text.strip())

file_list = [car_name, division, price]
print("All Data Now in CSV File")
exported = zip_longest(*file_list)
with open("CarData.csv", "w", newline='', encoding="utf-8-sig") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["car_name", "division", "price"])
    wr.writerows(exported)

