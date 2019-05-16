import simplejson as json
f = open('api.json', 'r')
source = f.read()
target = json.JSONDecoder().decode(source)
print(target)