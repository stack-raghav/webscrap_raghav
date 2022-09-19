from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pymongo

# Connet to Database
client = pymongo.MongoClient("mongodb://localhost:27017/")
# client = pymongo.MongoClient("mongodb+srv://JobBox:JobBox@cluster0.oi8bs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# Create Database
db = client['Web-Scrapping']
# db = client['JobBox']

# Create Database Collection
collection = db['quoras']


url = 'https://www.quora.com/profile/Shiv-Mishra-277'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)


# data(Dictionary) is final output of problem
data = {}


#-----username-----
username = url.split('/')[-1]


#-----Profile Name-----
profile_name = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[4]/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div/div/div/span/span').text


#-----Position-----
try:
    position = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[4]/div/div[1]/div[1]/div[1]/div[2]/div[2]/div').text
except:
    position = 'none'


#-----Followers-----
followers = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[4]/div/div[1]/div[1]/div[1]/div[2]/div[3]/span/span[2]/div/div').text


#-----Following-----
following = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[4]/div/div[1]/div[1]/div[1]/div[2]/div[3]/span/span[4]/div/div').text


#-----Answers-----
answers = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[4]/div/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div').text


#-----Questions-----
questions = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[4]/div/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[1]/div').text


#-----Posts-----
posts = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[4]/div/div[1]/div[2]/div/div[2]/div/div/div[4]/div/div[1]/div').text


#-----Credential info-----
try:
    credential_list = []
    credential_div = driver.find_elements(By.XPATH,"/html/body/div[2]/div[2]/div/div/div[4]/div/div[2]/div/div[1]/div[2]/div")
    for i in range(len(credential_div)):
        item = credential_div[i].text
        credential_list.append(item)
except:
    pass


#-----Spaces info-----
try:
    spaces_list = []
    spaces_div = driver.find_elements(By.XPATH,"/html/body/div[2]/div[2]/div/div/div[4]/div/div[2]/div/div[5]/div/div")
    for i in range(len(spaces_div)):
        item = spaces_div[i].text
        item_cleared = item.split('\n')[0]
        spaces_list.append(item_cleared)
    if spaces_list[-1] == "View more":
        spaces_list.pop(-1)
except:
    pass


#-----Knows-About info-----
try:
    knows_about_list = []
    knows_about_div = driver.find_elements(By.XPATH,"/html/body/div[2]/div[2]/div/div/div[4]/div/div[2]/div/div[3]/div/div")
    for i in range(len(knows_about_div)):
        item = knows_about_div[i].text
        item_cleared = item.split('\n')[0]
        knows_about_list.append(item_cleared)
    if knows_about_list[-1] == "View more":
        knows_about_list.pop(-1)
except:
    pass


# Assign KEYs to dictionaries(VALUE) for final output
data['username'] = username
data['profilename'] = profile_name
data['position'] = position
data['followers'] = followers
data['following'] = following
data['answers'] = answers
data['questions'] = questions
data['posts'] = posts 
if len(credential_list) == 0:
    data['credential'] = 'nodata'
else:
    data['credential'] = credential_list
if len(spaces_list) == 0:
    data['spaces'] = 'nodata'
else:
    data['spaces'] = spaces_list
if len(knows_about_list) == 0:
    data['knowsabout'] = 'nodata'
else:
    data['knowabout'] = knows_about_list


# Insert data in MongoDB database
collection.insert_one(data)