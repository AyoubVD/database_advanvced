from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import sleep
import pandas as pd

my_url = "https://www.blockchain.com/btc/unconfirmed-transactions"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.find_all("div",{"class":"sc-1g6z4xm-0 hXyplo"})

def maxValueIndex():
    usd = []
    for container in containers:
        rawUsd = container.find_all('span',{'class':'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC'})
        usd.append(rawUsd[2].text.replace('$', ''))
    max_index = usd.index(max(usd))
    return max_index

def hash(x):
    hashed = []
    for container in containers:
        rawHash = container.find_all('a',{'class':'sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK'})
        hashed.append(rawHash[0].text)
    mhashed = hashed[x]
    return mhashed

def time(x):
    timed = []
    for container in containers:
        rawTime = container.find_all('span',{'class':'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC'})
        timed.append(rawTime[0].text)
    mtime = timed[x]
    return mtime

def BTC(x):
    btc = []
    for container in containers:
        rawBtc = container.find_all('span',{'class':'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC'})
        btc.append(rawBtc[1].text)
    mbtc = btc[x]
    return mbtc

def USD(x):
    usd = []
    for container in containers:
        rawUsd = container.find_all('span',{'class':'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC'})
        usd.append(rawUsd[2].text.replace('$', ''))
    musd = usd[x]
    return musd

def calculatrix(df):
    x = maxValueIndex()
    dict = {"Hash":hash(x),"Time":time(x),"BTC":BTC(x),"USD":USD(x)}
    df = df.append([dict], ignore_index=True,verify_integrity=True)
    df.to_csv("blockchain.log", header="Hash", sep='\t', mode='a')
    return df

x = maxValueIndex()
dict = {"Hash":hash(x),"Time":time(x),"BTC":BTC(x),"USD":USD(x)}
df = pd.DataFrame([dict])
df.to_csv("blockchain.log", header="Hash", index=None, sep='\t', mode='a')
print(df)

while True:
    sleep(5)
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.find_all("div",{"class":"sc-1g6z4xm-0 hXyplo"})
    df = calculatrix(df)
    print(df)