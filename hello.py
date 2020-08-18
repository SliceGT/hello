import sys

import requests

# print("\n")
# print(sys.version)
# print("\n")
# print(sys.version_info)
# print("\n")
# print(sys.executable)
# print("\n")
# msg = "\n\t\tHello World"
# print(msg)

r = requests.get("https://coreyms.com")
print("\n\t" + str(r.status_code))
print("\n\t" + str(type(r)))
