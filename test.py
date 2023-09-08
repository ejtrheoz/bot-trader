from requests_html import HTMLSession
session = HTMLSession()

r = session.get("https://app.gmx.io/#/dashboard")
r.html.render()

s = r.html.text

longs = s[s.find("Long Positions")+16:s.find("Short Positions")-1]
shorts = s[s.find("Short Positions")+17:s.find("Fees since")-1]

longs = int(longs.replace(",", ""))
shorts = int(shorts.replace(",", ""))



print(longs)