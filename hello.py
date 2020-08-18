import sys

import requests

r = requests.get("https://coreyms.com")
print("\n\t" + str(r.status_code))
print("\n\t" + str(type(r)))
print("\n\t" + str(r.ok))
