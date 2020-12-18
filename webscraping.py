import requests
from bs4 import BeautifulSoup
url = "https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_1_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_0_1_na_na_na&as-pos=0&as-type=RECENT&suggestionId=iphone%7CMobiles&requestId=bf00dcfa-7537-48c4-bee9-8c4549d72e52&as-backfill=on"

r = requests.get(url)
#print(htmlContent)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify)

#types of object
#1 tag
#2 navigableString
#3 BeautifulSoup
#4 comment


#get all the paragraphs from the page
sd=[]
paras = soup.find_all('p')
for i in paras:
    sd.append(i.text)
    
#get the title the html page
title = soup.find_all('div', attrs={'class':'_3wU53n'})
titles_list=[]
for new in title:
    titles_list.append(new.text)
    
#get the price in html page    
price = soup.find_all('div', attrs={'class':'_1vC4OE'})
prices_list=[]
for new1 in price:
    prices_list.append(new1.text)
    
#get the ratting in html page
rat=soup.find_all('div', attrs={'class':'hGSR34'})
rating_list=[]
for new2 in rat:
    rating_list.append(new2.text)

import pandas as pd   
#converting data in csv file
df4={'title':titles_list,'price':prices_list,'rat': rating_list}
dff=pd.DataFrame(df4)       
dff.to_csv('mobile.csv')
    


#get all the anchor tags from the page
anchors = soup.find_all('a')
print(anchors)

print(soup.find('p')['id'])


anchors = soup.find_all('a')
all_links = set()
#get all the links on the page
for link in anchors:
    if(link != '#'):
       link = "https://www.flipkart.com/offers-store?otracker=nmenu_offer-zone" +link.get('href')
       all_links.add(link)
       print(link)
       type(all_links)




