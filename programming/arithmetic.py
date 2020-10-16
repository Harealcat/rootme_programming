import requests
import re

def main():
	#Do request and save cookie for later
	request = requests.get('http://challenge01.root-me.org/programmation/ch1/')
	cookie = request.cookies

	#Find pattern
	pattern = re.search("U\<sub\>n\+1(.*)\<\/sub\>\<br", request.text, flags=re.S)
	calculs = pattern.group()
	list1 = calculs.split(' ')

	#Variables
	a = int(list1[3])
	b = int(list1[11])
	U0 = int((list1[15].split('\n')[0]))
	n = int(list1[-1].split('>')[1].split('<')[0])
	
	#Solve
	answer = int((n*a) + U0 - (b*(n*(n-1))/2))

	#Send answer with cookie 
	response = requests.get('http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result='+str(answer), cookies=cookie)

	#Get password
	print(response.text)

	

main()