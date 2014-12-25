import xml.etree.ElementTree as ET
import random

windows_browsers = []
linux_browsers = []
mac_browsers = []

with open("useragentswitcher.xml") as xml:
	tree = ET.parse(xml)
	for browser in tree.findall('.//folder[@description="Browsers - Windows"]/useragent'):
		windows_browsers.append(browser.attrib['useragent'])
	for browser in tree.findall('.//folder[@description="Browsers - Mac"]/useragent'):
		mac_browsers.append(browser.attrib['useragent'])
	for browser in tree.findall('.//folder[@description="Browsers - Linux"]/useragent'):
		linux_browsers.append(browser.attrib['useragent'])

def get_user_agent():
	rand = random.randint(1,12)
	if rand < 9:
		browsers = windows_browsers
	elif rand < 11:
		browsers = mac_browsers
	else:
		browsers = linux_browsers
	return random.choice(browsers)

def gen_user_agent():
	while True:
		yield get_user_agent()

if __name__ == '__main__':
	user_agents = gen_user_agent()
	for i in xrange(10):
		print user_agents.next()