# -*- coding: utf-8 -*-
# @Time : 2023/10/21 23:03
# @Author : SummerRC
import datetime
import logging

import akshare as ak

from KPLSpider.utils.stock_utils import StockUtils


class AkShareUtils:

    @staticmethod
    def get_current_data_list():
        start_date = None
        end_date = None
        # 非交易日
        if StockUtils.today_is_a_stock_trade_day() is False:
            start_date = StockUtils.get_previous_workday_timestamp()
            end_date = start_date
        # 交易时间
        elif StockUtils.a_stock_is_trade_time():
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
            start_date = datetime.datetime.strptime(str(current_time) + ':00', '%Y-%m-%d %H:%M:%S')
            end_date = start_date
        # 非交易时间
        elif StockUtils.time_is_before_9_30_clock():
            return None
        elif StockUtils.time_is_before_13_clock():
            current_time = datetime.datetime.now().strftime('%Y-%m-%d')
            start_date = datetime.datetime.strptime(str(current_time) + ' 11:30:00', '%Y-%m-%d %H:%M:%S')
            end_date = start_date
        elif StockUtils.time_is_after_15_clock():
            current_time = datetime.datetime.now().strftime('%Y-%m-%d')
            start_date = datetime.datetime.strptime(str(current_time) + ' 15:00:00', '%Y-%m-%d %H:%M:%S')
            end_date = start_date

        logging.log(logging.DEBUG, "start_date: " + str(start_date))

        df = ak.index_zh_a_hist_min_em("000001", '1',  str(start_date), str(end_date))

        if df.empty:
            logging.log(logging.DEBUG, "start_date: " + str(start_date) + "df is empty")
        else:
            first_column = df.iloc[0, :]
            first_column = first_column.values
            return first_column.tolist()