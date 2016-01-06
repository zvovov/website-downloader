import json, requests
from bs4 import BeautifulSoup

def hit_it(url):
    '''
    Hit the input url. Return requests object is successful. Die, if not.
    '''
    try:
        r = requests.get(url)
    except:
        exit('Error 2: Could not connect to the given URL')
    return r


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
        r = hit_it(input_url)

        soup = BeautifulSoup(r.text, 'html.parser')
        #print(soup)

        # <a> tags
        a_tags = soup.find_all('a')
        for _ in a_tags:
            if not _['href'].startswith('/'):
                # if link points to an external location (not this site)
                print(_['href'])

        # <link> tags
        link_tags = soup.find_all('link')
        for _ in link_tags:
            try:
                if _['rel'] == "stylesheet":
                    # if css
                    if not _['href'].endswith('.css'):
                        # if css file is hosted elsewhere
                        css_r = hit_it(_['href'])
                        print(css_r.text)
                    else:
                        # if css file is found
                        css_r = hit_it(_['href'])
                        print(css_r.text)
            except:
                print('Sum ting wong in link')

        # <script> tags
        script_tags = soup.find_all('script')
        for _ in script_tags:
            try:
                script_r = hit_it(_['src'])
                print(script_r.text)
            except:
                print('Sum ting wong in script')
            

    else:
        # More than 3 dots in URL
        exit('Error 1: Invalid URL')    