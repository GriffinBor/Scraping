import settings
import tkinter
import Scraper
import Analyzer
import Trader
import Manager
import matplotlib.pyplot as plt
import time
start_time = time.time()

ticker_list = ['AAPL', 'TWTR']

manager_accounts = {}
ticker_services = {}

for ticker in settings.TICKER_LIST:
    ticker_services[ticker] = {'Scraper': Scraper.Ticker_Scraper(ticker), 'Analyzer': Analyzer.Ticker_Analzyer(ticker),
                               'Trader': Trader.Ticker_Trader(ticker)}

# for ticker in ticker_services:
#     cur_scraper = ticker_services[ticker]['Scraper']
#     cur_trader = ticker_services[ticker]['Trader']
#     cur_analyzer = ticker_services[ticker]['Analyzer']
#     data_list = []
#     for item in cur_scraper.get_closing_price_list():
#         print(item)
#

print('\n\n\n')
print("--- %s seconds ---" % (time.time() - start_time))