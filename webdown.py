import json, requests
from bs4 import BeautifulSoup

def hit_it(url):
    """
    Hit the input url. Return requests object is successful. Die, if not.
    """
    try:
        r = requests.get(url)
    except:
        print('Error 2: Could not connect to the given URL')
        initializer()
    return r

def get_a(soup, url):
    """
    Prints href of all <a> links
    """
    a_tags = soup.find_all('a')
    print(len(a_tags), "<a> TAGS")
    for _ in a_tags:
        try:
            if _['href'].startswith('/'):
                # links on the input_url
                print(url+_['href'])
            else:
                # external links
                print(_['href'])
        except:
            print("Error 5: hyperlink not found.")

def get_link(soup):
    """
    Prints href of all <link> tags where rel=stylesheet
    """
    link_tags = soup.find_all('link')
    print(len(link_tags), "<link> TAGS")
    for _ in link_tags:
        try:
            if _['rel'][0] == 'stylesheet':
                print(_['href'])
        except:
            print("Error 4: css file not found.")


def get_script(soup):
    """
    Prints src of all <script> tags
    """
    script_tags = soup.find_all('script')
    print(len(script_tags), "<script> TAGS")
    for _ in script_tags:
        try:
            print(_['src'])
        except:
            print("Error 3: javascript file not found.")

def interface(soup, url):
    """
    User Friendly interface
    """
    wrong_choice_count = 0
    while(True):
        choice = input("""\nPress a number 1-5. Then press Enter:
                        1. Show all hyperlinks on the webpage.
                        2. Show all css files on the webpage.
                        3. Show all javascript files on the webpage.
                        4. Enter a new URL.
                        5. Exit. 
                        """)
        if choice == "1":
            get_a(soup, url)
        elif choice == "2":    
            get_link(soup)
        elif choice == "3":
            get_script(soup)
        elif choice == "4":    
            initializer()
        elif choice == "5":    
            exit()
        else:
            wrong_choice_count += 1
            print("\nWrong choice.")
            if wrong_choice_count > 3:
                exit()

def initializer():
    """
    Prompts user to enter URL and diplays interface.
    """
    entered_url = input('\nEnter website url: ').strip()

    # Add 'http://' if not present
    if not entered_url.startswith('http'):
        input_url = 'https://' + entered_url
    else:
        input_url = entered_url

    print('Connecting to: ' + input_url)

    if input_url.count('.') < 4:
        # At most 3 dots in URL are valid
        r = hit_it(input_url)
        soup = BeautifulSoup(r.text, 'html.parser')
        interface(soup, input_url)
    
    else:
        # More than 3 dots in URL
        print('Error 1: Invalid URL')
        initializer()

if __name__ == '__main__':
    
    print('\n--- Webpage Asset Viewer ---\n')
    initializer()