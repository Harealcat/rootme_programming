import sys
import requests
import re
import base64
import subprocess
import urllib

def main():
	request = requests.get('http://challenge01.root-me.org/programmation/ch8/')
	cookie = request.cookies
	pattern = re.search("<img src=\"data:image/png;base64(.*)\" /><br", request.text)
	captcha = pattern.group()
	captcha = captcha[32:-7]
	decoded_image = base64.b64decode(captcha)

	image = open("captcha.png", 'wb')
	image.write(decoded_image)
	image.close()
	
	ocr = subprocess.Popen(["gocr" ,"-i" ,"captcha.png"], stdout=subprocess.PIPE)
	(res,_) = ocr.communicate()
	res = str(res)[2:-3]

	post_data = urllib.parse.urlencode({'cametu':res})
	headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Language':'en-US,en;q=0.5',
	'Accept-Encoding':'gzip, deflate',
	'Content-Type':'application/x-www-form-urlencoded',
	'Origin':'http://challenge01.root-me.org',
	'Referer':'http://challenge01.root-me.org/programmation/ch8/',
	'Upgrade-Insecure-Requests':'1',
	}
	proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
	print (post_data)
	response = requests.post('http://challenge01.root-me.org/programmation/ch8/', proxies=proxies, headers=headers,cookies=cookie,data=post_data)
	print(res)
	print('')
	print (response.text)
	image = open("captcha.html", 'w+')
	image.write(response.text)
	image.close()
	

main()