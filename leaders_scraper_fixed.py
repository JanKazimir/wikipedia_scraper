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
    to_return = ""
    
    # 1/ Making a request, checking it all works:
    ## we print the url we'll use:
    print(wikipedia_url) # keep this for the rest of the notebook
    
    ## Setting headers, making the request, printing status code:  
    headers = {"User-Agent": "Python exercise, I'll behave!"}
    r = session.get(wikipedia_url, headers=headers, timeout=10)
    # print(r.status_code) : checks for status, reactivate to debug
    
    # 2/ Retrieving the text from the request:
    ## Create a Beautifulsoup object, a empty paragraphs list.
    soup = BeautifulSoup(r.text, "html.parser")
    paragraphs = []
    
    ## Fills up the paragrapgh list with all the paragraphs
    for par in soup.find_all("p"):        
        paragraphs.append(par)  
    
    
    first_bold = par.find("b")
    # Filtering for the first paragraph that start with bold:    
    ## Looping though our paragraphs:
    for par in paragraphs:
        if not par.get_text(strip=True):   # if the paragraph is empty, skip it
            continue
        

    ### find a paragraph that begins with some bold      
        if first_bold is None:
            continue
    #print(first_bold)
    
        
        ### If the paragraph is not empty, clean it up, print its text and break.
        if first_bold:
            before_print = re.sub(r"(\(.*\[\d]\))", "", par.get_text())
            before_print2 = re.sub(r"\[\w\]", "", before_print)
            to_print = re.sub(r"\s{2,}", " ", before_print2)
            print(to_print)
            to_return = to_print
            break
    
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
        
        save_leaders_by_country()         
        return leaders_by_country
   
    

# A function that takes the leaders by country variable
    # dumps it in the leaders.json file
    # opens and prints it. 
def save_leaders_by_country():
    with open("leaders_fixed.json", "w") as leaders_json:
        json.dump(leaders_by_country, leaders_json, indent=2)
    with open("leaders_fixed.json", "r") as file:
        #print(json.load(file))
        pass

        
##        
## Calling the functions:
##
get_leaders()
#print(leaders_by_country)
save_leaders_by_country()
