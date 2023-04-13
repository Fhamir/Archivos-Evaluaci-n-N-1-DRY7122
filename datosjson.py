import json

with open('/home/devasc/labs/devnet-src/parsing/myfile.json', 'r') as json_file:
    ourjson = json.load(json_file)

print("El token de acceso es: {}".format(ourjson['access_token']))
print("El token caduca en {} segundos.".format(ourjson['expires_in']))
