import fear_and_greed
from requests_html import HTMLSession


"""
0 - disbelieve
1 - believe
-1 - average
"""


def mass_adopt():
	greed_and_fear = fear_and_greed.get().value
	
	session = HTMLSession()

	r = session.get("https://app.gmx.io/#/dashboard")
	r.html.render()

	s = r.html.text

	longs = s[s.find("Long Positions")+16:s.find("Short Positions")-1]
	shorts = s[s.find("Short Positions")+17:s.find("Fees since")-1]

	longs = int(longs.replace(",", ""))
	shorts = int(shorts.replace(",", ""))

	if greed_and_fear < 25 and longs*1.5 < shorts:
		return 0
	if greed_and_fear > 90 and shorts*1.5 < longs:
		return 1
	return -1




