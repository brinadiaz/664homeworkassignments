import csv
import os

nat_files = {}

with open('Artworks.csv') as artworks_file:
    artworks_csv_file = csv.DictReader(artworks_file)
    
    for artwork in artworks_csv_file:
        nationalities_str = artwork['Nationality']
        nationalities = nationalities_str.split(' ')
        
        for nat in nationalities:
            if nat_files.get(nat) is None:
                os.makedirs("art_nationalities_files", exist_ok=True)
                with open(f"art_nationalities_files/{nat}.csv", "w") as nat_file:
                    nat_dict_writer = csv.DictWriter(nat_file, artworks_csv_file.fieldnames)
                    nat_dict_writer.writeheader()
                    nat_dict_writer.writerow(artwork)
                    nat_files[nat] = True
            else:
                with open(f"art_nationalities_files/{nat}.csv", "a") as nat_file:
                    nat_dict_writer = csv.DictWriter(nat_file, artworks_csv_file.fieldnames)
                    nat_dict_writer.writerow(artwork)

