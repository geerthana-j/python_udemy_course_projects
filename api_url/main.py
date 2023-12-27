import requests
from send_email import send_email

api_key = "d19153d83ee54721a44b548c854c1799"

url = "https://newsapi.org/v2/everything?q=tesla&from=2023-11-26&sortBy=publishedAt&apiKey=d19153d83ee54721a44b548c854c1799"

# url = "https://newsapi.org/v2/everything?q=tesla&" \
#       "sortBy=publishedAt&apiKey=" \
#       "d19153d83ee54721a44b548c854c1799"

# Make request
request = requests.get(url)
# request = requests.get(url, headers={"Host": "newsapi.org"}, timeout=5, allow_redirects=True, verify=True)


# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"
        # body = article["title"] + "\n" + str(article["description"]) + 2 * "\n"


body = body.encode("utf-8")
send_email(message=body)