"""In this example we're using GitHub's APIs and we're going to access a private repo.
In this example I will show you how to populate headers for your API call using a
OAuth token (that expires in April).
"""


import requests

url = 'https://api.github.com/repos/robot297/hello-world'

headers = {
  'Accept': 'application/vnd.github.v3+json',
  'Authorization': 'token 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' # Please note this key is set to expire
}

payload = {} # If you wanted to send data via the body that would go here

data = requests.get(url=url, headers=headers, data=payload).json()

print(data['description'])
