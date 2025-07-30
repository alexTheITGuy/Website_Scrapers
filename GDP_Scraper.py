from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

#Find all the rows in the table body
rows = soup.find_all('tr')

#List to store each row's data
gdp_data = []

#Loop through data and add needed information to gdp_data
for row in rows:
    cells = row.find_all('td')
    if len(cells) >= 7:
        country = cells[0].get_text(strip=True)
        IMF = cells[1].get_text(strip=True)
        year = cells[2].get_text(strip=True)

        gdp_data.append((country, IMF, year))

#To test if all data is printed properly
#print(gdp_data) 

#Define a .csv file name
csv_file = 'gdp_by_country.csv'

#Write to the .csv file
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    #Write headers
    writer.writerow(["Country", "IMF_in_USD", "Year"])

    #Write the country data
    writer.writerows(gdp_data)

print(f"Data has been written to {csv_file}")
