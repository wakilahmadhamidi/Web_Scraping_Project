import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.worldometers.info/world-population/population-by-country/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# print(soup)

row = soup.find("table", {"id": "example2"}).find("tbody").find_all("tr")

# print(len(row))

countries_list = []

for i in range(len(row)):
    country = row[i].find_all("td")[1].text
    countries_list.append(country)
    Population_2023 = row[i].find_all("td")[2].text
    countries_list.append(Population_2023)
    Yearly_Change = row[i].find_all("td")[3].text
    countries_list.append(Yearly_Change)
    Net_Change = row[i].find_all("td")[4].text
    countries_list.append(Net_Change)
    Land_Area_KM2 = row[i].find_all("td")[6].text
    countries_list.append(Land_Area_KM2)
    Fertility_Rate = row[i].find_all("td")[8].text
    countries_list.append(Fertility_Rate)
    Median_Age = row[i].find_all("td")[9].text
    countries_list.append(Median_Age)

# To print the list of countries list in a table format
countries_list = [countries_list[i:i+7] for i in range(0, len(countries_list), 7)]
df = pd.DataFrame(countries_list, columns=["Country", "Population_2023", "Yearly_Change", "Net_Change", "Land_Area_KM2", "Fertility_Rate", "Median_Age"])
print(df)

# # To Save the data to a CSV file
df.to_csv("Countries.csv", index=False)

# To Save the data to a Excel file
df.to_excel("Countries.xlsx", index=False)

# print(countries_list)