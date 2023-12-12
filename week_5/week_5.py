import json
import os

nat_files = {}

with open('Artworks.csv') as artworks_file:
    artworks_csv_file = csv.DictReader(artworks_file)
    
    for artwork in artworks_csv_file:
        nationalities_str = artwork['Nationality']
        nationalities = nationalities_str.split(' ')
        
        for nat in nationalities:
            if nat_files.get(nat) is None:
                os.makedirs("res", exist_ok=True)
                with open(f"res/{nat}.json", "w") as nat_file:
                    nat_file.write(json.dumps([artwork], indent=2))
                    nat_files[nat] = True
            else:
                with open(f"res/{nat}.json", "a") as nat_file:
                    json_data = json.load(nat_file)
                    json_data.append(artwork)
                    nat_file.seek(0)
                    json.dump(json_data, nat_file, indent=2)



