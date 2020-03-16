#!/usr/bin/env python
# -*- coding:utf-8 -*-
from datetime import datetime

from jd_assistant import Assistant

if __name__ == '__main__':
    """
    重要提示：此处为示例代码之一，请移步下面的链接查看使用教程👇
    https://github.com/tychxn/jd-assistant/wiki/1.-%E4%BA%AC%E4%B8%9C%E6%8A%A2%E8%B4%AD%E5%8A%A9%E6%89%8B%E7%94%A8%E6%B3%95
    """

    sku_ids = ''  # 商品id
    area = '4_50953_58487'  # 区域id
    buy_time = ''
    asst = Assistant()  # 初始化
    asst.login_by_QRcode()  # 扫码登陆
    #asst.clear_cart()  # 清空购物车（可选）
    x = int(input('预约请安1,抢购请按2:'))
    sku_ids = input('请输入商品编号:')
    buy_time = input('请输入抢购预约时间(如2018-09-28 22:45:50.000):')
    time1 = datetime.now().strftime('%Y-%m-%d ')
    if len(buy_time) == 12 :
        buy_time = time1 + buy_time
    if x == 1:
        asst.make_reserve(sku_id=sku_ids, buy_time=buy_time)
    # """商品预约
    #        :param sku_id: 商品id
    #        :return:
    #        """

    elif x == 2:
        asst.exec_seckill_by_time(sku_ids=sku_ids, buy_time=buy_time)
    # """定时抢购
    # :param sku_ids: 商品id，多个商品id用逗号进行分割，如"123,456,789"
    # :param buy_time: 下单时间，例如：'2018-09-28 22:45:50.000'
    # :param retry: 抢购重复执行次数，可选参数，默认4次
    # :param interval: 抢购执行间隔，可选参数，默认4秒
    # :param num: 购买数量，可选参数，默认1个
    # :return:
    # """

    elif x == 3:
        asst.exec_reserve_seckill_by_time(sku_id=sku_ids, buy_time=buy_time)
    # 执行预约抢购
    # 5个参数
    # sku_id: 商品id
    # buy_time: 下单时间，例如：'2019-11-10 22:41:30.000'
    # retry: 抢购重复执行次数，可选参数，默认4次
    # interval: 抢购执行间隔，可选参数，默认4秒
    # num: 购买数量，可选参数，默认1个

    elif x == 4:
         asst.add_item_to_cart(sku_ids=sku_ids)  # 根据商品id添加购物车（可选）
         asst.use_coupon()
         asst.submit_order_by_time(buy_time=buy_time, retry=4, interval=5)  # 定时提交订单
    # 3个参数：
    # buy_time: 下单时间，例如：'2019-02-16 01:17:59.500'
    # retry: 下单重复执行次数，可选参数，默认4次
    # interval: 下单执行间隔，可选参数，默认5秒

    # asst.buy_item_in_stock(sku_ids=sku_ids, area=area, wait_all=False, stock_interval=5)  # 根据商品是否有货自动下单
    # 6个参数：
    # sku_ids: 商品id。可以设置多个商品，也可以带数量，如：'1234' 或 '1234,5678' 或 '1234:2' 或 '1234:2,5678:3'
    # area: 地区id
    # wait_all: 是否等所有商品都有货才一起下单，可选参数，默认False
    # stock_interval: 查询库存时间间隔，可选参数，默认3秒
    # submit_retry: 提交订单失败后重试次数，可选参数，默认3次
    # submit_interval: 提交订单失败后重试时间间隔，可选参数，默认5秒
