# Imports:
import json
import requests
import re
from bs4 import BeautifulSoup
import time

# this is out target: we want it full of leaders, with the first paragraph of their bios
leaders_by_country = {} 


def clean_paragraph_text(text):
    without_references = re.sub(r"\[[^\]]+\]", "", text)
    return re.sub(r"\s+", " ", without_references).strip()


## This function retrieves the first paragraph of a url, cleans it and add it to the bio
def get_first_paragraph(wikipedia_url, session=None):
    
    # 1/ Get a wikipedia page 
    # 2/ Get the paragraphs > put them in a list
    # 3/ Get the first bold Paragraph > print it 
    to_return = ""
    
    # 1/ Making a request, checking it all works:
    ## we print the url we'll use:
    print(wikipedia_url) # keep this for the rest of the notebook

    if session is None:
        session = requests.Session()
    
    ## Setting headers, making the request, printing status code:  
    headers = {"User-Agent": "Python exercise, I'll behave!"}
    try:
        r = session.get(wikipedia_url, headers=headers, timeout=10)
    except requests.RequestException as error:
        print(f"Request failed for {wikipedia_url}: {error}")
        return ""
    # print(r.status_code) : checks for status, reactivate to debug
    
    # 2/ Retrieving the text from the request:
    ## Create a Beautifulsoup object, a empty paragraphs list.
    soup = BeautifulSoup(r.text, "html.parser")
    paragraphs = []
    first_non_empty_paragraph = ""
    
    ## Fills up the paragrapgh list with all the paragraphs
    for par in soup.find_all("p"):        
        paragraphs.append(par)  
    
    
    # Filtering for the first paragraph that start with bold:
    ## Looping though our paragraphs:
    for par in paragraphs:
        paragraph_text = par.get_text(" ", strip=True)
        if not paragraph_text:   # if the paragraph is empty, skip it
            continue

        cleaned_text = clean_paragraph_text(paragraph_text)
        if not first_non_empty_paragraph:
            first_non_empty_paragraph = cleaned_text

        first_bold = par.find("b")
        

    ### find a paragraph that begins with some bold      
        if first_bold is None:
            continue
    #print(first_bold)
    
        
        ### If the paragraph is not empty, clean it up, print its text and break.
        if first_bold:
            print(cleaned_text)
            to_return = cleaned_text
            break

    if not to_return and first_non_empty_paragraph:
        print(first_non_empty_paragraph)
        to_return = first_non_empty_paragraph
    
    return to_return  



def get_leaders():
    root_url = "https://country-leaders.onrender.com"
    status_url = "https://country-leaders.onrender.com/status"
    countries_url = "https://country-leaders.onrender.com/countries"
    cookies_url = "https://country-leaders.onrender.com/cookie"
    check_url = "https://country-leaders.onrender.com/check"
    leaders_url =  "https://country-leaders.onrender.com/leaders"
    #leaders_by_country = {}
    countries = []
    leaders = []
    
    # Working in a session, for speed.
    with requests.Session() as s:
        # getting a ccokie and checking it.    
        s1 = s.get(cookies_url)
        print(s.get(check_url).text)
        
        # Getting the countries
        s2 = s.get(countries_url)
        countries = s2.json()

        ## Getting the leaders of coutries
        for country in countries:
            s.get(cookies_url) # getting a fresh cookie before leaders request
            params = {"country": country}
            s3 = s.get(leaders_url, params=params)
            leaders = s3.json()

            if not isinstance(leaders, list):
                print(f"Skipping {country}: unexpected response: {leaders}")
                leaders_by_country[country] = []
                continue

            # putting the leaders in the leaders by country dict.
            leaders_by_country[f"{country}"] = leaders

            # get the leader's first paragraph, adding it to its dict.
            for leader in leaders:
                wikipedia_url = leader.get("wikipedia_url")
                if not wikipedia_url:
                    leader["Bio"] = ""
                    continue
                time.sleep(0.1) # Pause before next request
                leader["Bio"] = get_first_paragraph(wikipedia_url, s)
                 
        return leaders_by_country
   
    

# A function that takes the leaders by country variable
    # dumps it in the leaders.json file
    # opens and prints it. 
def save_leaders_by_country():
    with open("leaders.json", "w") as leaders_json:
        json.dump(leaders_by_country, leaders_json, indent=2)
    with open("leaders.json", "r") as file:
        print(json.load(file))

        
##        
## Calling the functions:
##
if __name__ == "__main__":
    get_leaders()
    print(leaders_by_country)
