# work experience mising 
from email import header
import requests
from bs4 import BeautifulSoup
'''
import pymongo

# Connet to Database
client = pymongo.MongoClient("mongodb://localhost:27017/")
# client = pymongo.MongoClient("mongodb+srv://JobBox:JobBox@cluster0.oi8bs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# Create Database
db = client['Web-Scrapping']
# db = client['JobBox']

# Create Database Collection
collection = db['hackerranks']

'''
username = "boflynn"
# User Hacker-Rank page parser
url = f'https://www.hackerrank.com/profile/{username}'

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'
}
page = requests.get(url, headers = header)
soup = BeautifulSoup(page.content, 'html.parser')


# data(Dictionary) is final output of problem
data = {}


#========================== PROFILE INFO START ==========================

#-----Username-----
username = url.split('/')[-1]

# This is a profile information div
main_div = soup.find('div', {'id': 'content'})
profile_info_div = main_div.find('div', {'class': 'profile-sidebar'})

#-----Profile Name-----
heading_div = profile_info_div.find('h1').get_text()

#-----Location-----
location_div = profile_info_div.find('p', {'class':'profile-country'}).get_text()

#========================== PROFILE INFO END ==========================



#========================== PROFILE DATA START ==========================

# This is a main div of profile data
profile_data_div = soup.find('div', {'class': 'profile-right-pane'})

#-----Badges-----
badges_dict = {}
badges_div = profile_data_div.find('section', {'class':'section-card hacker-badges'})
badges_items = badges_div.find_all('div', {'class':'hacker-badge'})
for badges_text in badges_items:
    badge_name = badges_text.find('text').get_text()
    star_div = badges_text.find('g', {'class': 'star-section'})
    count_star = star_div.find_all('svg', {'class': 'badge-star'})
    stars = str(len(count_star)) + ' star'
    badges_dict[badge_name] = stars


#-----Verified Skill-----
certificate_list = []
skill_div = profile_data_div.find('div', {'class':'hacker-certificates'})
certificates = skill_div.find_all('a')
for i in range(len(certificates)):
    certificate_name = certificates[i].find('h2', {'class':'certificate-heading'}).get_text()
    certificate_list.append(certificate_name)


#-----Education-----
education_list = []
education_div = profile_data_div.find('ul', {'class':'ui-timeline'})
education_tag = education_div.find_all('li')
for i in range(len(education_tag)):
    dic = {}
    content = education_tag[i].find('div', {'class': 'timeline-item-content'})
    institute = content.find('h2').get_text()
    stream = content.find('p').get_text()
    dic['institute'] = institute
    dic['stream'] = stream
    education_list.append(dic)

#========================== PROFILE DATA END ==========================



# Assign KEYs to dictionaries(VALUE) for final output
data['username'] = username
data['profilname'] = heading_div
data['location'] = location_div
data['badges'] = badges_dict
data['certificates'] = certificate_list
data['education'] = education_list
data.to_csv("HackerRank.csv")
print(data)
# Insert data in MongoDB database
#collection.insert_one(data)