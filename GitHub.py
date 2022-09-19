import requests
from bs4 import BeautifulSoup
import re
'''
import pymongo

# Connet to Database
client = pymongo.MongoClient("mongodb://localhost:27017/")
# client = pymongo.MongoClient("mongodb+srv://JobBox:JobBox@cluster0.oi8bs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# Create Database
db = client['Web-Scrapping']
# db = client['JobBox']

# Create Database Collection
collection = db['githubs']
'''
# data(Dictionary) is final output of problem
data = {}

# User github page parser
username = "stack-raghav"
url = 'https://github.com/{username}'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# To get USERNAME
#username = url.split('/')[-1]

#-----Repositories Data START-----
url = f'https://github.com/{username}?tab=repositories'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

repository_div = soup.find('div', {'id': 'user-repositories-list'})
repository_items = repository_div.find_all('li')

# Dictionary for repository as KEY and language_dict as VALUE
repository_dict = {}

# This loop to get repository name
for item in repository_items:
  temp_list_for_make_repository_url = []
  repository = (item.find('a').get_text())
  repository = repository.strip('\n')
  repository = repository.replace(" ", "")
  temp_list_for_make_repository_url.append(repository)
  
  # Dictionary for languages and it's used percentage
  language_dict = {}

  # This loop to get languages and it's percentage used in perticular repository
  for i in temp_list_for_make_repository_url:
    url = f'https://github.com/{username}/{temp_list_for_make_repository_url[0]}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    languages_data = soup.find_all('li', {'class': 'd-inline'})

    for span in languages_data:
      language_info = span.find_all('span')
      language_name = language_info[0].get_text()
      used_percentage = language_info[1].get_text()
      # Collect data and add to language_dict
      language_dict[language_name] = used_percentage

  # Collect data and add to repository_dict
  repository_dict[repository] = language_dict

#-----Repositories Data END-----
# Some formatting
for i in repository_dict.copy().keys():
  if repository_dict[i] == {}:
      repository_dict.pop(i)
  else:
    for j in repository_dict[i].copy().keys():
      if '\n' in j:
        repository_dict[i][repository_dict[i][j]] =  re.findall('\d*[.]\d*%', j)[0]
        repository_dict[i].pop(j)
  
#print(repository_dict)
skills_dict = {}
for i in repository_dict.values():
  for j in i.keys():
    a = 1 + skills_dict.get(j, [0])[0]
    #print(skills_dict.get(j, [0,0])[1])
    b = float(i.get(j, "0%")[:-1]) + skills_dict.get(j, [0,0])[1]
    skills_dict[j] = ["",0]
    skills_dict[j][0] = a
    skills_dict[j][1] = b

skills_dict.to_csv("HackerRank.csv")
print(skills_dict)

# Assign KEYs to dictionaries(VALUE) for final output
data["username"] = username
data['repositorydata'] = repository_dict
#print(data)
'''
# Insert data in MongoDB database
collection.insert_one(data)
'''
