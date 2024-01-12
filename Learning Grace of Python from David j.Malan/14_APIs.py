# API - Application Programming Interface
# API is a set of routines, protocols, and tools for building software applications
# It specifies how software components should interact
# Api can be used using Request package
# pip install requests - to install requests package
# requests.get(url) - to get the data from the url,allows u to make web  requests
# let us take an example of a website api of apples itunes
# https://itunes.apple.com/search? - this is the url
# after search? we can give the parameters like term,media,entity,attribute,limit,country,lang,version,explicit
# entity=song&limit=1&term=maroon, entity is song, limit is 1, term is maroon this will give an txt file
# with the details of the song https://itunes.apple.com/search?entity=song&limit=1&term=maroon5
# we can also get the data in json format by giving the parameter &format=json but it will not make any difference
# json - javascript object notation
# json is a lightweight data-interchange format
# json is language independent it can be used in any programming language py,js,java,c,c++,c#,php,perl,etc
import requests
import json
import sys
if (len(sys.argv) == 2):
    search_term = sys.argv[1]
else:
    print("Please enter the search term")
    sys.exit()
response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=5&term=" + search_term)
# this will print the json data in the form of dictionary
# print(response.json())
# but it will be difficult to read the data so we use json.dumps() to print the data in a readable format
# print(json.dumps(response.json(), indent=2))
objects = response.json()
for object in objects["results"]:  # here object is the dictionary
    print(object["artistName"] + " - " + object["trackName"])
