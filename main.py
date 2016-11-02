import scraping_settings
import tkinter
import Scraper
import Analyzer
import Trader
import Manager
import matplotlib.pyplot as plt


ticker_list = ['AAPL', 'TWTR']

manager_accounts = {}
ticker_services = {}

for ticker in ticker_list:
    ticker_services[ticker] = {'Scraper': Scraper.Ticker_Scraper(ticker), 'Analyzer': Analyzer.Ticker_Analzyer(ticker), 'Trader': Trader.Ticker_Trader(ticker)}

for ticker in ticker_services:
    cur_scraper = ticker_services[ticker]['Scraper']
    cur_trader = ticker_services[ticker]['Trader']
    cur_analyzer = ticker_services[ticker]['Analyzer']
    data_list = []
    for item in cur_scraper.get_closing_price_list():
        print(item)


