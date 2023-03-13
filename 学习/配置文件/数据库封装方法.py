from 数据库 import link_sql

class Star:
    def __init__(self):
        self.conn = link_sql(1)
        self.cursor = self.conn.cursor()

    def find_star(self, star_star):
        sql = "select * from bads where star=%s"
        self.cursor.execute(sql, (star_star,))
        return self.cursor.fetchall()


if __name__ == '__main__':
    db = Star()
    # print(db.finsert_star('烤串'))
    for i in db.find_star(4.74):
        print(i)
