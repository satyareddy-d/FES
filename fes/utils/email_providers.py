"""

API key= '3d8b25cc473f88037e9b3f8065c53c1d-7cd1ac2b-c5f61ec2'

API_base_url = 'https://api.mailgun.net/v3/sandbox9f6373e62e2e4ad993c798a2789a0197.mailgun.org'
"""
#API key: 3d8b25cc473f88037e9b3f8065c53c1d-7cd1ac2b-c5f61ec2

import requests

API_KEY= '3d8b25cc473f88037e9b3f8065c53c1d-7cd1ac2b-c5f61ec2'

API_BASE_URL = 'https://api.mailgun.net/v3/sandbox9f6373e62e2e4ad993c798a2789a0197.mailgun.org'

def send_simple_message():
    res = requests.post(
        API_BASE_URL + "/messages",
		auth=("api", API_KEY),
		data={"from": "Excited User <mailgun@sandbox9f6373e62e2e4ad993c798a2789a0197.mailgun.org>",
			"to": ["badranarayana@gmail.com"],
			"subject": "Hello, this is from mail gun",
			"text": "Testing some Mailgun awesomness!"})
    print(res)
send_simple_message()
