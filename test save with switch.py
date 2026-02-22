import json
import csv



""" with open("test.csv", "w+", newline="", encoding="utf-8") as f:
    fieldnames = ["country",
                  "id",
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
    
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for country, leaders_list in leaders_by_country.items():
        for leader in leaders_list:
            lead = {k : v for k, v, in leader.items()}
            lead["country"] = country
        
        
            try:
                writer.writerow(lead)
            except NameError:
                writer.writerow("")
                continue
     """



def save_leader_by_country_with_switch(format=json):
    with open("leaders.json", "r") as f:
        leaders_by_country = json.load(f)
    
    if format == "json":
            with open("potato.json", "w") as leaders_json:
                json.dump(leaders_by_country, leaders_json, indent=2, ensure_ascii=False)

    
    if format == "csv":
        with open("potato.csv", "w+", newline="", encoding="utf-8") as f:
            fieldnames = ["country",
                        "id",
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
    
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for country, leaders_list in leaders_by_country.items():
                for leader in leaders_list:
                    lead = {k : v for k, v, in leader.items()}
                    lead["country"] = country

                    try:
                        writer.writerow(lead)
                    except NameError:
                        writer.writerow("")
                        continue 
                

save_leader_by_country_with_switch("csv")
        