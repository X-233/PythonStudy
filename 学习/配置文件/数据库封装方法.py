from 数据库 import link_sql

class Star:
    def __init__(self):
        self.conn = link_sql(1)
        self.cursor = self.conn.cursor()

    def find_big_star(self, star_star):
        sql = "select * from bads where star>%s;"
        self.cursor.execute(sql, (star_star,))
        return self.cursor.fetchall()

    def find_links(self, links):
        sql = "select shop_tag_cate_click from bads where review_num=%s;"
        self.cursor.execute(sql, (links,))

    def __enter__(self):
        print('进入上下文管理器...')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        print('退出上下文管理器!')

if __name__ == '__main__':
    with Star() as star:
        list_1 = star.find_big_star(4.5)
    for i in list_1:
        print(i)
