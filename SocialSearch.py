import json
import requests
import argparse

banner = """
 ╔═╗╔═╗╔═╗╦╔═╗╦  ╔═╗╔═╗╔═╗╦═╗╔═╗╦ ╦
 ╚═╗║ ║║  ║╠═╣║  ╚═╗║╣ ╠═╣╠╦╝║  ╠═╣
 ╚═╝╚═╝╚═╝╩╩ ╩╩═╝╚═╝╚═╝╩ ╩╩╚═╚═╝╩ ╩
"""

print(banner)
parser = argparse.ArgumentParser(description="SocialSearch - A script to search for social links.")
parser.add_argument("-q", "--query", help="query string", required=True)
parser.add_argument("-s", "--social_networks", help="comma separated social networks", default="facebook,tiktok,instagram,snapchat,twitter,youtube,linkedin,github,pinterest")
args = parser.parse_args()

if args.query == "":
    parser.print_help()
else:
    url = "https://social-links-search.p.rapidapi.com/search-social-links"

    querystring = {"query": args.query, "social_networks": args.social_networks}

    headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "social-links-search.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)['data']

    print(" Results: \n")
    for key, value in data.items():
        if value:
            print(f" {key.capitalize()} ~> {value[0]}")
