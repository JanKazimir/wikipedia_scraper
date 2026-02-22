import json
import csv


with open("leaders.json", "r") as f:
  leaders_by_country = json.load(f)

print(leaders_by_country)
  
#print(leaders_by_country)

# this isn't working, obviously. 

with open("test.csv", "w+", newline="", encoding="utf-8") as f:
    fieldnames = ["id",
                  "first_name",
                  "last_name", 
                  "birth_date", 
                  "death_date",
                  "place_of_birth",
                  "wikipedia_url", 
                  "start_mandate", 
                  "end_mandate", 
                  "Bio"
                  ]
    records = json.load(leaders_by_country)
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in records:
        #writer.writerow(row)
        try:
            writer.writerow(row)
        except NameError:
            print("got a null, keep going")
            continue
    



def save_leader_by_country_with_switch(format=json):
    if format == "json":
            with open("leaders.json", "w") as leaders_json:
                json.dump(leaders_by_country, leaders_json, indent=2, ensure_ascii=False)
            with open("leaders.json", "r") as file:
                print(json.load(file))
    else: 
        pass
        