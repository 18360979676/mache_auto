import os
import re
from jsonpath import jsonpath
import requests
import pandas as pd
import datetime


def trans_time(v_str):
    """转换GMT时间为标准格式"""
    GMT_FORMAT = '%a %b %d %H:%M:%S +0800 %Y'
    timeArray = datetime.datetime.strptime(v_str, GMT_FORMAT)
    ret_time = timeArray.strftime("%Y-%m-%d %H:%M:%S")
    return ret_time


headers = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br"
}

if __name__ == '__main__':
    url = 'https://m.weibo.cn/api/container/getIndex'
    page = 1
    v_weibo_file = "weibo_shanghaifengcheng.csv"
    params = {
        "containerid": "100103type=1&q={}".format("上海封城"),
        "page_type": "searchall",
        "page": page
    }
    r = requests.get(url, headers=headers, params=params)
    cards = r.json()["data"]["cards"]

    # 转发数
    reposts_count_list = jsonpath(cards, '$..mblog.reposts_count')
    # 评论数
    comments_count_list = jsonpath(cards, '$..mblog.comments_count')
    # 点赞数
    attitudes_count_list = jsonpath(cards, '$..mblog.attitudes_count')
    bid_list = jsonpath(cards, '$..mblog.bid')
    author_list = jsonpath(cards, '$..mblog.user.screen_name')
    time_list = jsonpath(cards, '$..mblog.created_at')
    text2_list = jsonpath(cards, '$..mblog.text')

    # 把列表数据保存成DataFrame数据
    df = pd.DataFrame(
        {   
            '微博bid': bid_list,
            '微博作者': author_list,
            '发布时间': time_list,
            '微博内容': text2_list,
            '转发数': reposts_count_list,
            '评论数': comments_count_list,
            '点赞数': attitudes_count_list,
        }
    )
    # 删除重复数据
    df.drop_duplicates(subset=['微博bid'], inplace=True, keep='first')
    # 再次保存csv文件
    df.to_csv(v_weibo_file, index=False, encoding='utf_8_sig')
    print('数据清洗完成')
