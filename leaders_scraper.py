# Imports:
import json
import requests
import re
from bs4 import BeautifulSoup
import time
import random

# this is out target: we want it full of leaders, with the first paragraph of their bios
leaders_by_country = {} 

## This function retrieves the first paragraph of a url, cleans it and add it to the bio
def get_first_paragraph(wikipedia_url, session=requests.Session()):
    
    # 1/ Get a wikipedia page 
    # 2/ Get the paragraphs > put them in a list
    # 3/ Get the first bold Paragraph > print it 
    biography_paragraph = ""
    
    # 1/ Making a request, checking it all works:
    ## we print the url we'll use:
    print(wikipedia_url) # keep this for the rest of the notebook
    
    if session is None: # in case the session didn't pass through, set one.
        session = requests.Session()
        s_cookie = session.get("https://country-leaders.onrender.com/cookie")
    
    ## Setting headers, making the request, printing status code:  
    #!! implement try except here.
    headers = {"User-Agent": "Python exercise, I'll behave!"}
    r = session.get(wikipedia_url, headers=headers, timeout=10)
    # print(r.status_code) : checks for status, reactivate to debug
    
    # 2/ Retrieving the text from the request:
    ## Create a Beautifulsoup object, a empty paragraphs list.
    soup = BeautifulSoup(r.text, "html.parser")
    paragraphs = []
    first_non_empty_paragraph = ""
    
    
    ## Fills up the paragrapgh list with all the paragraphs
    for par in soup.find_all("p"):        
        paragraphs.append(par)
         
    
    # Getting the first non empty bold paragraph, cleaning it and setting it as the bio
    for par in paragraphs:
        paragraph_text = par.get_text(" ", strip=True) 
        if not paragraph_text:   # if the paragraph is empty, skip it
            continue
        # if the paragraph has text, find the bold
        if paragraph_text:
            first_bold = par.find("b")
            if first_bold is None: 
                continue # skip the empty ones.

            if first_bold: # clean the first bold paragraph and set it as the bio paragraph
                cleanish_text = re.sub(r"(\(.*\[\d]\))", " " ,paragraph_text)
                cleanerish_text = re.sub(r"\[[^\]]+\]", " ", cleanish_text)
                cleaner_text = re.sub(r"\[\w\]", " " , cleanerish_text)
                clean_text = re.sub(r"\s+", " " , cleaner_text).strip() 
                biography_paragraph = clean_text
                print(clean_text)
                break
                
  
    return biography_paragraph  



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
            params = {"country": country}
            s3 = s.get(leaders_url, params=params)
            leaders = s3.json()
            
            # putting the leaders in the leaders by country dict.
            leaders_by_country[f"{country}"] = leaders
            s.get(cookies_url) # getting a new cookie
                
            # get the leader's first paragraph, adding it to its dict.
            for leader in leaders:
                wikipedia_url = leader["wikipedia_url"]
                time.sleep(0.1) # Pause before next request
                leader["Bio"] = get_first_paragraph(wikipedia_url, s)               
                 
        return leaders_by_country
   
    

# A function that takes the leaders by country variable
    # dumps it in the leaders.json file
    # opens and prints it. 
def save_leaders_by_country():
    with open("leaders.json", "w") as leaders_json:
        json.dump(leaders_by_country, leaders_json, indent=2, ensure_ascii=False)
    with open("leaders.json", "r") as file:
        print(json.load(file))


def save_leader_by_country_with_switch(format=json):
    if format == "json":
            with open("leaders.json", "w") as leaders_json:
                json.dump(leaders_by_country, leaders_json, indent=2, ensure_ascii=False)
            with open("leaders.json", "r") as file:
                print(json.load(file))
    else: 
        


        
##        
## Calling the functions:
##
    #get_leaders()
    #save_leaders_by_country()
    #print(leaders_by_country)
        pass