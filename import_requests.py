import requests

url = "https://cw-api.takeaway.com/api/v29/restaurants"

querystring = {"deliveryAreaId":"00-019","postalCode":"00-019","lat":"52.22884","lng":"21.00327","limit":"0","isAccurate":"true"}

payload = ""
headers = {
    "cookie": "__cf_bm=Xdb27EzkAHz0yLkdBj3D1FeU7Z7Lt.pfNH7mYiRzcbk-1655651907-0-AdQOXAP%2FbJ%2BXogTzkrn1qREJI9O1%2BrUPUIz014V4gxdCDuTG1Opou20gAHndadhwYTEvGldJp0mKCkMfgDrRPG3R3t6bXbgKN5yeHqboEnbq",
    "authority": "cw-api.takeaway.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "pl",
    "origin": "https://www.pyszne.pl",
    "referer": "https://www.pyszne.pl/",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "x-country-code": "pl",
    "x-datadog-origin": "rum",
    "x-datadog-parent-id": "3002354828839762374",
    "x-datadog-sampled": "1",
    "x-datadog-sampling-priority": "1",
    "x-datadog-trace-id": "5703379901750062002",
    "x-language-code": "pl",
    "x-requested-with": "XMLHttpRequest",
    "x-session-id": "ac8072c7-8540-44e2-8dee-ae632613d355"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)