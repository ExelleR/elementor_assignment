
import requests
import csv

# API Endpoint
URL = "https://rickandmortyapi.com/api/character"

def fetch_data():
    params = {
        "species": "Human",
        "status": "Alive",
        "origin": "Earth"
    }
    response = requests.get(URL, params=params)
    data = response.json()
    
    characters = []
    
    # Extracting required details
    for character in data["results"]:
        name = character["name"]
        location = character["origin"]["name"]
        image = character["image"]
        characters.append([name, location, image])
        
    return characters

def write_to_csv(data):
    with open("rick_and_morty.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Location", "Image"])
        writer.writerows(data)

if __name__ == "__main__":
    data = fetch_data()
    write_to_csv(data)
