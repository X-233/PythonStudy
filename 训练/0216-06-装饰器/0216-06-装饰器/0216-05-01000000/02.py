"""
需要的结果如下
['201802', '201803', '201804', ..., '201912', '202001']
"""

import datetime
from dateutil.relativedelta import relativedelta  # 月份相对时间差模块

start_date = datetime.date(2018, 2, 1)
end_date = datetime.date(2020, 1, 1)
month = relativedelta(days=1)  #
result = []
while start_date <= end_date:
    print(start_date)
    result.append(start_date.strftime('%Y-%m-%d'))
    start_date = month + start_date
print(result)
