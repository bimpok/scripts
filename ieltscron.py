#This script is scheduled to run every 2 minutes to check for if the dates are available. If available dates are found it should send emails to the respective recipients
#mentioned below.

import smtplib
import urllib.parse
import urllib.request
import msvcrt as m
from re import findall
url = "https://ielts.britishcouncil.org/nepal"
response = urllib.request.urlopen(url)
html = response.read()
htmlStr = html.decode()
findstr = "There currently are no test dates available"
pdata = findall(findstr, htmlStr)
cnt = 0
for item in pdata:
   #print(item)
   cnt = cnt+1
#print(cnt)

if cnt == 2:
	fromaddr = 'me.bpokharel@gmail.com'
	toaddrs  = 'bimpok@gmail.com,me.bpokharel@gmail.com,bsharma2039@gmail.com'
	SUBJECT = "IELTS Test Dates Available!"
	TEXT = " You will get message like this when new dates are available -- LOOKS LIKE TEST DATES ARE AVAILABLE. HURRY UP AND GET REGISTERED. ALSO INFORM ME (9841509706) AS SOON AS YOU GET THIS MESSAGE. THANKS. - BIMARSH."
	msg = 'Subject: %s\n\n%s' % (SUBJECT, TEXT)
	username = 'me.bpokharel'
	password = 'nepal@12345'
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs.split(","), msg)
	server.quit()
#input("Hit to continue...")
