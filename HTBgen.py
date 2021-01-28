import requests
import base64
import json
url = "https://www.hackthebox.eu/api/invite/generate"
Dor = 0 
Gever = int(input('Enter the number of invite codes: ')) 
while Dor < Gever :
        headers = {'User-Agent': ''}
        result = requests.post(url,headers=headers)  
        data = json.loads(result.text)
        parse = data['data']['code']  
        print(base64.b64decode(parse))
        Dor = Dor + 1
        
        # i didnt used any user agent , because it was working fine witout any 
