import schedule
import time
import pandas as pd

import numpy as np
import cx_Oracle



# con = cx_Oracle.connect("admin/Faiqalifarooqui12@eshop.cbp5pk0tdqap.us-east-2.rds.amazonaws.com:1521/orcl")
# con.version
# con.autocommit = True
# cur= con.cursor()
# pd.read_sql_query("DELETE FROM AI_VIDEO_MESSAGE",con)
#     #con.close()
# print('Table deleted successfully!!')


# try:
#     pd.read_sql_query("DELETE FROM AI_VIDEO_MESSAGE",con)
# except:
#   print("Table entries already Deleted!!")
# finally:
#   print("The 'try except' is finished")


def Table_Manufactured():
    con = cx_Oracle.connect("admin/Faiqalifarooqui12@eshop.cbp5pk0tdqap.us-east-2.rds.amazonaws.com:1521/orcl")
    con.version
    con.autocommit = True
    cur = con.cursor()
    try:
        pd.read_sql_query("DELETE FROM AI_VIDEO_MESSAGE", con)
    except:
        print("Table entries already Deleted!!")
    finally:
        point_1 = pd.read_sql_query(
            "SELECT STORE_ID, BRANCH_ID,CUSTOMER_ID,COUNT(*) AS ORDERS FROM BASKETS GROUP BY STORE_ID,BRANCH_ID, CUSTOMER_ID ",con)
        point_2 = pd.read_sql_query(
            " SELECT STORE_ID,BRANCH_ID,CUSTOMER_ID,SUM(TOTAL_ITEMS) FROM BASKETS GROUP BY STORE_ID,BRANCH_ID, CUSTOMER_ID",
            con)
        point_3 = pd.read_sql_query(
            "SELECT STORE_ID,BRANCH_ID,CUSTOMER_ID,SUM(GROSS_PRICE) FROM BASKETS GROUP BY STORE_ID,BRANCH_ID, CUSTOMER_ID",
            con)
        point_4 = pd.read_sql_query(
            "SELECT BASKETS.STORE_ID,BASKETS.BRANCH_ID,BASKETS.CUSTOMER_ID,SUM(BASKETS.TOTAL_DISCOUNT + BASKETS.TOTAL_VOUCHER_DISCOUNT) AS VOUCHER_ADD_PROMOTION_DISCOUNT FROM BASKETS GROUP BY BASKETS.STORE_ID, BASKETS.BRANCH_ID,BASKETS.CUSTOMER_ID",
            con)
        point_5 = pd.read_sql_query(
            "SELECT STORE_ID,BRANCH_ID,CUSTOMER_ID,SUM(TOTAL_DISCOUNT) AS SAVED_BY_PROMOTIONAL_DISCOUNT FROM BASKETS GROUP BY STORE_ID,BRANCH_ID,CUSTOMER_ID",
            con)
        point_7 = pd.read_sql_query(
            "SELECT ITEMS.BRANCH_ID,REVIEW_RATING.CUSTOMER_ID,COUNT(ITEMS.ITEM_ID) AS RATED_best_ITEM FROM ITEMS ITEMS, REVIEW_RATING REVIEW_RATING WHERE ITEMS.ITEM_ID = REVIEW_RATING.ITEM_ID AND REVIEW_RATING.RATING >= 4 AND REVIEW_RATING.REVIEW_FOR = ('ITEM')  GROUP BY ITEMS.BRANCH_ID,REVIEW_RATING.CUSTOMER_ID ORDER BY BRANCH_ID",
            con)
        point_8 = pd.read_sql_query(
            "SELECT  DISTINCT STORE_ID,BRANCH_ID,CUSTOMER_ID,REPLACE(TRUNC(DATE_CREATED) - TRUNC(SYSDATE),'-','') AS DAYS_SINCE_LAST_ORDER FROM BASKETS WHERE  DATE_CREATED IN (SELECT  MAX(DATE_CREATED) FROM BASKETS GROUP BY STORE_ID,BRANCH_ID,CUSTOMER_ID)",
            con)

        merge_2_4 = pd.merge(point_2, point_4, on=['STORE_ID','BRANCH_ID', 'CUSTOMER_ID'], how='left')
        merge_2_3_4 = pd.merge(merge_2_4, point_3, on=['STORE_ID','BRANCH_ID', 'CUSTOMER_ID'], how='left')
        merge_2_3_4_5 = pd.merge(merge_2_3_4, point_5, on=['STORE_ID','BRANCH_ID', 'CUSTOMER_ID'], how='left')
        merge_2_3_4_5_7 = pd.merge(merge_2_3_4_5, point_7, on=['BRANCH_ID', 'CUSTOMER_ID'], how='left')
        merge_1_2_3_4_5_7 = pd.merge(merge_2_3_4_5_7, point_1, on=['STORE_ID','BRANCH_ID', 'CUSTOMER_ID'], how='left')
        df = pd.merge(merge_1_2_3_4_5_7, point_8, on=['STORE_ID','BRANCH_ID', 'CUSTOMER_ID'], how='left')
        df = df.replace(np.nan, 0)

        # print(df.head())
        rows = [tuple(x) for x in df.values]
        cur.executemany(
            '''INSERT INTO AI_VIDEO_MESSAGE (STORE_ID,BRANCH_ID,CUSTOMER_ID,SUM_TOTAL_ITEMS,VOUCHER_ADD_PROMOTION_DISCOUNT,SUM_GROSS_PRICE,SAVED_BY_PROMOTIONAL_DISCOUNT,RATED_BEST_ITEM,ORDERS,DAYS_SINCE_LAST_ORDER )VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)''',
            rows)
        con.commit()
        # con.close()
        print('Table Uploaded Successfully!!')


# schedule.every().day.at("23:16").do(delete_table)
schedule.every(60).seconds.do(Table_Manufactured)
# schedule.every().day.at("23:49").do(Table_Manufactured)

while True:
    schedule.run_pending()
    time.sleep(1)