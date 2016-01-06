import json, requests
from bs4 import BeautifulSoup

# 'http://maps.googleapis.com/maps/api/geocode/xml?sensor=false&address=chirag'

if __name__ == '__main__':
    
    print('\n--- Static Website Downloader ---\n')

    input_url = input('Enter website url: ').strip()

    # Add 'http://' if not present
    if not input_url.startswith('http'):
        input_url = 'http://' + input_url
    print('Connecting to: ' + input_url)

    if input_url.count('.') < 4:
        # At most 3 dots in URL are valid
        # MAIN LOGIC
        try:
            r = requests.get(input_url)
        except:
            exit('Error 2: Could not connect to the given URL')

        soup = BeautifulSoup(r.text, 'html.parser')
        print(soup.get_text())


    else:
        # More than 3 dots in URL
        exit('Error 1: Invalid URL')