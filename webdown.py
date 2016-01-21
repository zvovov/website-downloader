import json, requests
from bs4 import BeautifulSoup

def hit_it(url):
    """
    Hit the input url. Return requests object is successful. Die, if not.
    """
    try:
        r = requests.get(url)
    except:
        exit('Error 2: Could not connect to the given URL')
    return r

def get_link(soup):
    """
    Prints href of all <link> tags where rel=stylesheet
    """
    link_tags = soup.find_all('link')
    print("<link> TAGS")
    for _ in link_tags:
        if _['rel'][0] == 'stylesheet':
            print(_['href'])

def get_a(soup):
    """
    Prints href of all <a> links
    """
    a_tags = soup.find_all('a')
    print("<a> TAGS")
    for _ in a_tags:
        # print(_['href'])
        if _['href'].startswith('/'):
            # links on the input_url
            print(input_url+_['href'])
        else:
            # external links
            print(_['href'])

def get_script(soup):
    """
    Prints src of all <script> tags
    """
    script_tags = soup.find_all('script')
    print("<script> TAGS")
    for _ in script_tags:
        print(type(_))
        # print(_.get(['src']))

def interface(soup):
    """
    User Friendly interface
    """
    choice = input("""Press 1, 2, or 3. Then press Enter:
                    1. Show all hyperlinks on the webpage.
                    2. Show all css files on the webpage.
                    3. Show all javascript files on the webpage.
                    4. Enter a new URL.
                    5. Exit. 
                    """)
    print(choice)

def initializer():
    """
    Prompts user to enter URL and diplays interface.
    """
    entered_url = input('Enter website url: ').strip()

    # Add 'http://' if not present
    if not entered_url.startswith('http'):
        input_url = 'http://' + entered_url
    print('Connecting to: ' + input_url)

    if input_url.count('.') < 4:
        # At most 3 dots in URL are valid
        r = hit_it(input_url)

        soup = BeautifulSoup(r.text, 'html.parser')
        #print(soup)
        
        # interface(soup)
        # <link> tags
        # get_link(soup)

        # # <a> tags
        # get_a(soup)

        # <script> tags
        get_script(soup)

    else:
        # More than 3 dots in URL
        exit('Error 1: Invalid URL')

if __name__ == '__main__':
    
    print('\n--- Webpage Asset Viewer ---\n')
    initializer()