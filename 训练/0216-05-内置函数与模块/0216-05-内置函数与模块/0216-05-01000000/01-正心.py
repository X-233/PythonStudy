"""
    中华人民共和国建国与1949年10月1日，请你计算到今天为止，中国总共成立了多少秒
"""
from datetime import datetime

time_1 = datetime(year=1949, month=10, day=1, hour=0, minute=0, second=0)

now = datetime.today()


time_2 = now - time_1

all_ = time_2.total_seconds()
print(int(all_))
