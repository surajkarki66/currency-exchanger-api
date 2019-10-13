# imports
from currency_exchanger.lib import OpenExchangeClient

APP_ID = 'a1e07ee943834eeab5c861848f40211b'

client = OpenExchangeClient(APP_ID)


usd = 200

# us dollar to pound
eng = client.convert(usd,"USD","GBP")

print(eng)
