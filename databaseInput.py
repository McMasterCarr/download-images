from polygon import RESTClient

import sqlalchemy as db
import time 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, text, update
from sqlalchemy.engine import result
import requests # to get image from the web
import shutil # to save it locally

import os.path 

client = RESTClient("h8MBNalegZa122f0UA4_EpSCIwnC8D8p")

engine = db.create_engine('sqlite:///database.db')
meta = db.MetaData(bind=engine)
MetaData.reflect(meta)
asset = db.Table('asset', meta, autoload=True, autoload_with=engine)
meta.create_all(engine)

connection = engine.connect()

query = db.select([asset]) 
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
'''
engine = db.create_engine('sqlite:///database.db')
connection = engine.connect()
metadata = db.MetaData()
asset = db.Table('asset', metadata, autoload=True, autoload_with=engine)

query = db.select([asset]) 
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
'''

def fixTickerSymbol(ResultSet, symbol):
    modidied_ticker_symbol_index = ResultSet.index(symbol)
    modidied_ticker_symbol = ResultSet[:modidied_ticker_symbol_index]
    return(modidied_ticker_symbol)

def getData(tickerSymbol):
    try:
        time.sleep(12)
        financials = client.get_ticker_details(tickerSymbol)
        return(financials)
    except:
        return(str(tickerSymbol) + " does not match with polygon API")

