import pandas as pd
import json
from pandas.io.json import json_normalize 
import wget   
pd.set_option('display.max_columns', 50)  

#many thanks from
#https://github.com/hugovk/gutenberg-metadata
with open("raw_data/gutenberg-metadata.json", 'rb') as f:
    data_json = json.load(f)


metadata_gutenberg = pd.DataFrame.from_dict(data_json, orient = "index")

for col in [x for x in metadata_gutenberg.columns if x != "formaturi"]:
    metadata_gutenberg[col] = metadata_gutenberg[col].apply(lambda x: " ".join(x) )

plato_books = metadata_gutenberg[(metadata_gutenberg["author"] == "Plato") & (metadata_gutenberg["language"] == "en")]

#this ain't a plato book
plato_books = plato_books[plato_books["title"] != "The Project Gutenberg Works of Plato: An Index"]
#Aology isn't in the dialogue at all
plato_books = plato_books[plato_books["title"] != "Apology"]


download_list = []
for link_list in plato_books.formaturi:
    download_links = [x for x in link_list if x.endswith(".txt")]
    download_list += download_links

#download the selected books
for url in download_list:
    print(url)
    url_split = url.split("/")
    path_to_output_file = "raw_data/books/" + url_split[len(url_split)-1]
    wget.download(url, path_to_output_file)