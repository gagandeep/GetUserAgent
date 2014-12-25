from lxml import etree
import random

windows_browsers = []
linux_browsers = []
mac_browsers = []

with open("useragentswitcher.xml") as xml:
	tree = etree.parse(xml)
	#print etree.tostring(tree.getroot())
	windows_browsers = tree.xpath('//folder[@description="Browsers - Windows"]/useragent/@useragent')
	mac_browsers = tree.xpath('//folder[@description="Browsers - Mac"]/useragent/@useragent')
	linux_browsers = tree.xpath('//folder[@description="Browsers - Linux"]/useragent/@useragent')

def get_user_agent():
	rand = random.randint(1,12)
	#print rand
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