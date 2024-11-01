import os
import yaml
import pandas as pd 

# get all publication files 
all_pub_files = os.listdir("_publications")

# initialize list to collect data
df_list = []
for file in all_pub_files:
    pub_file = "_publications/"+file
    # open each publication file 
    with open(pub_file, 'r') as f:
        # load file - yaml thinks that the end "---" for the front matter is another document, so must work around that 
        data = yaml.load_all(f, yaml.FullLoader)
        for doc in data:
            # the last "---" will be an empty document - handle that 
            if doc is not None:
                # pull relevant info 
                d   = {
                    'title' : doc['title'],
                    'authors' : doc['authors_string'],
                    'fim_authors' : ", ".join([x for x in doc['author_ids'] if x is not None]),
                    'date' : doc['date'].strftime("%Y-%m-%d"), 
                    'journal' : doc['journal'], 
                    'volume' : doc['volume'], 
                    'pages' : doc['pages'],
                    'book_title' : doc['book_title'],
                    'publisher': doc['book_title'],
                    'abstract': doc['abstract'], 
                    'data_loc' : doc['data_loc'], 
                    'code_loc' : doc['code_loc'], 
                    'type': doc['type']
                }

                # handle a few edge cases of information 
                if doc['doi'] is not None:
                    d['doi'] = doc['doi']
                else: 
                    d['doi'] = ""

                if doc['project_id'] is not None:
                    if isinstance(doc['project_id'], list):
                        d['project_id'] = (", ").join(doc['project_id'])
                    else: 
                        d['project_id'] = doc['project_id']
                else: 
                    d['project_id']= ""
                # add info to list 
                df_list.append(d)
# once we've finished pulling all pub documents, convert to DataFrame and write out as csv
pd.DataFrame(df_list).to_csv("_data/pub_list.csv", index=False)