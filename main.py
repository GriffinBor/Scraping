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

# for item in scraping_settings.NAME_LIST:
#     manager_accounts[item[0]] = {'Manager': Manager.Account_Manager(item[0], item[1])}
#
# for manager in manager_accounts:
#     cur_manager = manager_accounts[manager]['Manager']
#     cur_manager.write_to_file(cur_manager.Account_Name + ', ' + cur_manager.Account_Money)
# #
for ticker in ticker_services:
    cur_scraper = ticker_services[ticker]['Scraper']
    cur_trader = ticker_services[ticker]['Trader']
    cur_analyzer = ticker_services[ticker]['Analyzer']
    data_list = []
    for item in cur_scraper.get_closing_price_list():
        print(item)
        # data_list.append(cur_scraper.get_closing_price(item))
#     print('The moving average of ' + cur_scraper.Ticker_Name + ' is: ' + str(cur_analyzer.get_moving_average(data_list, 5)))
# #


