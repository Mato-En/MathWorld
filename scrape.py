import requests
from bs4 import BeautifulSoup
import re
forums ={"mathoverflow": "https://mathoverflow.net", "stackexchange" : "https://math.stackexchange.com"}
questions = dict()
def initiate_scrape(search_query):
    session=requests.Session()
    headers = {"User-Agent": "Mozilla/5.0 (X11, Linux x86_64)" "AppleWebkit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.28 Safari/537.36", "Accept": "text/html, application/xhtml+xml,application/xml;" "q=0.9,image/webp,*/*;q=0.8"} #imitate browser
    for forum_name, url_stem in forums.items(): #iterate through forums to get their name and url
        req = session.get(url_stem+"/search?q="+search_query, headers=headers)
        bs = BeautifulSoup(req.text, "html.parser")
        results = bs.find_all("div", class_="s-post-summary--content")
        for index, result in enumerate(results): #iterates through list of matched objects
            content = result.contents #returns list of PageElements, 2nd and 3rd element are question, excerpt respectively
            title = content[1].get_text().strip()
            excerpt = content[3].get_text().strip()
            tag = result.find("a", class_="s-link") #tag that contains link to actual question
            link = tag["href"]
            questions[index]= {"title": title, "excerpt": excerpt, "link": url_stem+link, "forum": forum_name}



initiate_scrape("conjugate")
print(questions)