import requests

chat_id = "6799580948"
urlp = "https://t.me/zzsszzz"
url = f"https://api.telegram.org/bot6731536783:AAEAG7kqwpquRZRd5ZtxdYGFo5Jro7F0wJo/getChat?chat_id={chat_id}"

req = requests.get(url).json()
print(req)
