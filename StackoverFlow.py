import requests
from bs4 import BeautifulSoup
"""
import pymongo

# Connet to Database
client = pymongo.MongoClient("mongodb://localhost:27017/")
# client = pymongo.MongoClient("mongodb+srv://JobBox:JobBox@cluster0.oi8bs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# Create Database
db = client['Web-Scrapping']
# db = client['JobBox']

# Create Database Collection
collection = db['stackoverflows']
"""
# This function convert Two lists to Dictionary
def list_to_dictionary(key_list,value_list,dict_name):
    for key in key_list:
        for value in value_list:
            dict_name[key] = value
            value_list.remove(value)
            break
    return dict_name

# data(Dictionary) is final output of problem
data = {}

# User stackover-flow page parser
url = 'https://stackoverflow.com/users/12500315/allan-cameron'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')


#-----Get Username-----
username = url.split('/')[-1]
username = username.replace("-"," ")


#-------Stats information START------
stats_div = soup.find('div', {'class': 's-card fc-light bar-md'})
sub_stats_div = stats_div.find('div', {'class': 'd-flex flex__allitems6 gs16 fw-wrap md:jc-space-between'})
stats_items = sub_stats_div.find_all('div', {'class': 'flex--item md:fl-auto'})

stats_dict = {}
stats_data = ['reputation','reached','answers','questions']
stats_value = []

# for loop used for append stats item value in list
for i in range(len(stats_items)):
    item = stats_items[i].find('div', {'class': 'fs-body3 fc-dark'}).get_text()
    stats_value.append(item)

# call function for make dictionary
list_to_dictionary(stats_data,stats_value,stats_dict)

#-----Stats informations END------


#-----Badges info START-----
badges_div = soup.find('div',{'class': 'd-flex flex__fl-equal fw-wrap gs24'})
badges_items = badges_div.find_all('div', {'class': 'flex--item s-card bar-md'})

badges_dict = {}
badges_data = ['gold','silver','bronze']
badges_value = []

# This loop to get badges value
for i in range(3):
    try:
        item = badges_items[i].find('div', {'class': 'fs-title fw-bold fc-black-800'}).get_text()
        item = item.replace("\r","")
        item = item.replace("\n","")
        item = item.replace(" ","")
        badges_value.append(item)
    except:
        item = "Not Yet"
        badges_value.append(item)

# call function for make dictionary
list_to_dictionary(badges_data,badges_value,badges_dict)

#-----Badges info END-----


#-----Community info START-----
"""
commnity_div = soup.find('ul', {'class': 'list-reset d-flex fd-column gs12 gsy'})
commnity_items = commnity_div.find_all('li')

community_dict = {}
community_data = []
community_value = []

# To get items
for i in range(len(commnity_items)):
    item = commnity_items[i].find('div', {'class': 'truncate'}).get_text()
    community_data.append(item)

# To get items value
for j in range(len(commnity_items)):
    item_value = commnity_items[j].find('div', {'class': 'flex--item fl-shrink0 ml-auto fc-light'}).get_text()
    item_value = item_value.replace("\r","")
    item_value = item_value.replace("\n","")
    item_value = item_value.replace(" ","")
    community_value.append(item_value)

# call function for make dictionary
list_to_dictionary(community_data,community_value,community_dict)

#-----Community info END-----
"""

#-----Top Tags information START------
top_tag_div = soup.find('div', {'id': 'top-tags'})
sub_top_tag_div = top_tag_div.find('div', {'class': 's-card bar-md p0'})
top_tag_items = sub_top_tag_div.find_all('div', {'class': 'p12 bb bc-black-075'})

top_tag_dict = {}
# This loop to get top-tag item name
for i in range(len(top_tag_items)):
    item = top_tag_items[i].find('div', {'class': 'flex--item ws-nowrap'}).get_text()
    item = item.replace("\n","")
    
    sub_items_div = top_tag_items[i].find('div', {'class': 'flex--item ml-auto'})
    inner_div = sub_items_div.find('div', {'class': 'd-flex gsx gs16'})
    sub_items = inner_div.find_all('div', {'class': 'flex--item d-flex ai-center'})

    sub_item_dict = {}
    sub_items_data = ['Score','Posts','Posts %']
    sub_items_value = []

    # This loop to get sub items of top-tag
    for j in range(3):
        item_value = sub_items[j].find('div', {'class': 'fs-body3 mr4'}).get_text()
        sub_items_value.append(item_value)
    
    # call function for make dictionary
    list_to_dictionary(sub_items_data,sub_items_value,sub_item_dict)

    # Add item as KEY and sub_item_dict as VALUE to top_tag_dict
    top_tag_dict[item] = sub_item_dict

#-----Top Tags information END------


#-----Top posts START-----
top_post_list = []
top_post_div = soup.find('div', {'id': 'js-top-posts'})
sub_div = top_post_div.find('div', {'class': 's-card bar-md p0'})
top_post_items = sub_div.find_all('div', {'class': 'p12 bb bc-black-075'})
for i in range(len(top_post_items)):
    item = top_post_items[i].find('div', {'class': 'flex--item fl-grow1 pr12 js-gps-track'}).get_text()
    item = item.replace("\n","")
    top_post_list.append(item)

#-----Top posts END-----


# Assign KEYs to dictionaries(VALUE) for final output
data['username'] = username
data['stats'] = stats_dict
data['badges'] = badges_dict
#data['communities'] = community_dict
data['toptags'] = top_tag_dict
data['topposts'] = top_post_list
data.to_csv("StackOverflow.csv")
print(data)
# Insert data in MongoDB database
#collection.insert_one(data)