def sendData2Database(assetID, data):
    
    asset1 = meta.tables['asset']
    u = update(asset1)

    if hasattr(data.address, 'address1'):
        u = u.values({"address1":str(data.address.address1)})
    else:
        u = u.values({"address1" : "None"})

    if hasattr(data.address, 'address2'):
        u = u.values({"address2":str(data.address.address2)})
    else:
        u = u.values({"address2" : "None"})
        
    if hasattr(data.address, 'city'):    
        u = u.values({"city":str(data.address.city)})
    else:
        u = u.values({"city" : "None"})
    
    if hasattr(data.address, 'state'):
        u = u.values({"state":str(data.address.state)})
    else:
        u = u.values({"state" : "None"})
        
    if hasattr(data.address, 'country'):
        u = u.values({"country":str(data.address.address1)})
    else:
        u = u.values({"country" : "None"})
        
    if hasattr(data.address, 'postal_code'):
        u = u.values({"postal_code":str(data.address.postal_code)})
    else:
        u = u.values({"postal_code" : "None"})
        
    if hasattr(data.branding, 'icon_url'):
        u = u.values({"icon_url":str(data.branding.icon_url)})
    else:
        u = u.values({"icon_url" : "None"})
        
    if hasattr(data.branding, 'logo_url'):
        u = u.values({"logo_url":str(data.branding.logo_url)})
    else:
        u = u.values({"logo_url" : "None"})
        
    if hasattr(data.branding, 'light_color'):
        u = u.values({"light_color":str(data.branding.light_color)})
    else:
        u = u.values({"light_color" : "None"})
        
    if hasattr(data.branding, 'dark_color'):
        u = u.values({"dark_color":str(data.branding.dark_color)})
    else:
        u = u.values({"dark_color" : "None"})
        
    if hasattr(data, 'cik'):
        u = u.values({"cik":str(data.cik)})
    else:
        u = u.values({"cik" : "None"})
        
    if hasattr(data, 'composite_figi'):
        u = u.values({"composite_figi":str(data.composite_figi)})
    else:
        u = u.values({"composite_figi" : "None"})
        
    if hasattr(data, 'currency_name'):
        u = u.values({"currency_name":str(data.currency_name)})
    else:
        u = u.values({"currency_name" : "None"})
        
    if hasattr(data, 'currency_symbol'):
        u = u.values({"currency_symbol":str(data.currency_symbol)})
    else:
        u = u.values({"currency_symbol" : "None"})
        
    if hasattr(data, 'base_currency_name'):
        u = u.values({"base_currency_name":str(data.base_currency_name)})
    else:
        u = u.values({"base_currency_name" : "None"})
        
    if hasattr(data, 'base_currency_symbol'):
        u = u.values({"base_currency_symbol":str(data.base_currency_symbol)})
    else:
        u = u.values({"base_currency_symbol" : "None"})
      
    if hasattr(data, 'delisted_utc'):
        u = u.values({"delisted_utc":str(data.delisted_utc)})
    else:
        u = u.values({"delisted_utc" : "None"})
      
    if hasattr(data, 'description'):
        u = u.values({"description":str(data.description)})
    else:
        u = u.values({"description" : "None"})
      
    if hasattr(data, 'ticker_root'):
        u = u.values({"ticker_root":str(data.ticker_root)})
    else:
        u = u.values({"ticker_root" : "None"})
      
    if hasattr(data, 'homepage_url'):
        u = u.values({"homepage_url":str(data.homepage_url)})
    else:
        u = u.values({"homepage_url" : "None"})
      
    if hasattr(data, 'list_date'):
        u = u.values({"list_date":str(data.list_date)})
    else:
        u = u.values({"list_date" : "None"})
      
    if hasattr(data, 'locale'):
        u = u.values({"locale":str(data.locale)})
    else:
        u = u.values({"locale" : "None"})
      
    if hasattr(data, 'market'):
        u = u.values({"market":str(data.market)})
    else:
        u = u.values({"market" : "None"})
      
    if hasattr(data, 'market_cap'):
        u = u.values({"market_cap":str(data.market_cap)})
    else:
        u = u.values({"market_cap" : "None"})
      
    if hasattr(data, 'name'):
        u = u.values({"name":str(data.name)})
    else:
        u = u.values({"name" : "None"})
      
    if hasattr(data, 'phone_number'):
        u = u.values({"phone_number":str(data.phone_number)})
    else:
        u = u.values({"phone_number" : "None"})
      
    if hasattr(data, 'primary_exchange'):
        u = u.values({"primary_exchange":str(data.primary_exchange)})
    else:
        u = u.values({"primary_exchange" : "None"})
      
    if hasattr(data, 'share_class_figi'):
        u = u.values({"share_class_figi":str(data.share_class_figi)})
    else:
        u = u.values({"share_class_figi" : "None"})
      
    if hasattr(data, 'share_class_shares_outstanding'):
        u = u.values({"share_class_shares_outstanding":str(data.share_class_shares_outstanding)})
    else:
        u = u.values({"share_class_shares_outstanding" : "None"})
      
    if hasattr(data, 'sic_code'):
        u = u.values({"sic_code":str(data.sic_code)})
    else:
        u = u.values({"sic_code" : "None"})
      
    if hasattr(data, 'sic_description'):
        u = u.values({"sic_description":str(data.sic_description)})
    else:
        u = u.values({"sic_description" : "None"})
      
    if hasattr(data, 'ticker'):
        u = u.values({"ticker":str(data.ticker)})
    else:
        u = u.values({"ticker" : "None"})
      
    if hasattr(data, 'total_employees'):
        u = u.values({"total_employees":str(data.total_employees)})
    else:
        u = u.values({"total_comployees" : "None"})
      
    if hasattr(data, 'type'):
        u = u.values({"type":str(data.type)})
    else:
        u = u.values({"type" : "None"})
      
    if hasattr(data, 'weighted_shares_outstanding'):
        u = u.values({"weighted_shares_outstanding":str(data.weighted_shares_outstanding)})
    else:
        u = u.values({"weighted_shares_outstanding" : "None"})
      
    u = u.where(asset1.c.id == assetID)
    engine.execute(u)
    sql = text("SELECT * from ASSET")
    result = engine.execute(sql).first()
    return()   

def download_icon(url, filename):
    time.sleep(12)
    r = requests.get(url, stream = True)
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
    
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')

