import urllib2
import json

gh_id = raw_input("Enter the github username: ")

url = 'https://api.github.com/users/' + gh_id + '/followers'

result = json.load(urllib2.urlopen(url))

print("Followers: ")

i = 1
for foll in result:
	print(str(i) + ". " + foll["login"])
	i += 1


url = 'https://api.github.com/users/' + gh_id + '/following'

result = json.load(urllib2.urlopen(url))

print("Following: ")

i = 1
for foll in result:
	print(str(i) + ". " + foll["login"])
	i += 1




