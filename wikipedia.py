import wikipediaapi
import csv

wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')

def find_links(page):
    titles = []
    page_py = wiki_wiki.page(page)
    links = page_py.links
    for title in sorted(links.keys()):
        titles.append(title)
    return titles

# Collect all rows to be written to the CSV at once
rows = [["id1","id2"]]
pages = ['Discrete mathematics', 'Portland, Oregon', 'Mars']
for link in ['Discrete mathematics', 'Portland, Oregon', 'Mars']:
    pages = pages + find_links(link)
    
print("len: " + str(len(pages)))
for i, page in enumerate(pages):
    if not i%10:
        print(i)
    links = find_links(page)
    links = [link for link in links if link in pages]
    for link in links:
        rows.append([page, link])

# Write all rows to the CSV at once
with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
