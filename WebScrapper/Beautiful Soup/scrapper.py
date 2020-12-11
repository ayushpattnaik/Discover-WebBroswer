import requests
from bs4 import BeautifulSoup
url="http://www.example.com"

#Get the html
r=requests.get(url)
htmlContent=r.content
#print(htmlContent)
soup=BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify)
#Tag
#Navigable string
#BS object
#Comment
#print(type(title))
#getting the title of the html page
title=soup.title

#Getting all paras
paras=soup.find_all('p')
#print(paras)

print(soup.find('p')['class'])
#find all the elements with class lead
print(soup.find_all("p",class_="lead"))

#Get the text from the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())

#Get all anchor tags
anchors=soup.find_all('a')
print(anchors)
all_links=set()
#Get all the links on the page: 
for link in anchors:
    if(link.get('href')!='#'):
        linkText=url+link.get('href')
        all_links.add(link)
        print(linkText)
        
navbar=soup.find(id='navbarSupportedContent')
print(navbar.contents)
for elem in navbar.contents:
    print(elem)

for item in navbar.stripped_strings:
    print(item)
#print(navbar.parent)
for item in navbar.parents:
    print(item)
    print(item.name)