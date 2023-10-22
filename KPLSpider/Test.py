# -*- coding: utf-8 -*-
# @Time : 2023/10/21 23:03
# @Author : SummerRC
import datetime

import akshare as ak


class TestAkShare:

    def __init__(self):
        pass

    def print_data(self):
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        start_date = datetime.datetime.strptime(str(current_time) + ':00', '%Y-%m-%d %H:%M:%S')
        end_date = start_date
        print(current_time)

        stock_zh_index_spot_df = ak.index_zh_a_hist_min_em("000001", '1',
                                                           str(start_date),
                                                           str(end_date))

        if stock_zh_index_spot_df.empty:
            print(str(stock_zh_index_spot_df.empty))
        else:
            first_column = stock_zh_index_spot_df.iloc[0, :]
            first_column = first_column.values
            first_column.tolist()
            for item in first_column:
                print(item)









share = TestAkShare()
share.print_data()