#!/usr/bin/python3
import requests
import random

def get_qotd():
    categories = ["motivational", "inspirational", "resilience", "perseverance", "meaning"]
    tag = random.choice(categories)

    while True:
        url = f"https://zenquotes.io/api/random/{tag}"
        response = requests.get(url)
        if response.status_code == 200:
            quotes = response.json()
            quote = quotes[0]
            quote_text = quote['q']
            if 5 <= len(quote_text.split()) <= 13:
                print(f"Category: {tag} - Quote: {quote_text} — {quote['a']}")
                return f"{quote_text}"
            else:
                continue
        else:
            print("Error Retrieving Quote: " + str(response.status_code))
            break

def change_status(token, text):
    headers = {"authorization": token, "user-agent": "Samsung Fridge/6.9"}
    json = {"custom_status": {"text": text, "emoji_name": "📝"}}
    resp = requests.patch(
        "https://discord.com/api/v8/users/@me/settings", headers=headers, json=json
    )
    if resp.status_code == 200:
        return True
    else:
        return False

def get_token(tokenfile):
    fp = open(tokenfile, "r")
    discord_token = fp.read()
    fp.close()
    return discord_token.strip()


quote_of_the_day = get_qotd()
print(f"Quote of the Day: {quote_of_the_day}")
result = change_status(token=get_token("token.txt"), text=quote_of_the_day)
if not result:
    print("Status Not Updated on Discord")
else:
    print("Status Updated on Discord")
