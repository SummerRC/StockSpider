import logging

from KPLSpider.db.db_helper import DbHelper
from KPLSpider.utils.stock_utils import StockUtils


class AkShareDbHelper(DbHelper):

    def get_yesterday_index(self, item, spider):
        self._init_db()
        index = self.query_yesterday_index(item, spider)
        self._close_db()

        return index

    def insert_one_item_to_db(self, list_data, spider):
        if list_data is None:
            return
        if len(list_data) != 8:
            return
        self._init_db()
        self.__insert_one_item_to_db(list_data, spider)
        self._close_db()

    def _init_db(self):
        super()._init_db()

    # 查询上阵指数昨日的收盘价
    def query_yesterday_index(self, item, spider):
        timestamp = StockUtils.get_previous_workday_timestamp()
        sql = "select price_shoupan from %s where timestamp = '%s'" % (self.config_helper.db_table_name_ak_share_index,
                                                                       timestamp)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            spider.log(self.config_helper.db_table_name_ak_share_index + "表数据查询失败, exception info: " + str(e),
                       logging.ERROR)
        else:  # 如果没有异常
            spider.log(self.config_helper.db_table_name_ak_share_index + "表数据查询成功", logging.DEBUG)
        finally:
            pass

        return self.cursor.fetchone()[0]

    def __insert_one_item_to_db(self, data, spider):
        sql = (("insert into %s (timestamp, price_kaipan, price_shoupan, price_zuigao, price_zuidi, trad_num, "
                "trade_money, price_newest) value "
                "('%s', %s, %s, %s, %s, %s, %s, %s)") %
               (self.config_helper.db_table_name_ak_share_index, data[0], data[1], data[2], data[3], data[4], data[5],
                data[6], data[7]))
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            spider.log(self.config_helper.db_table_name_ak_share_index + "表数据插入失败, exception info: " + str(e),
                       logging.ERROR)
        else:  # 如果没有异常
            spider.log(self.config_helper.db_table_name_ak_share_index + "表数据插入成功", logging.DEBUG)
        finally:
            pass

    # 关闭数据库
    def _close_db(self):
        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.conn.close()