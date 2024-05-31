import json

with open('us-zips.json', 'r') as infile, open('us-zips-line-delimited.json', 'w') as outfile:
    data = json.load(infile)
    for entry in data:
        json.dump(entry, outfile)
        outfile.write('\n')
