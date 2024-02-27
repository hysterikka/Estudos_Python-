#API: AIzaSyDz8lyuoqZBXl9nbKuQwtmWnY6uUn02qgg
import urllib.request, urllib.parse, urllib.error
import json
import ssl
api_key = 'AIzaSyDz8lyuoqZBXl9nbKuQwtmWnY6uUn02qgg'
if api_key is False:
   api_key = 42
   serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input ('Insira a localizacao: ')
    if len (address) < 1: break
    parms = dict ()
    parms ['address'] = address
    if api_key is not False: parms ['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print ('Carregando', url)
    uh = urllib.request.urlopen(url, context = ctx)
    data = uh.read().decode()
    data = ('Carregado', len (data), 'caracteres')
    try:
        js= json.loads (data)
    except:
        js = None
        if not js or 'status' not in js or js ['status'] != 'Ok':
                print ('== Falha ao encontrar endereco ==')
                print (data)
                continue
        print (json.dumps(js, indent = 4))
        lat = js ['results'] [0]['geometry']['location']['lat']
        lng = js ['results'] [0]['geometry']['location']['lng']
        print ('lat', lat, 'lng', lng)
        location  = js ['results'][0]['formated_address']
        print (location)
