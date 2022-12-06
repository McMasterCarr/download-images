from polygon import RESTClient

import sqlalchemy as db
import time 

import requests # to get image from the web
import shutil # to save it locally

import os.path 

client = RESTClient("h8MBNalegZa122f0UA4_EpSCIwnC8D8p")

engine = db.create_engine('sqlite:///database.db')
connection = engine.connect()
metadata = db.MetaData()
asset = db.Table('asset', metadata, autoload=True, autoload_with=engine)

query = db.select([asset]) 
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()

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
        if "_DELISTED" in item.symbol:
            print("delisted") 
        elif "-" in item.symbol:
            data = getData(fixTickerSymbol(item.symbol, "-"))
        elif "." in item.symbol:
            data = getData(fixTickerSymbol(item.symbol, "."))
        else:   
            data = getData(item.symbol)
        if 'None' in str(data.branding.icon_url):
            print('No URL for ' + (data.ticker_root))
        else:
            if hasattr(data, 'ticker_root'):
                filename = str(data.ticker_root) + ".jpeg"
                if os.path.exists(filename):
                    print("File already exists, skipping")
                else: 
                    print("Requesting: "+ filename)
                    print(data)
                    print('/////////////////////////')
                    print("Icon URL: ")
                    print(data.branding.icon_url)
                    url = str(data.branding.icon_url) + "?apiKey=h8MBNalegZa122f0UA4_EpSCIwnC8D8p"
                    #print(url)
                    try:
                        download_icon(url, filename)
                    except:
                        print('download failed')
            else:
                print("Failure 1")
    else:
        print(str(item.symbol) + " is inactive")
        
            

    


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