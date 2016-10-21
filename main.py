import scraping
import settings
import tkinter

STOCK_NAME = []
TIME_RANGE = '1d'
TIME_INTERVAL = '1m'


# def get_data():
#     data = scraping.get_all_data('AAPL', TIME_RANGE, TIME_INTERVAL)
#     for index in range(scraping.get_timestamp_length(data)):
#         listbox1.insert(tkinter.END, 'Index: ' + str(index) + ', Price: ' + str(scraping.get_high_price(data, index)) + ', Time: ' + str(scraping.get_timestamp(data, index)))
#         # print('Index: ' + str(index) + ', Price: ' + str(scraping.get_high_price(data, index)) + ', Time: ' + str(scraping.get_timestamp(data, index)))
#
#
#
# root = tkinter.Tk()
#
# listbox1 = tkinter.Listbox(root, bg='white', fg='black', height='20', width='80')
# listbox1.grid(row='1')
#
# button1 = tkinter.Button(root, command=get_data, text='BIG BUTTON')
# button1.grid(row='0')
#
#
# tkinter.mainloop()

data = scraping.get_all_data('TWTR', TIME_RANGE, TIME_INTERVAL)
f = open('test.csv' 'w')
for index in range(scraping.get_timestamp_length(data)):
    f.write(str(scraping.get_timestamp(data, index)) + ',' + str(scraping.get_high_price(data, index)))
    # print('Index: '+ str(index) + ', Price: ' + str(scraping.get_high_price(data, index)) + ', Time: ' + str(scraping.get_timestamp(data, index)))
#
# for item in settings.TICKER_LIST:
#     data = scraping.get_all_data(item, TIME_RANGE, TIME_INTERVAL)
#     print(item)
#     print(str(scraping.get_regular_open_trading_time(data)))
#     print(str(scraping.get_regular_closing_trading_time(data)))
#     print(str(scraping.get_high_price(data, scraping.get_high_price_length(data))))
#     print('\n')
