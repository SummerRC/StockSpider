import logging

from KPLSpider.db.db_helper import DbHelper
from KPLSpider.utils.stock_utils import StockUtils


class AkShareDbHelper(DbHelper):

    def get_yesterday_index(self, item, spider):
        self._init_db()
        index = self.query_yesterday_index(item, spider)
        self._close_db()

        return index

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

    # 关闭数据库
    def _close_db(self):
        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.conn.close()