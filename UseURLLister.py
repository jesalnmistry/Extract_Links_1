import urllib, URLLister
usock = urllib.urlopen("http://in.yahoo.com/?p=us")
#usock = urllib.urlopen("http://www.google.co.in/")
parser = URLLister.URLLister()
parser.feed(usock.read())         	
usock.close()                     
parser.close()
urllist=[]
file = open("url.txt",'w')                    
for url in parser.urls: 

	file.write(url)
	file.write('\n')
file.close()
file =open("url.txt",'r')
for url in parser.urls:
     str=file.readline()
     urllist.append(str)
    
file.close()


if urllist:
   urllist.sort()
   last = urllist[-1]
   for i in range(len(urllist)-2, -1, -1):
       if last==urllist[i]: del urllist[i]
       else: last=urllist[i]

for item in urllist:
    print item
file = open("url.txt",'w') 

for item in urllist:
	file.write(item)
	file.write('\n')

file.close()


