import requests
url="http://api.idolondemand.com/1/api/sync/{}/v1"
apikey="8e1741c1-1c77-4be0-b0eb-5084924de171"

def postrequests(function,data={},files={}):
    data["apikey"]=apikey
    callurl=url.format(function)
    r=requests.post(callurl,data=data,files=files)
    return r.json()

f = open('pics/phone_number_2.jpg', 'rb')

results = postrequests('ocrdocument', files= {'file': f}, data={'mode': 'scene_photo'})
print results