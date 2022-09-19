from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pymongo
"""

# Connet to Database
client = pymongo.MongoClient("mongodb://localhost:27017/")
# client = pymongo.MongoClient("mongodb+srv://JobBox:JobBox@cluster0.oi8bs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# Create Database
db = client['Web-Scrapping']
# db = client['JobBox']

# Create Database Collection
collection = db['leetcodes']

"""
url = 'https://leetcode.com/superluminal/'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)


# Time to load website data
time.sleep(5)


# This function convert Two lists to Dictionary
def list_to_dictionary(key_list,value_list,dict_name):
    for key in key_list:
        for value in value_list:
            dict_name[key] = value
            value_list.remove(value)
            break
    return dict_name

# To append element into list
def append_element_to_list(element_path,list):
    var = driver.find_element(By.XPATH, element_path).text
    list.append(var)
    return list


# data(Dictionary) is final output of problem
data = {}


#-----Username-----
username = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div[2]').text
#username = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div[2]/div').text
print(username)


#-----Profile Name-----
profilename = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div').text
print(profilename)

#-----Rank-----
rank = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div[3]/span[2]').text


#-----Community stats START-----
community_dict = {}
community_stats_keys = ['view','solution','discuss','reputation']
community_stats_values = []

# append view data
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[3]/div[2]/div[1]/div[1]/div[3]',community_stats_values)

# append solution data
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[3]/div[2]/div[2]/div[1]/div[3]',community_stats_values)

# append discuss data
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[3]/div[2]/div[3]/div[1]/div[3]',community_stats_values)

# append reputation data
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[3]/div[2]/div[4]/div[1]/div[3]',community_stats_values)

# convert into dictionary
list_to_dictionary(community_stats_keys,community_stats_values,community_dict)

#-----community stats END-----


#-----Language START-----
language_dict = {}
language_name = []
solved_problem = []

# append languages into language_name list
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[6]/div[1]/div[1]/span',language_name)
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[6]/div[2]/div[1]/span',language_name)
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[6]/div[3]/div[1]/span',language_name)

# append solved problems in perticular language into solved_problem list
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[6]/div[1]/div[2]/span[1]',solved_problem)
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[6]/div[2]/div[2]/span[1]',solved_problem)
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[6]/div[3]/div[2]/span[1]',solved_problem)

# convert into dictionary
list_to_dictionary(language_name,solved_problem,language_dict)

#-----Language END-----


#-----Skills START-----
skills_dict = {}

advanced_dict = {}
advanced_keys = []
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[8]/div[2]/div[1]/div[2]/div[1]/a/span',advanced_keys)
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[8]/div[2]/div[1]/div[2]/div[2]/a/span',advanced_keys)
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[8]/div[2]/div[1]/div[2]/div[3]/a/span',advanced_keys)
advanced_values = []
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[8]/div[2]/div[1]/div[2]/div[1]/span',advanced_values)
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[8]/div[2]/div[1]/div[2]/div[2]/span',advanced_values)
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[8]/div[2]/div[1]/div[2]/div[3]/span',advanced_values)
list_to_dictionary(advanced_keys,advanced_values,advanced_dict)

intermediate_dict = {}
intermediate_keys = []
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[8]/div[2]/div[2]/div[2]/div[1]/a/span',intermediate_keys)
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[8]/div[2]/div[2]/div[2]/div[2]/a/span',intermediate_keys)
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[8]/div[2]/div[2]/div[2]/div[3]/a/span',intermediate_keys)
intermediate_values = []
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[8]/div[2]/div[2]/div[2]/div[1]/span',intermediate_values)
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[8]/div[2]/div[2]/div[2]/div[2]/span',intermediate_values)
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[8]/div[2]/div[2]/div[2]/div[3]/span',intermediate_values)
list_to_dictionary(intermediate_keys,intermediate_values,intermediate_dict)

fundamental_dict = {}
fundamental_keys = []
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[8]/div[2]/div[3]/div[2]/div[1]/a/span',fundamental_keys)
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[8]/div[2]/div[3]/div[2]/div[2]/a/span',fundamental_keys)
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[8]/div[2]/div[3]/div[2]/div[3]/a/span',fundamental_keys)
fundamental_values = []
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[8]/div[2]/div[3]/div[2]/div[1]/span',fundamental_values)
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[8]/div[2]/div[3]/div[2]/div[2]/span',fundamental_values)
append_element_to_list('/html/body/div/div/div/div/div[1]/div/div[8]/div[2]/div[3]/div[2]/div[3]/span',fundamental_values)
list_to_dictionary(fundamental_keys,fundamental_values,fundamental_dict)

skills_dict['Advanced'] = advanced_dict
skills_dict['Intermediate'] = intermediate_dict
skills_dict['Fundamental'] = fundamental_dict

#-----Skills END-----


#-----Solved Problems START-----
solved_problems_dict = {}
problem_list = ['Total-Solved','Easy','Medium','Hard']
problem_values = []
try:
    append_element_to_list('/html/body/div/div/div/div/div[2]/div[3]/div[1]/div/div[2]/div[1]/div/div/div/div[1]',problem_values)
    append_element_to_list('/html/body/div/div/div/div/div[2]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[2]/span[1]',problem_values)
    append_element_to_list('/html/body/div/div/div/div/div[2]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[2]/span[1]',problem_values)
    append_element_to_list('/html/body/div/div/div/div/div[2]/div[3]/div[1]/div/div[2]/div[2]/div[3]/div[1]/div[2]/span[1]',problem_values)
except:
    append_element_to_list('/html/body/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/div/div[1]',problem_values)
    append_element_to_list('/html/body/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[2]/span[1]',problem_values)
    append_element_to_list('/html/body/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[2]/span[1]',problem_values)
    append_element_to_list('/html/body/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div[2]/div[3]/div[1]/div[2]/span[1]',problem_values)

list_to_dictionary(problem_list,problem_values,solved_problems_dict)

#-----Solved Problems END-----


#-----Badges START-----
try:
    badges = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div[3]/div[2]/div/div/div[1]/div/div[2]').text
except:
    badges = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div[1]/div[2]/div/div/div[1]/div/div[2]').text
#-----Badges END-----


#-----Submissions START-----
try:
    submission = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div[4]/div/div[1]/div[1]/span[1]').text
except:
    submission = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div[2]/div/div[1]/div[1]/span[1]').text
#-----Submissions END-----


# Assign KEYs to dictionaries(VALUE) for final output
data['username'] = username
data['profilename'] = profilename
data['rank'] = rank
data['lastyearsubmissions'] = submission
data['badges'] = badges
data['communitystats'] = community_dict
data['toplanguages'] = language_dict
data['topskills'] = skills_dict
data['solvedproblems'] = solved_problems_dict

data.to_csv("Leetcode.csv")
print(data)
"""
# Insert data in MongoDB database
collection.insert_one(data)
"""