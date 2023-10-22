# -*- coding: utf-8 -*-
# @Time : 2023/10/21 23:03
# @Author : SummerRC
import akshare as ak


class TestAkShare:

    def __init__(self):
        pass

    def print_data(self):
        stock_zh_index_spot_df = ak.index_zh_a_hist_min_em("000001", '1',
                                                           start_date='2023-10-01 09:15:00',
                                                           end_date='2023-10-20 15:00:00')
        # writer = pd.ExcelWriter('./', engine='xlsxwriter')
        # stock_zh_index_spot_df.to_excel(sheet_name='A股指数分时数据.xlsx', excel_writer=writer)
        stock_zh_index_spot_df.to_csv('A股指数分时数据.csv')
        print(stock_zh_index_spot_df)


share = TestAkShare()
share.print_data()