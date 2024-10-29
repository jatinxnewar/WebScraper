import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://en.wikipedia.org/wiki/Delhi"
response = requests.get(url)

if response.status_code == 200:
    print("Request successful")

    soup = BeautifulSoup(response.content, 'html.parser')
    

    links = soup.find_all('a')

    places = soup.find_all('span', {'class': 'place'})
    
    data = []
    
    for place, link in zip(places, links):
        
        place_text = place.text
        link_text = link.text

        temp_dict = {
            'Place': place_text,
            'Link': link_text
            }
        
        data.append(temp_dict)

    

    #Creating a list to store the scraped data
    scraped_data = []
    
    for link in links:
        href = link.get('href')
        scraped_data.append(href)
        df = pd.DataFrame(scraped_data, columns=['Links'])
        df.to_csv('scraped_data.csv', index=False)
else:
    print("Request failed")


