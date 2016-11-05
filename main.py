import settings
import tkinter
import Scraper
import Analyzer
import Trader
import Manager
import time
import requests
import json
start_time = time.time()

# g = open("url list.txt", "r")
#
# temp_list = []
#
# for line in g:
#     if '%' in line:
#         if '\n' in line:
#             temp_list.append(line.rstrip('\n'))
#         else:
#             temp_list.append(line)
#
# # for line in temp_list:
# #     print(line)
#
# for line in temp_list:
#     for line2 in temp_list:
#         if line2 == line:
#             temp_list.remove(line2)
#
# for line in temp_list:
#     print(line)
ticker_list = ['AAPL']

manager_accounts = {}
ticker_services = {}

for ticker in ticker_list:
    ticker_services[ticker] = {'Scraper': Scraper.Ticker_Scraper(ticker,True, False, True), 'Analyzer': Analyzer.Ticker_Analzyer(ticker),
                               'Trader': Trader.Ticker_Trader(ticker)}

for ticker in ticker_services:
    cur_scraper = ticker_services[ticker]['Scraper']
    cur_trader = ticker_services[ticker]['Trader']
    cur_analyzer = ticker_services[ticker]['Analyzer']

    data_list = []
    data_list = cur_scraper.get_long_closing_price_list()
    for item in range(cur_scraper.get_long_timestamp_length()):
        print(str(item) + ', ' + str(cur_scraper.get_long_timestamp(item)) + ', ' + str(cur_scraper.get_long_closing_price(item)))


# pizza = requests.get("https://query1.finance.yahoo.com/v10/finance/quoteSummary/AAPL?formatted=true&crumb=RnfZVQrjb%2FI&lang=en-US&region=US&modules=summaryProfile%2CfinancialData%2CrecommendationTrend%2CupgradeDowngradeHistory%2Cearnings%2CdefaultKeyStatistics%2CcalendarEvents&corsDomain=finance.yahoo.com")
#
# varib = pizza.json()
#
# f = open("newjson.json", 'w')
# f.write(json.dumps(varib, sort_keys=True, indent=4, separators=(',', ':')))

print('\n\n\n')
print("--- %s seconds ---" % (time.time() - start_time))