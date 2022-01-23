import requests

url = "https://api.stackexchange.com/2.3/questions?site=stackoverflow"
response = requests.get(url)
maxAmount = int(input("How many questions? "))
count = 0
print()
for data in response.json()['items']:
    if count < maxAmount:
        if data["answer_count"] == 0:
            print(data["title"])
            print(data["link"])
            print()
            count += 1
    else:
        break