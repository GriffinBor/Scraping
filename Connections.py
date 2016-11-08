import psycopg2
import settings
import Scraper

def post_single_data(sql_db, *params):
    query_string = "INSERT INTO playground VALUES "
    param_dict = {}

    query_string += "("
    for item in params:
        query_string += "%(" + str(item) + ")s ,"
    query_string = query_string[:-1]
    query_string += ")"

    for item in params:
        param_dict[item] = item

    connection = psycopg2.connect(host=settings.SQL_HOST, dbname=sql_db, user=settings.SQL_USERNAME, password=settings.SQL_PASSWORD)
    cursor = connection.cursor()
    cursor.execute(query_string, param_dict)
    connection.commit()


def post_timestamp_data(sql_db, cur_scraper):
    query_string = "INSERT INTO playground VALUES "

    for item in range(cur_scraper.get_timestamp_length()):
        query_string += "('"
        query_string += str(cur_scraper.Ticker_Name) + "', '"
        query_string += str(cur_scraper.get_timestamp_with_offset(item)) + "', '"
        query_string += str(cur_scraper.get_closing_price(item)) + "'"
        query_string += "), "
    query_string = query_string[:-2]

    connection = psycopg2.connect(host=settings.SQL_HOST, dbname=sql_db, user=settings.SQL_USERNAME, password=settings.SQL_PASSWORD)
    cursor = connection.cursor()
    cursor.execute(query_string)
    connection.commit()


# def post_timestamp_data(sql_db, loop_length,  *params):
#     query_string = "INSERT INTO playground VALUES "
#
#     for item in range(loop_length):
#         query_string += "("
#         for param in params:
#             query_string += "'" + str(param(item)) + "', "
#             query_string += ")"
#         query_string += "), "
#
#     print(query_string[:-2])
#     connection = psycopg2.connect(host=settings.SQL_HOST, dbname=sql_db, user=settings.SQL_USERNAME, password=settings.SQL_PASSWORD)
#     cursor = connection.cursor()
#     cursor.execute(query_string)
#     connection.commit()

