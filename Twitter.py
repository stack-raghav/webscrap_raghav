from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pymongo
'''
# Connet to Database
client = pymongo.MongoClient("mongodb://localhost:27017/")
# client = pymongo.MongoClient("mongodb+srv://JobBox:JobBox@cluster0.oi8bs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# Create Database
db = client['Web-Scrapping']
# db = client['JobBox']

# Create Database Collection
collection = db['twitters']
'''

url = 'https://twitter.com/sachin_rt'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

# Time to load website data
time.sleep(5)


# data(Dictionary) is final output of problem
data = {}

#-----Username-----
username = url.split('/')[-1]


#-----Profile-Name-----
profile_name = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div/span[1]/span').text


#-----Information-----
info_list = []
info = driver.find_elements(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[4]/div/span')
for i in range(len(info)):
    y = info[i].text
    info_list.append(y)


#-----Tweets-----
tweets = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/div/div').text
tweets = tweets.split(' ')[0]


#-----Followers-----
followers = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[5]/div[2]/a/span[1]/span').text


#-----Following-----
following = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[5]/div[1]/a/span[1]/span').text


#-----Check Verified Account-----
try:
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div/span[2]/div/div') 
    check_verified = 'true'
except:
    check_verified = 'false'


#-----Latest Tweet-----
latest_tweet = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div/span').text


# Assign KEYs to dictionaries(VALUE) for final output
data['username'] = username
data['profilename'] = profile_name
data['verifiedaccount'] = check_verified
data['latesttweet'] = latest_tweet
data['tweets'] = tweets
data['followers'] = followers
data['followings'] = following
data['informations'] = info_list
print(data)
'''

# Insert data in MongoDB database
collection.insert_one(data)
'''