import requests
from bs4 import BeautifulSoup

def print_to_text(base_url):

    r = requests.get(base_url)
    soup = BeautifulSoup(r.text)

    for story_heading in soup.find_all(class_="story-heading"):
        if story_heading.a:
            print(story_heading.a.text.replace("\n", " ").strip())
        else:
            print(story_heading.contents[0].strip())


base_url = "http://www.nytimes.com"
print_to_text(base_url)
