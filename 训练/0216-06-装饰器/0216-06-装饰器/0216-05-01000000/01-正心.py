"""
    中华人民共和国建国与1949年10月1日，请你计算到今天为止，中国总共成立了多少秒
"""
import datetime

start_date = datetime.datetime(1949, 10, 1, 0, 0, 0)
end_date = datetime.datetime.now()
diff_date = end_date - start_date
print(diff_date.total_seconds())
