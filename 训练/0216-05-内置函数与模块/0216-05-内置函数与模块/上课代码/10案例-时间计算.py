""""""
from datetime import datetime

"""
案例-计算时间差:
    计算今天到 24:00 总共还剩下多少秒
"""

now = datetime.today()
target = datetime(now.year, now.month, now.day + 1, 0, 0, 0)
diff = target - now
print(diff.total_seconds())
