import requests
from bs4 import BeautifulSoup as bs
import logging
from urllib.request import urlopen
# product to search
query=input("what do you want to search ")
query=query.replace(' ','+')
url='https://www.flipkart.com/search?q='+query
req=urlopen(url)
page=req.read()
soup=bs(page,'html.parser')
item=soup.findAll('div',{'class':"_1AtVbE col-12-12"})
box=item[2]
item_link='https://www.flipkart.com'+box.div.div.div.a["href"] # item which we want to scrap
product=requests.get(item_link)
product.encoding='utf-8'
product_html = bs(product.text, "html.parser")
ratingbox=product_html.find_all('div',{'class':"_3LWZlK _1BLPMq"})

ratings=[]
for i in ratingbox:
    ratings.append(i.text)
comment_headers=product_html.find_all('p',{'class':"_2-N8zT"})
review_header=[]
for i in comment_headers:
    review_header.append(i.text) 
    
comment_box=product_html.find_all('div',{'class':"t-ZTKy"})

comment=[]
for i in comment_box:
    comment.append(i.text.replace('READ MORE',''))

data={'Ratings':ratings,
      'Reviews headers':review_header,
      'Reviews':comment
     }
import pandas as pd
df=pd.DataFrame(data)
df.to_csv('FLIPKART.csv', index=False)
pd.read_csv('FLIPKART.csv')