for item in ResultSet:
    if item.status == 'active':
        # for database 
        if "_DELISTED" in item.symbol:
            print("delisted") 
        elif "-" in item.symbol:
            data = getData(fixTickerSymbol(item.symbol, "-"))
        elif "." in item.symbol:
            data = getData(fixTickerSymbol(item.symbol, "."))
        else:   
            data = getData(item.symbol)
        try:
            sendData2Database(assetID=str(item.id), data=data)
            print("sendData2Database succeeded")
            print("Success with:")
            print(item.id)
            print()
        except:
            print("sendData2Database failed")
            print("Failed on:")
            print(item.id)
    else:
        print(str(item.symbol) + " is inactive")
        
print("Done with database input from databaseInput.py.")



"""

TickerDetails(active=True, 
address=CompanyAddress(address1='100 WINCHESTER CIRCLE', address2='.', city='LOS GATOS', state='CA', country=None, postal_code='95032'), 
branding=Branding(icon_url='https://api.polygon.io/v1/reference/company-branding/d3d3Lm5ldGZsaXguY29t/images/2022-01-10_icon.jpeg', logo_url='https://api.polygon.io/v1/reference/company-branding/d3d3Lm5ldGZsaXguY29t/images/2022-01-10_logo.svg', accent_color=None, light_color=None, dark_color=None), 
cik='0001065280', 
composite_figi='BBG000CL9VN6', 
currency_name='usd', 
currency_symbol=None, 
base_currency_name=None, 
base_currency_symbol=None, 
delisted_utc=None, 
description="Netflix's primary business is a streaming video on demand service now available in almost every country worldwide except China. The firm primarily generates revenue from subscriptions to its eponymous service. Netflix delivers original and third-party digital video content to PCs, internet-connected TVs, and consumer electronic devices, including tablets, video game consoles, Apple TV, Roku, and Chromecast. Netflix is the largest SVOD platform in the world with over 220 million subscribers globally.", 
ticker_root='NFLX', 
homepage_url='https://www.netflix.com', 
list_date='2002-05-23', 
locale='us', 
market='stocks', 
market_cap=125126412297.98001, 
name='NetFlix Inc', 
phone_number='408-540-3700', 
primary_exchange='XNAS', 
share_class_figi='BBG001SF6L46', 
share_class_shares_outstanding=445020000, 
sic_code='7841', 
sic_description='SERVICES-VIDEO TAPE RENTAL', 
ticker='NFLX', 
total_employees=11300, 
type='CS', 
weighted_shares_outstanding=445020494

"""


'''
File already exists, skipping
attempting to execute sendData2Database
trying
sendData2Database failed
File already exists, skipping
attempting to execute sendData2Database
trying
sendData2Database failed
^CURL does not exist, or other failure
attempting to execute sendData2Database
trying
sendData2Database failed
Requesting: DBL.jpeg
TickerDetails(active=True, address=None, branding=None, cik='0001525201', composite_figi='BBG001YCYRX0', currency_name='usd', currency_symbol=None, base_currency_name=None, base_currency_symbol=None, delisted_utc=None, description='Doubleline Opportunistic Credit Fund operates as a closed-end management investment company. Its investment objective is to seek a high total investment return by providing a high level of current income and the potential for capital appreciation. The Fund invests in debt securities, residential and commercial mortgage-backed securities, asset-backed securities, U.S. Government securities, corporate debt, international sovereign debt, and short-term investments.', ticker_root='DBL', homepage_url='https://www.doubleline.com', list_date='2012-01-27', locale='us', market='stocks', market_cap=233171261.72, name='DOUBLELINE OPPORTUNISTIC CREDIT FUND', phone_number=None, primary_exchange='XNYS', share_class_figi='BBG001YCYSP7', share_class_shares_outstanding=15590000, sic_code=None, sic_description=None, ticker='DBL', total_employees=None, type='FUND', weighted_shares_outstanding=15691202)
/////////////////////////
Icon URL: 
URL does not exist, or other failure
attempting to execute sendData2Database
trying
sendData2Database failed


'''

# tutorial from : https://www.geeksforgeeks.org/how-to-update-sqlalchemy-row-entry/